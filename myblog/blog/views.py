from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm, CommentForm
from .models import Post, Comment
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login


def post_list(request):
    posts = Post.objects.all()
    comment_forms = {post.pk: CommentForm() for post in posts}
    return render(request, 'blog/post_list.html', {'posts': posts, 'comment_forms': comment_forms})

def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)

            post.save()
            return redirect('post_list')  # 새로운 게시물이 작성된 후 게시물 목록 페이지로 이동
    else:
        form = PostForm()
    return render(request, 'blog/post_new.html', {'form': form})


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog:post_list')  # 가입 성공 시 메인 페이지로 이동
    else:
        form = UserCreationForm()

    return render(request, 'signup.html', {'form': form})

def custom_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('blog:post_list')  # 'post_list' 메인 페이지로 이동
    else:
        form = AuthenticationForm()

    return render(request, 'login/login.html', {'form': form})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = Comment.objects.filter(post=post)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            return redirect('post_detail', pk=pk)
    else:
        form = CommentForm()

    return render(request, 'post_detail.html', {'post': post, 'comments': comments, 'form': form})
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.post = post
            new_comment.save()

            # 댓글을 추가한 후 해당 게시물의 댓글 목록
            comments = Comment.objects.filter(post=post)
            return redirect('blog:post_detail', pk=pk)
    else:
        form = CommentForm()

    return render(request, 'comment.html', {'post': post, 'form': form})

def my_blog_view(request):
    posts = Post.objects.all()
    return render(request, 'your_template_name.html', {'posts': posts})
