from django.urls import path, include
from . import views


app_name = 'posts'

urlpatterns = [
    path('', views.all_posts, name="all_posts"),
    path('create/', views.create_post, name="create_post"),
]
