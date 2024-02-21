from django.contrib import admin
from .models import Destination

class DestinationAdmin(admin.ModelAdmin):
    list_display = ['name', 'img', 'demo', 'desc', 'price', 'offer']

# Register your models here.
admin.site.register(Destination, DestinationAdmin)