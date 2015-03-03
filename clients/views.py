from django.conf import settings
from django.shortcuts import  render
from django.http import *
from django.shortcuts import render_to_response,redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

from .models import MyClient, MyAdmin


def home (request):
	return render(request, 'default.html') #the default home page


def loginU(request):                               #the login request.
    logout(request)
    username = password = ''
    if request.method == 'POST':
        data = request.POST
        # username = request.POST['username']
        # password = request.POST['password']
        username = data['username']
        password = data['password']
        print data

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/firstview/ad')
    #return render_to_response('error.html', context_instance=RequestContext(request))


def firstvw(request):
    return render(request, 'home.html', {
        'socket_port': settings.SOCKJS_PORT,
        'socket_channel': settings.SOCKJS_CHANNEL
    })


@login_required                                     #this makes only registered users have access to the admin.
def myadmin(request):
	return render(request, 'admin.html',{
		'socket_channel':settings.SOCKJS_CHANNEL,
		'socket_port': settings.SOCKJS_PORT
		})
