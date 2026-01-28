from django.views.generic import ListView
from django.shortcuts import render
from .models import Post


class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'all_posts'


def qa_view(request):
    return render(request, 'blog/qa.html')
