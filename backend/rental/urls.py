from django.urls import path
from .views import RentalListeCreate, RentalRetrieveUpdateDestroy

urlpatterns = [
    path("rentals/", RentalListeCreate.as_view(), name="rental-list-create"),
    path(
        "rentals/<int:pk>", RentalRetrieveUpdateDestroy.as_view(), name="rental-detail"
    ),
]
