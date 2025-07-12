from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100,label='name',required=True)
    email = forms.EmailField(label='email',required=True)
    message = forms.CharField(label='message',required=True)