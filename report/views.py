from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import Template, Context

from api import models
from taskman import celerytask

def index(request):
	tasks = models.Task.objects.all()

	if tasks.count() == 0:
		return HttpResponse('<h1>No results found</h1>')
	return render_to_response('index.html', {'tasks':tasks})

def send(request):
	template = Template('index.html')
	celerytask.send(
		'Report',
		'your report',
		'nickparser@example.com',
		['lol@example.com'],
		template.render(Context())
	)
	return HttpResponse('<h1>report successful sended!</h1>')