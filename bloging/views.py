from django.shortcuts import render, get_object_or_404
from .models import Bloging


def allblogs(request):
    blogs = Bloging.objects
    return render(request, 'blog/allblogs.html', {'blogs': blogs})


def delail(request, blog_id):
    detailblog = get_object_or_404(Bloging, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog': detailblog})
