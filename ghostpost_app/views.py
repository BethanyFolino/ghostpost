from django.shortcuts import render, HttpResponseRedirect, reverse
from ghostpost_app.models import Post
from ghostpost_app.forms import AddPostForm

# Create your views here.
def index_view(request):
    posts = Post.objects.all().order_by('-id')
    return render(request, 'index.html', {'posts': posts})


def upvote(request, post_id):
    post = Post.objects.get(id=post_id)
    post.upvotes += 1
    post.save()
    return HttpResponseRedirect(reverse('home'))

def downvote(request, post_id):
    post = Post.objects.get(id=post_id)
    post.downvotes += 1
    post.save()
    return HttpResponseRedirect(reverse('home'))

def add_post(request):
    if request.method == "POST":
        form = AddPostForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            post = Post.objects.create(
                boast_or_roast=data['boast_or_roast'],
                text = data['text']
            )
            return HttpResponseRedirect(reverse('home'))
    form = AddPostForm()
    return render(request, 'addpost.html', {'form': form})

def vote_score_view(request):
    posts = sorted(Post.objects.all(), key=lambda post:post.vote_score(), reverse=True)
    return render(request, 'index.html', {'posts': posts})

def boasts_view(request):
    posts = Post.objects.filter(boast_or_roast=True).order_by('-id')
    return render(request, 'index.html', {'posts': posts})

def roasts_view(request):
    posts = Post.objects.filter(boast_or_roast=False).order_by('-id')
    return render(request, 'index.html', {'posts': posts})