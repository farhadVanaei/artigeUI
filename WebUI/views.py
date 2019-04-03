from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.template import loader

from WebUI.models import Post


def index(request):
    """View function for home page of site."""
    # Render the HTML template index.html with the data in the context variable
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'index.html', context)