from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm
from django.contrib import messages
from .functions import sendEmail
# Create your views here.
def projects(request):
    return HttpResponse("Under Development")
def home(request):
    return render(request, 'coreSite/index.html', {})
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            #flash send message
            email = form.cleaned_data['sender']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sendEmail(email, subject, message)
            messages.success(request, 'Your message was sent successfully!')
        else:
            #flash finish all parts of the forms
            messages.warning(request, 'Please fill out the form completely')
    else:
        form = ContactForm()
    return render(request, 'coreSite/contact.html', {'form': form})
def blog(request):
    return render(request, 'coreSite/blog.html', {})
