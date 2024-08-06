from .serializers import RentalSerializer
from .models import Rental
from rest_framework import generics


class RentalListeCreate(generics.ListCreateAPIView):
    queryset = Rental.objects.all()
    serializer_class = RentalSerializer


class RentalRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rental.objects.all()
    serializer_class = RentalSerializer
