from django import forms


class ContactForm(forms.Form):
    """
    Form for contact page.
    """
    subject = forms.CharField(max_length=100)
    message = forms.CharField()
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)
