from django import forms

class BookForm():
    title=forms.CharField(label="Title", max_length=50)
    author=forms.CharField(label="Author", max_length=50)
    price=forms.IntegerField(label="Price")
    publisher=forms.CharField(label="Publisher")
    ebook=forms.BooleanField(label="Ebook", initial=True)