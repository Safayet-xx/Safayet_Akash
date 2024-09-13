from django.shortcuts import render, get_object_or_404

from .models import Blog

def allblogs(request):
    blogs = Blog.objects
    return render(request, 'blog/allblogs.html', {'blogs':blogs})

def detail (request, blog_id): 
    detailblog = get_object_or_404(Blog, pk = blog_id)
    return render (request, 'blog/detail.html',{'blog': detailblog})


def allblogs(request):
    # Fetch all blog objects
    blogs = Blog.objects.all()  # Correct: This returns a queryset, which is iterable
    return render(request, 'blog/allblogs.html', {'blogs': blogs})