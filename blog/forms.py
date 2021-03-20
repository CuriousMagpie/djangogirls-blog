from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        title = forms.CharField()
        text = forms.TextInput()
        fields = ('title', 'text')

        #Use bootstrap to create a datetime calendar selecty-thing for published_date
