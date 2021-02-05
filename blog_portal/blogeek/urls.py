from django.urls import path
from .views import index, get_category, view_blogposts, add_posts

urlpatterns = [
    path('', index, name='home'),
    path('category/<int:category_id>/', get_category, name='category'),
    path('posts/<int:blogposts_id>/', view_blogposts, name='view_blogposts'),
    path('posts/add-posts/', add_posts, name='add-posts'),
]