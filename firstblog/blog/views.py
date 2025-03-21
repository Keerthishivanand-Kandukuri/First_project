from django.shortcuts import redirect, render , get_object_or_404
from django.http import HttpResponse
from .models import Post

# Create your views here.
def home(request):

    posts= Post.objects.all()
    return render(request, 'blog/base.html', {'posts':posts}) 

def create_post(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')

        # Create and save post to the database
        Post.objects.create(title=title, content=content)
        
        # Redirect to homepage or any desired page
        return redirect('home')
    return render(request, 'blog/add_post.html')

def delete_post(request, post_id) :
    if request.method == 'POST':
        p=  get_object_or_404(Post, id=post_id)
        p.delete()
        return redirect('home')
    print( 'in post', request.method, get_object_or_404(Post, id=post_id) )
    posts= Post.objects.all()
    return render(request, 'blog/base.html', {'posts':posts}) 