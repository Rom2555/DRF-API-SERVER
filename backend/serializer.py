from django.contrib.auth.models import User
from rest_framework import serializers

from backend.models import Adv


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name' ]

class PostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adv
        fields = ['id', 'user', 'text', 'created_at', 'updated_at',]
