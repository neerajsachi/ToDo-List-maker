from .models import Todo, User
from rest_framework import serializers

class ToDoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['title', 'details', 'date', 'user']  

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
