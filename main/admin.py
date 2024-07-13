# admin.py
from django.contrib import admin
from .models import Hotel, HotelImage, SiteSettings

class HotelImageInline(admin.TabularInline):
    model = HotelImage
    extra = 1

@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'location')
    search_fields = ('name', 'location')
    inlines = [HotelImageInline]

@admin.register(HotelImage)
class HotelImageAdmin(admin.ModelAdmin):
    list_display = ('hotel', 'image')


admin.site.register(SiteSettings)
