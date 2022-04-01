from django.shortcuts import render,get_object_or_404
from .models import Post
# Create your views here

#Vista que renderiza el archivo de "home" para el blog
def homeBlog(request):
    listPost = Post.objects.all()
    
    # Vaiables que pasaremos a la vista 
    variables = {
        'listPost':listPost
    }
    return render(request,'home_blog.html',variables)

# Segundo vista
def getPostByID(request,post_id):
    post=get_object_or_404(Post,pk=post_id)
    return render (request,'post_details.html',{
        'post':post
    })