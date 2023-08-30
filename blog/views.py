from django.views.generic.detail import DetailView
from django.shortcuts import render, get_object_or_404
from blog.models import Post
def post_show(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'post/detail.html', {'post': post})

# Create your views here.
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html', {'titulo': 'Últimas notícias, a gata da academia tá solteira'})

def ola(request):
    return render(request, 'home.html')
    #return HttpResponse('Olá django')
class PostDetailView(DetailView):
    model = Post
    template_name = 'post/detail.html'
    context_object_name = 'post'
