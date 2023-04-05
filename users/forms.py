from django.conf import settings
from django import forms
from test_app.models import Company, Person
from test_app.models import CompanyProfile, PersonProfile

#create your forms here

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = Company
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = CompanyProfile
        fields = ['name' ]

