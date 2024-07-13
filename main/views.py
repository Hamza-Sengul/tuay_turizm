from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Hotel, SiteSettings

def index(request):
    hotels = Hotel.objects.all()
    logo = SiteSettings.objects.last()
    return render(request, 'index.html', {'hotels': hotels, 'logo': logo})


def hotel_detail(request, pk):
    logo = SiteSettings.objects.last()
    hotel = get_object_or_404(Hotel, pk=pk)
    return render(request, 'hotel_detail.html', {'hotel': hotel, 'logo': logo})

def odalar(request):
    hotels = Hotel.objects.all()
    logo = SiteSettings.objects.last()
    return render(request, 'odalar.html', {'hotels': hotels, 'logo': logo})

def hakkimizda(request):
    hotels = Hotel.objects.all()
    logo = SiteSettings.objects.last()
    return render(request, 'hakkimizda.html', {'hotels': hotels, 'logo': logo})

def iletisim(request):
    hotels = Hotel.objects.all()
    logo = SiteSettings.objects.last()
    return render(request, 'iletisim.html', {'hotels': hotels, 'logo': logo})

def kurallar(request):
    hotels = Hotel.objects.all()
    logo = SiteSettings.objects.last()
    return render(request, 'kurallar.html', {'hotels': hotels, 'logo': logo})
