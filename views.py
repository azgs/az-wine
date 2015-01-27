import json
import re
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User, Group
from models import Vineyard

def homepage(request):
    context = RequestContext(request)
    registered = False
    user_exists = False
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

        bad_credentials = True
        return render_to_response('azwine/home.html', {
            'registered': registered,
            'bad_credentials': bad_credentials
        }, context)

    if request.POST and request.POST.get('submit') == 'Register':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if username and email and password:

            if not username.isalnum():
                bad_username = True
                return render_to_response('azwine/home.html', {
                    'registered': registered,
                    'bad_username': bad_username
                }, context)

            if User.objects.filter(username=username).count() > 0:
                user_exists = True
                return render_to_response('azwine/home.html', {
                    'registered': registered,
                    'user_exists': user_exists
                }, context)

            user = User.objects.create_user(username, email, password)
            group = Group.objects.get(name='winegrowers')
            user.is_staff = True
            group.user_set.add(user)
            user.save()

            registered = True
            return render_to_response('azwine/home.html', {
                'registered': registered,
            }, context)

        empty_fields = True
        return render_to_response('azwine/home.html', {
            'registered': registered,
            'empty_fields': empty_fields
        }, context)

    return render_to_response('azwine/home.html', {
        'registered': registered,
    }, context)

def get_all_vineyards(extension='json'):
    models = Vineyard.objects.all()
    data = [m.vineyards_serialized() for m in models]
    return HttpResponse(json.dumps(data))