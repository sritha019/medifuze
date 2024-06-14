from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, Appointment

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'address', 'mobile_number', 'user_type')

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'address', 'mobile_number', 'user_type')

class BookTestForm(forms.Form):
    test_id = forms.IntegerField(widget=forms.HiddenInput())

class BookAppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['doctor', 'appointment_date']
