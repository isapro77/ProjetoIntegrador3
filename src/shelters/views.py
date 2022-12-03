from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from django.db.models import F

from rest_framework import generics

from .models import *
from .serializers import ShelterSerializer


class ShelterListView(ListView):
    model = Shelter
    template_name = "shelters/shelter_list.html"


class ShelterDetailView(DetailView):
    model = Shelter
    template_name = "shelters/shelter_detail.html"


class ShelterCreateView(CreateView):
    model = Shelter
    template_name = "shelters/shelter_new.html"
    fields = ["nome", "endereço", "CEP", "bairro", "cidade", "pet", "total", "vagas", "vacância"]


class ShelterUpdateView(UpdateView):
    model = Shelter
    template_name = "shelters/shelter_edit.html"
    fields = ["nome", "endereço", "CEP", "bairro", "cidade", "pet", "total", "vagas", "vacância"]


class ShelterDeleteView(DeleteView):
    model = Shelter
    template_name = "shelters/shelter_delete.html"
    success_url = reverse_lazy("home")


class DeviceListView(ListView):
    model = Device
    template_name = "devices/device_list.html"


class DeviceDetailView(DetailView):
    model = Device
    template_name = "devices/device_detail.html"


class DeviceCreateView(CreateView):
    model = Device
    template_name = "devices/device_new.html"
    fields = ["código", "endereço_dispositivo", "CEP", "bairro", "cidade"]


class DeviceUpdateView(UpdateView):
    model = Device
    template_name = "devices/device_edit.html"
    fields = ["código", "endereço_dispositivo", "CEP", "bairro", "cidade"]


class DeviceDeleteView(DeleteView):
    model = Device
    template_name = "devices/device_delete.html"
    success_url = reverse_lazy("home")


class ShelteredListView(ListView):
    model = Sheltered
    template_name = "sheltereds/sheltered_list.html"


class ShelteredDetailView(DetailView):
    model = Sheltered
    template_name = "sheltereds/sheltered_detail.html"


class ShelteredCreateView(CreateView):
    model = Sheltered
    template_name = "sheltereds/sheltered_new.html"
    fields = ["nome", "gênero", "idade", "etinia", "abrigo"]


class ShelteredUpdateView(UpdateView):
    model = Sheltered
    template_name = "sheltereds/sheltered_edit.html"
    fields = ["nome", "gênero", "idade", "etinia", "abrigo"]


class ShelteredDeleteView(DeleteView):
    model = Sheltered
    template_name = "sheltereds/sheltered_delete.html"
    success_url = reverse_lazy("home")


class ShelterDeviceListView(ListView):
    model = ShelterDevice
    template_name = "shelter_devices/shelter_device_list.html"


class ShelterDeviceDetailView(DetailView):
    model = ShelterDevice
    template_name = "shelter_devices/shelter_device_detail.html"


class ShelterDeviceCreateView(CreateView):
    model = ShelterDevice
    template_name = "shelter_devices/shelter_device_new.html"
    fields = ["abrigo", "dispositivo", "distância"]


class ShelterDeviceUpdateView(UpdateView):
    model = ShelterDevice
    template_name = "shelter_devices/shelter_device_edit.html"
    fields = ["abrigo", "dispositivo", "distância"]


class ShelterDeviceDeleteView(DeleteView):
    model = ShelterDevice
    template_name = "shelter_devices/shelter_device_delete.html"
    success_url = reverse_lazy("home")


class DetailShelter(generics.RetrieveAPIView):
    # queryset = Shelter.objects.all()
    queryset = ShelterDevice.objects.select_related(
        'abrigo'
    ).values(
        nome=F('abrigo__nome'),
        endereço=F('abrigo__endereço'),
        #vagas=F('abrigo__vagas'),
        pet=F('abrigo__pet'),
    ).filter(
        abrigo__vagas__gt=0
    )
    serializer_class = ShelterSerializer


'''
class DetailShelter(generics.RetrieveAPIView):
    # queryset = Shelter.objects.all()
    queryset = Device.objects.select_related('shelterdevice').values(
        nome=F('abrigo__nome'),
        endereço=F('abrigo__endereço'),
        pet=F('abrigo__pet'),
    ).filter(
        abrigo__vagas__gt=0
    )
    serializer_class = ShelterSerializer
'''