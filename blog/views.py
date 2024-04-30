from django.shortcuts import render
from django.views import generic
from .models import Post


# Create your views here.

class PostList(generic.ListView):
#   model = Post
    queryset = Post.objects.all()
    # queryset = Post.objects.filter(author=1)
    template_name= "blog/index.html"
    paginate_by = 6

