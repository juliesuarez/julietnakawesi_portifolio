from django import forms

from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ["name", "email", "phone",'Message']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Add placeholders
        self.fields["name"].widget.attrs["placeholder"] = "Enter  name"
        self.fields["email"].widget.attrs["placeholder"] = "Enter the email"
        self.fields["phone"].widget.attrs["placeholder"] = "Enter the phone number"
        self.fields["Message"].widget.attrs["placeholder"] = "Enter the phone number"

