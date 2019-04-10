from django.shortcuts import render, redirect
from .forms import PostModelForm


# Create your views here.
def create(request):
    # 'POST'요청이 오면,
    if request.method == 'POST':
        # 글을 작성하기
        form = PostModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('posts:create')
        
    # 'GET'요청이 오면,
    else:
        # post를 작성하는 form을 가져와 template에서 보여줌. 
        form = PostModelForm()
        context = {
            'form': form
        }
        return render(request, 'posts/create.html', context)

