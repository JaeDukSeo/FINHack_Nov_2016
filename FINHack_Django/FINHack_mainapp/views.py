from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from .forms import MainappForm,CreateRoomForm

def home(requests):
	return render(requests,'index.html',{})



def create_room(requests):
	form = CreateRoomForm(requests.POST or None )
	
	if form.is_valid():
		instance = form.save(commit = False)
		return HttpResponse('Next step for room ')

	context = {
		'form' : form
	}
	return render(requests,'create_room.html',context)

def invite(requests):

	form  = MainappForm(requests.POST or None)

	if form.is_valid():
		instance = form.save(commit = False)
		return HttpResponse('Next step ')

	context = {
		'form' : form
	}

	return render(requests,'invite.html',context)
