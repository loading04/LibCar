from .serializers import RentalSerializer
from .models import Rental
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny


class RentalListeCreate(generics.ListCreateAPIView):
    queryset = Rental.objects.all()
    serializer_class = RentalSerializer
    permission_classes = [IsAuthenticated]



class RentalRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rental.objects.all()
    serializer_class = RentalSerializer
