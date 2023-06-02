from django import forms
from django.forms import formset_factory
from .models import Item, ComparetiveStatement

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'description', 'unit', 'apprx_qty']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'unit': forms.TextInput(attrs={'class': 'form-control'}),
            'apprx_qty': forms.NumberInput(attrs={'class': 'form-control'}),
        }


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
