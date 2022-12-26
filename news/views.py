from django.views.generic import ListView, DetailView
from .models import Post, Comment


class PostListView(ListView):
    model = Post
    template_name = 'news/news_list.html'
    context_object_name = 'posts'
    ordering = ['-created_at']
    paginate_by = 2


class PostDetailView(DetailView):
    model = Post
    queryset = None
    template_name = 'news/single.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context

