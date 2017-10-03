from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
# Create your views here.
def home(request):
    return render(request, 'coreSite/index.html', {})
def moreAbout(request):
    return render(request, 'coreSite/about.html', {})
