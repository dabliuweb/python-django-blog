from django.urls import path
from . import views

urlpatterns = [
    path('blog', views.blogIndex, name="blog"),
    path('post/<int:id>', views.post, name="post"),
]