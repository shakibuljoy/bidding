from django import forms
from django.forms.models import inlineformset_factory
from .models import Book, Author


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = (
            'title',
            'number_of_page'
        )

BookFormSet = inlineformset_factory(
    Author,
    Book,
    BookForm,
    can_delete=False,
    min_num=2,
    extra=0
)