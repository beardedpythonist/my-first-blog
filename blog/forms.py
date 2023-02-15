from django import forms
from .models import Post

class Form1(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text')

