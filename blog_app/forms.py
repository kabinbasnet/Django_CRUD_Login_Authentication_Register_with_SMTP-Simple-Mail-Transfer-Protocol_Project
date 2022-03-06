from pyexpat import model
from django.forms import ModelForm
from blog_app.models import Blog


class AddBlogsNews(ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'content']
        # OR ====>>> exclude = ['author']
