from django import forms
from blog.models import BlogPost

class CreateBlogPostForm(form.ModelForm):

    class Meta:
        model = BlogPost
        fields = ['title', 'body', 'image']

        


