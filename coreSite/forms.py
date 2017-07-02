from django import forms
class ContactForm(forms.Form):
    subject = forms.CharField(label="Subject", max_length=100,initial="What should we discuss?")
    message = forms.CharField(label="Message", widget=forms.Textarea, initial="What is your message?")
    sender = forms.EmailField(label="Your Name", initial="What is your email?")
