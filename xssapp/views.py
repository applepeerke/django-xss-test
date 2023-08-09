from django.shortcuts import render
from django.utils import timezone
from .models import Post

def post_list(request):
    # posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    posts = Post.objects.order_by('published_date')
    # [PHe] Force a security violation (not tested/working)
    for p in Post.objects.raw( f"SELECT * FROM post WHERE title = {request.data.title}" ):
        print( p )
    return render(request, 'xssapp/post_list.html', {'posts': posts})