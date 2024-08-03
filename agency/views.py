from rest_framework import generics
from .models import Agency
from .serializers import AgencySerializer


class AgencyListCreate(generics.ListCreateAPIView):
    queryset = Agency.objects.all()
    serializer_class = AgencySerializer


class AgencyRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Agency.objects.all()
    serializer_class = AgencySerializer
