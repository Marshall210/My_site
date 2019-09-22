from django.shortcuts import render
from .models import Post
from django.utils import timezone
from datetime import datetime 


def post_list(request):
    posts = Post.objects.filter(published_date=datetime.now())
    context = {}
    context['posts'] = posts
    return render(request, 'blog/post_list.html', context)
# Create your views here.


'''
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

'''