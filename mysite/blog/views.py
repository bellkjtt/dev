from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Post
from .models import User
from .models import Tag
from .forms import PostForm, PostModelForm
# Create your views here.


def test1(request):
    return HttpResponse("blog/test1 응답!")


def test2(request, id):
    return HttpResponse(id)


def test3(request, year, mon, day):
    return HttpResponse(f'{year}년 {mon}월 {day} 일')


def list(request):
    post_list = Post.objects.all()
    search_key = request.GET.get('keyword')
    if search_key:  # 데이터가 있다면
        # 서치 키워드가 타이틀에 포함되어 있는 녀석들만 뽑는다.
        post_list = Post.objects.filter(title__contains=search_key)
    return render(request, 'blog/list.html', {'post_all': post_list})


def detail(request, id):
    post = get_object_or_404(Post, id=id)
    comment_list = post.comments.all()
    tag_list = post.tag.all()
    return render(request, 'blog/detail.html', {'post': post, 'comment_all': comment_list,
                                                'tag_list': tag_list})


def test4(request):
    var = """
    이것은 테스트 입니다.
    """
    return render(request, 'blog/test4.html', {'score': 95, 'var': var})


def profile(request):
    user = User.objects.get(id=1)
    return render(request, 'blog/profile.html', {'user': user})


def tag_list(request, id):
    tag = Tag.objects.get(id=id)
    post_list = tag.post_set.all()
    return render(request, 'blog/list.html', {'post_all': post_list})


def test7(request):
    print('요청방식 : ', request.method)
    print('get방식으로 전달된 질의 문자열:', request.GET)
    print('POST 방식으로 전달된 질의 문자열:', request.POST)
    print('업로드 파일: ', request.FILES)
    return render(request, 'blog/form_test.html')


def post_create(request):
    if request.method == 'POST':
        form = PostModelForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            post = form.save(commit=False)
            post.ip = request.META['REMOTE_ADDR']
            post.save()
        return redirect(post)
    else:
        form = PostForm()
        return render(request, 'blog/post_form.html', {'form': form})


def post_update(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == 'POST':
        form = PostModelForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('blog:list')
    else:
        form = PostModelForm(instance=post)
        return render(request, 'blog/post_update.html', {'form': form})


def post_delete(request, id):
    post = Post.objects.get(id=id)
    if request.method == 'POST':
        post.delete()
        return redirect('blog:list')
    else:
        return render(request, 'blog/post_delete.html', {'post': post})
