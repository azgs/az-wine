from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from forms import UserForm, UserProfileForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User, Group

def homepage(request):
    context = RequestContext(request)
    registered = False
    username = ''
    password = ''
    email = ''


    if request.POST and request.POST.get('submit') == 'Login':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/admin')

    if request.POST and request.POST.get('submit') == 'Register':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User.objects.create_user(username, email, password)
        group = Group.objects.get(name='winegrowers')
        user.is_staff = True
        group.user_set.add(user)
        #user.is_superuser = True
        user.save()
        """
        user_form = UserForm(data=request.POST)

        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            registered = True
        else:
            print user_form.errors
    else:
        user_form = UserForm()
    """
    return render_to_response('azwine/home.html', {
        'registered': registered,
    }, context)