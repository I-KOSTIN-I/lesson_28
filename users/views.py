
from rest_framework.generics import RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView, ListAPIView
from rest_framework.viewsets import ModelViewSet

from users.models import Location, User
from users.serialaizers import UserSerializer, LocationSerializer, UserCreateSerializer, UserDeleteSerializer, \
    UserUpdateSerializer


class LocationViewSet(ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class UserListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserCreateView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer


class UserUpdateView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserUpdateSerializer


class UserDeleteView(DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserDeleteSerializer
