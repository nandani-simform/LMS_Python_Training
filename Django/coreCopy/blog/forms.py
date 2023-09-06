from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta :
        model = Post
        fields = ['title', 'content']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if self.user:
            self.fields['author'].initial = self.user
