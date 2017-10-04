from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    url(r'Projects/$', views.projects, name = 'projects'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
