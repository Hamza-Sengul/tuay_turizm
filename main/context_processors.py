# context_processors.py

from .models import SiteSettings

def site_settings(request):
    try:
        site_settings = SiteSettings.objects.latest('id')
        return {'site_settings': site_settings}
    except SiteSettings.DoesNotExist:
        return {}
