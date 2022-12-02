from django import forms
from django.core.exceptions import ValidationError

from .models import Post, Category


class PostForm(forms.ModelForm):
    text = forms.CharField(min_length=20)

    class Meta:
        model = Post
        fields = ['author', 'title', 'text', 'postCategory']

    def clean(self):
        cleaned_data = super().clean()
        text = cleaned_data.get("description")
        title = cleaned_data.get("title")

        if title == text:
            raise ValidationError(
                "Текст не должен быть идентичен названию."
            )

        return cleaned_data
