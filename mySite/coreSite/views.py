from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from blog.models import Post
# Create your views here.
def home(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    posts = posts[0]
    return render(request, 'coreSite/index.html', {'posts':posts})
def moreAbout(request):
    return render(request, 'coreSite/about.html', {})
def postJSON(request):
    return render(request, 'coreSite/Visual.html')
