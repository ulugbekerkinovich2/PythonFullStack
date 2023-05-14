from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from .models import Blog


# Create your views here.


def bloglistviews(request):
    print(request, 'bu request da kelayapti')
    blogs = Blog.objects.all()
    users = User.objects.all()
    print(users)
    context = {
        'blogs': blogs,
        'users': users
    }

    return render(request, 'home.html', context=context)


def blogdeatilview(request, pk):
    print(request, pk)
    try:
        blog = Blog.objects.get(id=pk)
        context = {
            'blog': blog
        }
    except Blog.DoesNotExist:
        raise Http404('Notblog found')

    return render(request, "blog_detail.html", context=context)


def blog_detail_view(request, pk):
    blog = get_object_or_404(Blog, id=pk)
    context = {
        'blog': blog
    }
    return render(request, 'blog_detail.html', context=context)


class BlogListView(ListView):
    model = Blog
    template_name = 'home.html'
    context_object_name = 'blogs'


class BlogDetailView(DetailView):
    model = Blog
    template_name = 'home.html'
    context_object_name = 'blogs'
# default = object_list