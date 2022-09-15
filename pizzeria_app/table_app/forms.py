from pyexpat import model
from django import forms
from django.forms import ModelForm
from django import forms
from .models import booking, contact


class DateInput(forms.DateInput):
    input_type = "date"


class TimeInput(forms.DateTimeInput):
    input_type = "time"


class booking_form(ModelForm):
    class Meta:
        model = booking
        fields = "__all__"
        widgets = {
            "booking_date": DateInput(
                format="%d/%m/%Y",
            ),
            "booking_Tod": TimeInput(),
        }


class contact_form(ModelForm):
    class Meta:
        model = contact
        fields = "__all__"


class ContactForm(forms.Form):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email_address = forms.EmailField(max_length=150)
    subject = forms.CharField(max_length=50)
    message = forms.CharField(widget=forms.Textarea, max_length=2000)
