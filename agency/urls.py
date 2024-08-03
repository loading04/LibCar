from django.urls import path
from .views import AgencyListCreate, AgencyRetrieveUpdateDestroy

urlpatterns = [
    path("agencies/", AgencyListCreate.as_view(), name="agency-list-create"),
    path(
        "agencies/<int:pk>/",
        AgencyRetrieveUpdateDestroy.as_view(),
        name="agency-detail",
    ),
]
