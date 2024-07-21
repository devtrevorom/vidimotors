from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from PIL import Image
from django.utils import timezone

# Create your models here.
class Vehicle(models.Model):
    vehicle_id = models.CharField(max_length=200)
    vehicle_name = models.CharField(max_length=200)
    model_year = models.IntegerField()
    color = models.CharField(max_length=200)
    msrp = models.IntegerField()
    dealer_discounts = models.IntegerField()
    vehicle_overview = CKEditor5Field('Text', config_name='extends', blank=True)
    date_added = models.DateField(editable=False)
    date_updated = models.DateField()

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.date_added = timezone.now()
        self.date_updated = timezone.now()
        return super(Vehicle, self).save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.vehicle_name} - {self.model_year}"

class Vehicle_Photo(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name='photos')
    photo = models.ImageField(upload_to='vehicle_photos/')

    def __str__(self):
        return f"{self.vehicle.vehicle_name} - {self.vehicle.model_year} Photos"