from django.contrib.auth.models import User
from rest_framework import viewsets
from .models import Card
from .permissions import IsOwnerOrReadOnly
from .serializers import CardSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import CursorPagination


class SmallCursorPagination(CursorPagination):
    page_size = 3
    ordering = '-id'


class CardViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly,)
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    pagination_class = SmallCursorPagination
#IsAuthenticatedOrReadOnly

class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly,)
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = SmallCursorPagination




