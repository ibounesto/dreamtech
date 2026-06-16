from django import forms
from . import models

class RegisterArticleForm(forms.ModelForm):
    class Meta:
        model = models.Article
        fields = ['image','name','description','price','categorie',]
