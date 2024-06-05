from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    path('<slug:category_slug/', views.category_posts, 
         name='category_posts category'),
    path('<int:id>/', views.post_detail, name='detail'), ]
