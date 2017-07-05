from django.conf.urls import url
from . import views

urlpatterns = [
url(r'^$', views.home, name='home'),
url(r'^ContactMe/$', views.contact, name='contact'),
url(r'^Blog/$', views.blog, name='blog'),
url(r'^AboutMe/$', views.about, name='about'),
]
