from django.shortcuts import render, redirect
from .models import Post

# Create your views here.

def post_list(request):
    posts = Post.objects.all()
    print(posts[0].id)
    return render(request, 'blog/post_list.html', {'posts':posts})

def post_like(request):
    print('LIKE')
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        post = Post.objects.get(id = post_id)
        post.likes +=1
        post.save()
    return redirect('post_list')