from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


class NameForm(forms.Form):
    param1 = forms.IntegerField(
        label='Establishing threat hunting goals:')
    param2 = forms.IntegerField(
        label='Current coverage of threat hunting goals:')
    param3 = forms.IntegerField(
        label='Hiring personnel dedicated to threat hunting:')
    param4 = forms.IntegerField(
        label='Formulating a threat hunting hypothesis:')
    param5 = forms.IntegerField(
        label='Acquiring specialized datasets and tools:')
    param6 = forms.IntegerField(
        label='Threat hunting training:')
    param7 = forms.IntegerField(
        label='SOC members who can develop needed cybersecurity scripts:')
    param8 = forms.IntegerField(
        label='Utilizing full packet capture:')
    param9 = forms.IntegerField(
        label='Utilizing windows registry keys:')
    param10 = forms.IntegerField(
        label='Utilizing system memory:')
    param11 = forms.IntegerField(
        label='Ability to scale threat hunting program:')
