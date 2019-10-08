from django.contrib.auth.models import User,Group
from rest_framework import viewsets
from .serializers import UserSerializer, GroupSerializer, ContactSerializer, InteractionSerializer
from .models import Contacts, Interactions

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    """
    API Endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    """
    API Endpoint that allows groups to be viewed or edited
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contacts.objects.all()
    serializer_class = ContactSerializer

class InteractionViewSet(viewsets.ModelViewSet):
    queryset = Interactions.objects.all()
    serializer_class = InteractionSerializer
