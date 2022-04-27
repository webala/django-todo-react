from rest_framework import serializers
from .models import Todo


class TodoSerializer(serializers.ModelSerialzer):
    class Meta:
        model = Todo
        fields = ('id', 'title', 'description', 'completed')