from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from .forms import MainappForm

def home(requests):
	return render(requests,'index.html',{})


def create(requests):

	form = MainappForm(requests.POSTS or None)

	return render(requests,'index.html',{})
