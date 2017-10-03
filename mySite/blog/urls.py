from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    url(r'Blog/$', views.blog, name = 'blog'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
