from . serializers import GenericSerializer
from . models import GenericModel
from rest_framework import generics
# Create your views here.

class creategeneric (generics.CreateAPIView):
    serializer_class=GenericSerializer
    queryset=GenericModel.objects.all()