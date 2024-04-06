from django import forms
from .models import Post, Type

choices = Type.objects.all().values_list('name', 'name')
choice_list = []
for item in choices:
    choice_list.append(item)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'origin', 'author', 'type', 'history')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'type': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
            'history': forms.Textarea(attrs={'class': 'form-control'}),
            'origin': forms.TextInput(attrs={'class': 'form-control'}),
        }

class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'origin',  'type', 'history')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'type': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
            'history': forms.Textarea(attrs={'class': 'form-control'}),
            'origin': forms.TextInput(attrs={'class': 'form-control'}),
        }