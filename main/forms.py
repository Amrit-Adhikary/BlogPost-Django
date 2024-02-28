from django import forms
from .models import BlogpostModel

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogpostModel
        fields = '__all__'