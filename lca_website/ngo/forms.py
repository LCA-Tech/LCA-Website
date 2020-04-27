from django import forms
from django.core.validators import validate_email, URLValidator


class SignupForm(forms.ModelForm):
    NGO_CATEGORY = (
        (0, "Zero"),
        (1, "One"),
    )
    name = forms.CharField(label="Name of the NGO", max_length=100)
    registration_number = forms.CharField(
        label="Registration number of the NGO", max_length=25
    )
    category = forms.ChoiceField(
        label="Category to which the NGO belongs", choices=NGO_CATEGORY
    )
    address = forms.CharField(label="Address of the NGO", max_length=255)
    contact_number = forms.CharField(
        label="Contact Number of the NGO", max_length=10, min_length=10
    )
    email_address = forms.CharField(
        label="Email address of the NGO", max_length=255, validators=[validate_email]
    )
    website = forms.CharField(
        label="Website of the NGO",
        max_length=75,
        validators=[URLValidator()],
        required=False,
    )
    agree_to_tnc = forms.BooleanField(required=True)
