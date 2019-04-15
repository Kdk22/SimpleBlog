from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from .models import Post
# Create your views here.
from django import forms


def index(request):
    all_posts = Post.objects.all()
    all_values = all_posts.values()
    return render(request, 'index.html', {'all_posts': all_posts})


def post(request):
    all_posts = Post.objects.all()

    return render(request, 'post/post.html', {'all_posts': all_posts})


def create(request):
    context ={
        'page': 'Create New Article'
    }
    return render(request, 'post/form.html', context)


def insert(request):

    if request.method.lower() == 'post':

        blog_title = request.POST['blog_title']
        blog_category = request.POST['blog_category']
        more_content = request.POST['more_info']
        post_date = request.POST['post_date']
        print(post_date)
        import ipdb
        ipdb.set_trace()
        pic = request.FILES['pic']

        b= Post(title=blog_title, categories=blog_category,content=more_content, icon=pic,post_date=post_date)
        b.save()

        return post(request)
    else:
        return HttpResponseNotFound
