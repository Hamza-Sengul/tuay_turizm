from django.db import models

class Hotel(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=100)
    description = models.TextField()
    main_image = models.ImageField(upload_to='hotels/')
    
    def __str__(self):
        return self.name

class HotelImage(models.Model):
    hotel = models.ForeignKey(Hotel, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='hotel_images/')

    def __str__(self):
        return f"{self.hotel.name} Image"
    

class SiteSettings(models.Model):
    logo = models.ImageField(upload_to='logos/')