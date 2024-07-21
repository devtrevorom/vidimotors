from django.contrib import admin
from .models import Vehicle, Vehicle_Photo
# Register your models here.

class PhotoAdmin(admin.StackedInline):
    model = Vehicle_Photo

class VehicleAdmin(admin.ModelAdmin):
    inlines = [PhotoAdmin]
    class Meta:
        model = Vehicle

admin.site.register(Vehicle_Photo)
admin.site.register(Vehicle, VehicleAdmin)