from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods

from . import models

def all_posts(request):

    context = {
    'posts': models.Post.objects.all()
    }
    return render(request, 'posts/all_posts.html', context)


@require_http_methods(["GET", "POST"])
def create_post(request):
    if request.method == 'POST':
        title = request.POST.get('title', 'Some Title')
        description = request.POST.get('description', 'Some description')
        post = models.Post(title=title, description=description)
        post.save()
        return redirect('posts:all_posts')

    context = {

    }
    return render(request, 'posts/create.html', context)
