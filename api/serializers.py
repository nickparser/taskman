from rest_framework import serializers

from . import models

class ProjectSerializer(serializers.ModelSerializer):
	tasks = serializers.StringRelatedField(many=True)

	class Meta:
		model = models.Project
		fields = ('id', 'name', 'description', 'owner', 'tasks',)
		read_only_fields = ('owner', )

class TaskSerializer(serializers.ModelSerializer):

	class Meta:
		model = models.Task
		fields = ('id', 'project', 'title', 'status', 'description', 'createdat', 'owner',)
		read_only_fields = ('owner', 'createdat', )