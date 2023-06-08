from django import forms
from django.forms import formset_factory
from .models import Item, ComparetiveStatement

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'description', 'unit', 'apprx_qty']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control autosize', 'cols':55}),
            'unit': forms.TextInput(attrs={'class': 'form-control unit-size'}),
            'apprx_qty': forms.NumberInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['description'].widget.attrs['rows'] = 3
        self.fields['description'].widget.attrs['data-autosize'] = 'true'
        self.fields['description'].widget.attrs['cols'] = 55

ItemFormSet = formset_factory(ItemForm, extra=1)


class ComparetiveStatementForm(forms.ModelForm):
    class Meta:
        model = ComparetiveStatement
        fields = ['title', 'project_name', 'location']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'project_name': forms.TextInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
        }

