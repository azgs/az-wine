from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import RequestContext, loader
from forms import UserForm, UserProfileForm

def homepage(request):
    pass