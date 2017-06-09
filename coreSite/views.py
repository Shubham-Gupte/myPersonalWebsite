from django.shortcuts import render
from .forms import ContactForm

# Create your views here.
def home(request):
    return render(request, 'coreSite/index.html', {})
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            #flash send message
            messages.success(request, 'Your message was sent successfully!')
        else:
            #flash finish all parts of the forms
            messages.warning(request, 'Please fill out the form completely')
    else:
        form = ContactForm()
    return render(request, 'coreSite/contact.html', {'form': form})
def blog(request):
    return "Blog"
