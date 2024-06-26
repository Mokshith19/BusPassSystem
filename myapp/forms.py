from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Passenger, Pass

# Form for user registration, extending UserCreationForm
class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    name = forms.CharField(max_length=255)
    age = forms.IntegerField()
    contact = forms.CharField(max_length=15)

    class Meta:
        model = User
        fields = ['username', 'email', 'name', 'age', 'contact', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            # Create a Passenger instance associated with the user
            passenger = Passenger.objects.create(
                user=user,
                name=self.cleaned_data['name'],
                age=self.cleaned_data['age'],
                email=self.cleaned_data['email'],
                contact=self.cleaned_data['contact']
            )
        return user

# Form for adding a new pass
class AddPassForm(forms.ModelForm):
    class Meta:
        model = Pass
        fields = ['bus']
        widgets = {
            'bus': forms.Select()
        }
