from django import forms
from .models import infocompos

class creaciocompo(forms.ModelForm):
    class Meta:
        model = infocompos
        fields = ('titol', 'instrument', 'genere', 'bpms', 'tonalitat', 'definicio', 'arxiu', 'imatge_compo')

    def __init__(self, *args, **kwargs):
        super(creaciocompo, self).__init__(*args, **kwargs)
        self.fields['titol'].widget.attrs['class'] = 'form-control col-5'
        self.fields['instrument'].widget.attrs['class'] = 'form-control col-5'
        self.fields['genere'].widget.attrs['class'] = 'form-control col-5'
        self.fields['bpms'].widget.attrs['class'] = 'form-control col-2'
        self.fields['tonalitat'].widget.attrs['class'] = 'form-control col-2'
        self.fields['definicio'].widget.attrs['class'] = 'form-control col-5'