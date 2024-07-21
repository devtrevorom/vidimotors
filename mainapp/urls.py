from django.urls import path
from . import views

app_name = 'mainapp'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('about', views.about_view, name='about'),
    path('cars', views.cars_view, name='cars'),
    path('car-details/<int:id>', views.car_details_view, name='car-details'),
    path('contact', views.contact_view, name='contact')
]