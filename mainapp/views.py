from django.shortcuts import render

# Create your views here.
def home_view(request):
    return render(request, 'mainapp/index.html')

def about_view(request):
    return render(request, 'mainapp/about.html')

def cars_view(request):
    return render(request, 'mainapp/cars.html')

def contact_view(request):
    return render(request, 'mainapp/contact.html')