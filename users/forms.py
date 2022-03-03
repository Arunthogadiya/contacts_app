from django import forms
from django.contrib.auth.models import User
from users.models import ContactList
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import RegexValidator
 
 
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    secret = forms.CharField(widget=forms.PasswordInput(),max_length = 20)
    class Meta:
        model = User
        fields = ['email', 'secret', 'password1']
    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        del self.fields['password2']
        self.fields['password1'].help_text = None
        self.fields['password1'].widget.attrs.update({'class': 'log-input'})
        self.fields['email'].widget.attrs.update({'class': 'log-input'})
        self.fields['secret'].widget.attrs.update({'class': 'log-input'})

class ContactListForm(forms.ModelForm):
    phone_regex = RegexValidator(
    regex=r'^\+?1?\d{9,15}$',
    message="Enter valid phone number"
    )
    phone_no = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), label="Ph No", min_length=7, validators=[phone_regex], max_length=17)
    class Meta:
        model = ContactList
        fields = ('name', 'phone_no', 'email')
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'phone_no': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.TextInput(attrs={'class':'form-control'}),
        }