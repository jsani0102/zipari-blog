from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone

from .models import Post

def index(request):
	latest_posts = Post.objects.order_by('-created_at')

	# limit content to first 250 words
	for post in latest_posts:
		if len(post.content.split()) > 250:
			post.content = " ".join(post.content.split()[:250])

	args = { 'latest_posts': latest_posts }
	return render(request, 'zipariblog/index.html', args)

def create(request):
	if request.user.is_authenticated:
		return render(request, 'zipariblog/create.html')
	return HttpResponseRedirect(reverse('admin:index'))

def submit(request):
	new_post = Post()
	new_post.title = request.POST['title']
	new_post.content = request.POST['content']
	new_post.created_at = timezone.now()
	new_post.author = request.user.username
	new_post.save()

	return HttpResponseRedirect(reverse('zipariblog:index'))

def detail(request, post_id):
	post = get_object_or_404(Post, pk=post_id)
	return render(request, 'zipariblog/detail.html', {'post': post})

def edit(request, post_id):
	post = get_object_or_404(Post, pk=post_id)
	return render(request, 'zipariblog/edit.html', {'post': post})

def submit_edit(request, post_id):
	post = get_object_or_404(Post, pk=post_id)
	post.title = request.POST['title']
	post.content = request.POST['content']
	post.save()

	return HttpResponseRedirect(reverse('zipariblog:index'))
