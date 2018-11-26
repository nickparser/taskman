from django.shortcuts import render_to_response
from django.http import HttpResponse

from api import models

def index(request):
	tasks = models.Task.objects.all()

	if tasks.count() == 0:
		return HttpResponse('No results found')
	return render_to_response('index.html', {'tasks':tasks})