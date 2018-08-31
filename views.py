from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render_to_response

def home(request):
	return HttpResponse("Do you even work bro?")
	

def error(request):
	response="<html><head><title>oups</title><body>I'm not quite sure what you are doing here</body></html>"
	return HttpResponse(response)