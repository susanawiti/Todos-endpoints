from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from rest_framework import viewsets
from .serializers import PostSerializer

# Create your views here.

# def welcome(request):
#     return render(request, 'welcome_student.html')
def post(request):
    post = Post.objects.all()
    
    context={
        'post':post
    }
    return render(request,'list.html',context)
    
# viewsets define the view behavior 
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
