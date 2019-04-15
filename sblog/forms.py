'''

from django import forms
from .models import Post
#from django.db import models


class ContentForm(forms.Form):
    Post.title = forms.CharField(max_length=100)
    Post.content= forms.Textarea()
    Post.Category= forms.CharField(max_length=100)
    Post.icon= forms.FileField()
    Post.post_date= forms.DateField()



'''