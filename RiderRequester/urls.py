from django.conf.urls import url
from django.urls import path, include
from .views import (
    RiderListApiView,
    GetRiderDetailsByLocationApiView,
    RequesterListApiView,
    RequestFromRequesterApiView
)

urlpatterns = [
    path('rider', RiderListApiView.as_view()),
    path('requester', RequesterListApiView.as_view()),
    path('get_rider_details_by_location', GetRiderDetailsByLocationApiView.as_view()),
    path('apply_for_rider', RequestFromRequesterApiView.as_view()),
    path('get_all_register_ride', RequestFromRequesterApiView.as_view()),
]