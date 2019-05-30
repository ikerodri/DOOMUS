from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from compo.models import *

class formulariregiste(UserCreationForm):
    correu = forms.EmailField()
    imatge = forms.ImageField(required=False)
    class Meta:
        model = User
        fields = ('username',
                  'password1',
                  'password2')

    def __init__(self, *args, **kwargs):
        super(formulariregiste,self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control col-5'
        self.fields['password1'].widget.attrs['class'] = 'form-control col-5'
        self.fields['password2'].widget.attrs['class'] = 'form-control col-5'
        self.fields['correu'].widget.attrs['class'] = 'form-control col-5'