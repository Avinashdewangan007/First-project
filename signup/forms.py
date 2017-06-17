from django import forms
from .models import signup

class insertdata(forms.ModelForm):
    class Meta:
        model = signup
        fields = [
            'first_name',
            'last_name',
            'date_of_birth',
            'gender',
            'email',
            'create_password',
            'reenter_password'
        ]