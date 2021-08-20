from django.shortcuts import render
from ghostpost_app.models import Post

# Create your views here.
def index_view(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts})