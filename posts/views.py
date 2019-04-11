from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostModelForm
from .models import Post


# Create your views here.
def create(request):
    # 'POST'요청이 오면,
    if request.method == 'POST':
        # 글을 작성하기
        form = PostModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('posts:list')
        
    # 'GET'요청이 오면,
    else:
        # post를 작성하는 form을 가져와 template에서 보여줌. 
        form = PostModelForm()
        context = {
            'form': form
        }
        return render(request, 'posts/create.html', context)


def list(request):
    posts = Post.objects.all()
    context = {
        'posts':posts
    }
    return render(request, 'posts/list.html', context)
    

def delete(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.delete()
    return redirect('posts:list')


def update(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = PostModelForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('posts:list')
    else:
        form = PostModelForm(instance=post)
        context = {
            'form':form
        }
        return render(request, 'posts/update.html', context)