from django.contrib import admin
from api.models import (
    CarOwner,
    Car
)

class CarOwnerAdmin(admin.ModelAdmin):
    pass

class CarAdmin(admin.ModelAdmin):
    pass

admin.site.register(CarOwner, CarOwnerAdmin)
admin.site.register(Car, CarAdmin)
