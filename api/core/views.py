from django.shortcuts import render
from rest_framework import viewsets, permissions
from core.models import Cliente
from core.serializers import ClienteSerializer

# Create your views here.

class ClienteViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    permission_classes = [permissions.IsAuthenticated]
