from rest_framework import generics

from . import models
from . import serializers

class ProjectListView(generics.ListCreateAPIView):
	queryset = models.Project.objects.all()
	serializer_class = serializers.ProjectSerializer

	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)

class DetailProject(generics.RetrieveUpdateDestroyAPIView):
	queryset = models.Project.objects.all()
	serializer_class = serializers.ProjectSerializer

	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)


class TaskListView(generics.ListCreateAPIView):
	queryset = models.Task.objects.all()
	serializer_class = serializers.TaskSerializer

	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)

class DetailTask(generics.RetrieveUpdateDestroyAPIView):
	queryset = models.Task.objects.all()
	serializer_class = serializers.TaskSerializer

	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)