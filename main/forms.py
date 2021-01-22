from django import forms
from .models import Blog_data


class Add_blog(forms.ModelForm):

    class Meta:
        model = Blog_data
        exclude = ('likes', 'views')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'})
        }


class mainform(forms.Form):
    number = forms.CharField()
