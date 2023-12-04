from django import forms
from .models import Authors, Tags, Quotes

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Authors
        fields = ['fullname', 'born_date', 'born_location', 'description']

class TagForm(forms.ModelForm):
    class Meta:
        model = Tags
        fields = ['name']

class QuoteForm(forms.ModelForm):
    class Meta:
        model = Quotes
        fields = ['quote', 'tags', 'author']