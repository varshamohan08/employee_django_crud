from django import forms

class MyForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    photo = forms.FileField(required=False)

    def clean_email(self):
        email = self.cleaned_data['email']
        if not email.endswith('@example.com'):
            raise forms.ValidationError('Email must be from @example.com domain.')
        return email

class MyUpdateForm(forms.Form):
    id = forms.IntegerField(widget=forms.HiddenInput)
    name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    photo = forms.FileField(required=False)

    def clean_email(self):
        email = self.cleaned_data['email']
        if not email.endswith('@example.com'):
            raise forms.ValidationError('Email must be from @example.com domain.')
        return email
