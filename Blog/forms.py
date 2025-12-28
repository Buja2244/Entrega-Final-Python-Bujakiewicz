from django import forms
from .models import Blog
from .models import Post

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['titulo', 'subtitulo', 'cuerpo', 'imagen']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'subtitulo': forms.TextInput(attrs={'class': 'form-control'}),
            'cuerpo': forms.Textarea(attrs={'class': 'form-control'}),
            'imagen': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titulo', 'contenido', 'imagen']