from django import forms
from .models import Book
class BookForm(forms.ModelForm):
    title=forms.CharField(label="Title ", max_length=50)
    author=forms.CharField(label="Author ", max_length=50)
    price=forms.IntegerField(label="Price ")
    publisher=forms.CharField(label="Publisher ")
    ebook=forms.BooleanField(label="Ebook", initial=True)
    class Meta:
        model=Book
        fields="__all__"