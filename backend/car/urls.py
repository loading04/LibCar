from django.urls import path
from .views import CarRetrieveUpdateDestroy, CarListCreate


urlpatterns = [
    path("cars/", CarListCreate.as_view(), name="car-list-create"),
    path("cars/<int:pk>/", CarRetrieveUpdateDestroy.as_view(), name="car-detail"),
]
