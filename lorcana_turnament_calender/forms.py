from django import forms

class ContactForm(forms.Form):
    city = forms.CharField(label="In welcher Stadt soll das Event stattfinden?")
    eventlocation = forms.CharField(label="Welche Location ist für die Veranstaltung geplant?")
    permit = forms.BooleanField(required=False, label="Liegt eine Genehmigung vor an diesem Veranstaltungsort Veranstaltungen auszurichten?")
    capacity = forms.IntegerField(label="Wie viele Plätze bietet der Veranstaltungsort?")
    experience = forms.CharField(widget=forms.Textarea, label="Erfahrungen als Turnierorganisator")
    name = forms.CharField(label="Name")
    email = forms.EmailField(label="Email")
    notes = forms.CharField(widget=forms.Textarea, label="Anmerkungen")