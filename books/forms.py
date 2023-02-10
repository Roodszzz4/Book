from django import forms
from .models import *


class AuthorForm(forms.ModelForm):
    date_of_birth = forms.DateField(widget=forms.SelectDateWidget(years=[i for i in range(1700, 2032)]))
    name = forms.CharField(min_length=3)

    class Meta:
        model = Author
        fields = '__all__'

class BookForm(forms.ModelForm):
    title = forms.CharField(min_length=3)
    date_published = forms.DateField(widget=forms.SelectDateWidget(years=[i for i in range(1900, 2032)]))

    class Meta:
        model = Book
        fields = '__all__'
        exclude = ['year_of_issue']