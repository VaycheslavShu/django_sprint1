from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.index),
    path('<slug:category_slug/', views.category_posts, name='category'),
    path('<int:id>/', views.post_detail, name='detail'), ]