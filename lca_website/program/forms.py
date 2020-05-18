from django import forms

class RegistrationForm(forms.ModelForm):
    "Form displayed for registering a program."

    name = forms.CharField(label="Name of Program", max_length=80)
    description = forms.CharField(label="Description", max_length=255)

    eligiblity_criteria = forms.CharField(
        label="Eligibilty Criteria to Attend Program",
        max_length=255,
        required=False
    )

    date = forms.DateTimeField(label="Date and Time of Program")
    venue = forms.CharField(label="Venue", max_length=255)
