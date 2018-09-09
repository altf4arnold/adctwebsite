from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render_to_response

def home(request):
	return HttpResponse("<html><body>Do you even work bro? if yes, click <a href='tested'>here</a></body></html>")

def tested(request):
	return HttpResponse("it seems to work")

def error(request):
	response="<html><head><title>oups</title><body>I'm not quite sure what you are doing here</body></html>"
	return HttpResponse(response)