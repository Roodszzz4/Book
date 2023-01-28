from django import forms
from .models import *


class AuthorForm(forms.ModelForm):
    date_of_birth = forms.DateField(widget=forms.SelectDateWidget(years=[i for i in range(1700, 2032)]))
    name = forms.CharField(min_length=3)

    class Meta:
        model = Author
        fields = '__all__'
