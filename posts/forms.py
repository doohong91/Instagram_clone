from django import forms
from .models import Post

class PostModelForm(forms.ModelForm):
    content = forms.CharField(label='content')
    
    class Meta:
        model = Post
        # input을 만들 column을 list로 만들어 넣어줌.
        fields = ['content',]