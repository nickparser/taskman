from django.db import models
from django.conf import settings

class Project(models.Model):
	name = models.CharField(max_length=50)
	description = models.CharField(max_length=200, blank=True, default='')
	owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

	def __str__(self):
		return self.name

class Task(models.Model):
	title = models.CharField(max_length=50)
	status = models.CharField(max_length=50)
	description = models.CharField(max_length=200, blank=True, default='')
	createdat = models.DateTimeField(auto_now_add=True, blank=True)
	project = models.ForeignKey(Project, related_name='tasks', on_delete=models.CASCADE)
	owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

	def __str__(self):
		return '{} : {}'.format(self.id, self.title)