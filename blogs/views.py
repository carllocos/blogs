from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from django.views.decorators.http import require_http_methods

def home(request):
    """
    The home page of blogs.
    """
    user=request.user

    if user.is_authenticated:
        #Do somenthing if use user is logged in
        pass
    else:
        #Do somenthing else
        pass

    context = {
    'title': 'Home'
    }
    return render(request, "blogs/home.html", context=context)



def other_request(request):
    link= reverse('some_request')
    return HttpResponse(f"This URL is {link}")
