from rest_framework import serializers
from .models import Task

class Taskserializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        # fields = ['id', 'title', 'description', 'completed']
        fields='__all__'
