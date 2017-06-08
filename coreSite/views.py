from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'coreSite/index.html', {})
def contact(request):
    return render(request, 'coreSite/contact.html', {})
