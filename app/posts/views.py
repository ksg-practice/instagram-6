from django.shortcuts import render
from .models import Post

def post_list(request):
    # render의 context인수로 전달 (키:posts)
    #   context = {'posts': Post.objects.all
    posts = Post.objents.all()
    context = {
        'posts': posts,
    }
    return render(request, 'posts/post_list.html')