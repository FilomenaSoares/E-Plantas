from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    # ... (seu PostForm existente) ...
    class Meta:
        model = Post
        fields = ['title', 'post_type', 'content', 'image', 'category', 'summary', 'pdf_file']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
        widgets = {
            'body': forms.Textarea(attrs={'class': 'w-full p-2 border rounded-md', 'rows': 3, 'placeholder': 'Escreva seu comentário...'}),
        }
        labels = { 'body': '' }
