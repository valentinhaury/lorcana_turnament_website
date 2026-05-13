from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label="Name")
    email = forms.EmailField(label="Email")
    eventlocation = forms.CharField(label="Event Location")
    city = forms.CharField(label="City")
    date = forms.DateField(label="Date")
    content = forms.CharField(widget=forms.Textarea, label="Content")