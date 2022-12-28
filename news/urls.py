from django.urls import path

from . import views


urlpatterns = [
    path('', views.PostListView.as_view(), name='news'),
    path('<int:pk>', views.PostDetailView.as_view(), name='post'),
    path('add/', views.add_news, name='add_news'),
]
