from django_filters import FilterSet

from .models import Post


class PostFilter(FilterSet):
    class Meta:
        model = Post
        fields = ('title', 'text', 'type', 'author', 'created_at')