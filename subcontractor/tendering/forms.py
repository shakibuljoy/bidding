from django import forms
from django.forms import formset_factory
from .models import Item, ComparetiveStatement

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'description', 'unit', 'apprx_qty']


ItemFormSet = formset_factory(ItemForm, extra=2)


class ComparetiveStatementForm(forms.ModelForm):
    class Meta:
        model = ComparetiveStatement
        fields = ['title', 'project_name', 'location']

