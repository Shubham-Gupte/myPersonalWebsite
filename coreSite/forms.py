from django import forms
class ContactForm(forms.Form):
    subject = forms.CharField(label="Subject", max_length=100,)
    message = forms.CharField(label="Message", widget=forms.Textarea)
    sender = forms.EmailField(label="Your Name")
