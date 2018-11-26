from rest_framework import generics, mixins

from . import models
from . import serializers

class View(generics.GenericAPIView):
	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)

class ListCreateAPIView(
	View, 
	mixins.RetrieveModelMixin, 
	mixins.UpdateModelMixin
):
	pass

class RetrieveUpdateDestroyAPIView(
	View, 
	mixins.RetrieveModelMixin,
	mixins.UpdateModelMixin,
	mixins.DestroyModelMixin
):
	pass

class ProjectView:
	queryset = models.Project.objects.all()
	serializer_class = serializers.ProjectSerializer

class TaskView:
	queryset = models.Task.objects.all()
	serializer_class = serializers.TaskSerializer

class ProjectListView(ProjectView, ListCreateAPIView):
	pass

class DetailProject(ProjectView, RetrieveUpdateDestroyAPIView):
	pass

class TaskListView(TaskView, generics.ListCreateAPIView):
	pass

class DetailTask(TaskView, RetrieveUpdateDestroyAPIView):
	pass