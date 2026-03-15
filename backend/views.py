from rest_framework import viewsets
from django.contrib.auth.models import User
from backend.models import Adv
from backend.serializer import UsersSerializer, PostsSerializer


class UsersViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UsersSerializer


class PostsViewSet(viewsets.ModelViewSet):
    queryset = Adv.objects.all()
    serializer_class = PostsSerializer
