# Archivo de URL que solo sirve para la ruta inicial de 
# BLOG
from django.urls import path
from .views import homeBlog,getPostByID

app_name = 'blog'

urlpatterns = [
    path('',homeBlog,name="homeBlog"),
    path('<int:post_id>',getPostByID,name="postByID"),
]