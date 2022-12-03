from django.contrib import admin

from .models import *

admin.site.register(Shelter)
admin.site.register(Sheltered)
admin.site.register(Device)
admin.site.register(ShelterDevice)
