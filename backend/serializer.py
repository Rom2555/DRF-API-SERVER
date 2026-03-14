from rest_framework import serializers

from backend.models import Adv


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adv
        fields = ['id', 'user',]

class PostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adv
        fields = ['id', 'user', 'text', 'created_at', 'updated_at',]
