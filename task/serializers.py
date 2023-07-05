from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = 'title description completed'.split()


class TaskValidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'