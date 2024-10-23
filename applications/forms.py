from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import JobApplication

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter email'})
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    # Add Bootstrap classes to the form fields
    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter username'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter password'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Confirm password'})

class JobApplicationForm(forms.ModelForm):
    date_applied = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        input_formats=['%Y-%m-%d']
    )

    class Meta:
        model = JobApplication
        fields = ['company', 'position', 'date_applied', 'status', 'notes']

    # Add Bootstrap classes to the form fields
    def __init__(self, *args, **kwargs):
        super(JobApplicationForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            if field.widget.attrs.get('class'):
                field.widget.attrs['class'] += ' form-control'
            else:
                field.widget.attrs['class'] = 'form-control'

    def clean_company(self):
        company = self.cleaned_data.get('company')
        # Custom validation logic if needed
        return company

    def clean_position(self):
        position = self.cleaned_data.get('position')
        # Custom validation logic if needed
        return position