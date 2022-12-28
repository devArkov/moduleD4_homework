from django.views.generic import ListView, DetailView, CreateView
from django.shortcuts import render

from .models import Post, Category
from .filters import PostFilter
from .forms import NewsForm


class PostListView(ListView):
    model = Post
    template_name = 'news/news_list.html'
    context_object_name = 'posts'
    ordering = ['-created_at']
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())
        return context


class PostDetailView(DetailView):
    model = Post
    queryset = None
    template_name = 'news/single.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


def add_news(request):
    if request.method == 'POST':
        form = NewsForm(request.POST)

        if form.is_valid():
            title = form.cleaned_data['title']
            text = form.cleaned_data['text']
            category = form.cleaned_data['category']
            if form.cleaned_data['type']:
                post_type = 'NW'
            else:
                post_type = 'AR'

            new_post = Post.objects.create(author=request.user, title=title, text=text, type=post_type)
    else:
        form = NewsForm()

    return render(request, 'news/add.html', {'form': form})
