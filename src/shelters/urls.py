from django.urls import path
from .views import \
    ShelterCreateView, \
    ShelterDetailView, \
    ShelterListView, \
    ShelterUpdateView, \
    ShelterDeleteView, \
    DeviceCreateView, \
    DeviceDetailView, \
    DeviceListView, \
    DeviceUpdateView, \
    DeviceDeleteView, \
    ShelteredCreateView, \
    ShelteredDetailView, \
    ShelteredListView, \
    ShelteredUpdateView, \
    ShelteredDeleteView, \
    ShelterDeviceCreateView, \
    ShelterDeviceDetailView, \
    ShelterDeviceListView, \
    ShelterDeviceUpdateView, \
    ShelterDeviceDeleteView, \
    DetailShelter


urlpatterns = [
    path('shelters/new/', ShelterCreateView.as_view(), name='shelter_new'),
    path('shelters/<int:pk>/', ShelterDetailView.as_view(), name='shelter_detail'),
    path('shelters/<int:pk>/edit/', ShelterUpdateView.as_view(), name='shelter_edit'),
    path('shelters/<int:pk>/delete/', ShelterDeleteView.as_view(), name='shelter_delete'),
    path('shelters/', ShelterListView.as_view(), name='shelter_list'),

    path('devices/new/', DeviceCreateView.as_view(), name='device_new'),
    path('devices/<int:pk>/', DeviceDetailView.as_view(), name='device_detail'),
    path('devices/<int:pk>/edit/', DeviceUpdateView.as_view(), name='device_edit'),
    path('devices/<int:pk>/delete/', DeviceDeleteView.as_view(), name='device_delete'),
    path('devices/', DeviceListView.as_view(), name='device_list'),

    path('sheltereds/new/', ShelteredCreateView.as_view(), name='sheltered_new'),
    path('sheltereds/<int:pk>/', ShelteredDetailView.as_view(), name='sheltered_detail'),
    path('sheltereds/<int:pk>/edit/', ShelteredUpdateView.as_view(), name='sheltered_edit'),
    path('sheltereds/<int:pk>/delete/', ShelteredDeleteView.as_view(), name='sheltered_delete'),
    path('sheltereds/', ShelteredListView.as_view(), name='sheltered_list'),

    path('shelter_devices/new/', ShelterDeviceCreateView.as_view(), name='shelter_device_new'),
    path('shelter_devices/<int:pk>/', ShelterDeviceDetailView.as_view(), name='shelter_device_detail'),
    path('shelter_devices/<int:pk>/edit/', ShelterDeviceUpdateView.as_view(), name='shelter_device_edit'),
    path('shelter_devices/<int:pk>/delete/', ShelterDeviceDeleteView.as_view(), name='shelter_device_delete'),
    path('shelter_devices/', ShelterDeviceListView.as_view(), name='shelter_device_list'),

    path('api/<int:pk>/', DetailShelter.as_view(), name='shelter_detail'),
]
