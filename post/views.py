from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django import forms
from post.models import Posts
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.


class BlogForm(forms.Form):
    title = forms.CharField(label="Title", max_length=100)
    content = forms.CharField(widget=forms.Textarea)


def index(request):
    return redirect(reverse("post:posts"))


@login_required(login_url="auth:login")
def add_post(request):
    if request.method == "POST":
        form = BlogForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            user = User.objects.get(username=request.user.username)
            _ = Posts(title=title, content=content, user=user)
            _.save()

            return HttpResponseRedirect(reverse("post:posts"))
    else:

        return render(request, 'post/w_posts.html', {
            "form": BlogForm
        })


def posts(request):
    posts = Posts.objects.all()
    return render(request, 'post/posts.html', {
        "posts": posts
    })


def post_details(request, id):
    if id:
        post = Posts.objects.get(pk=id)

    return render(request, 'post/details.html', {
        "post": post
    })


def edit_post(request, id):
    post = Posts.objects.get(pk=id)

    if request.method == "POST":
        post.title = request.POST.get("title")
        post.content = request.POST.get("content")
        post.save()
        return redirect('post:details', id=post.id)

    return render(request, 'post/edit_post.html', {
        "post": post,
        "form": BlogForm
    })


def delete_post(request, id):
    post = Posts.objects.get(pk=id)

    post.delete()

    return HttpResponseRedirect(reverse("auth:profile"))
