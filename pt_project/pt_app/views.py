from django.shortcuts import render_to_response
from django.http import HttpResponse

def login(request):
	return HttpResponse("Please login here or create account.")

def home(request):
	return render_to_response(('home.html'))


def newgame(request):
	return HttpResponse("Oh you want to play a new game huh?")