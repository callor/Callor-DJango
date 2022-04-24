from django.shortcuts import render
from .models import Post


# Create your views here.

def index(req):
    return render(
        req,
        'views/index.html',
    )


def blog(req):
    postAll = Post.objects.all().order_by('-pk')
    return render(
        req,
        'views/blog_view.html',
        {
            'posts': postAll
        }
    )


def single_post_page(req,pk):
    findById = Post.objects.all().get(pk=pk)
    return render(
        req,
        'views/single_post_page.html',
        {
            'post': findById
        }
    )
