from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
# Create your views here.
def index(request):
    #return HttpResponse(" I am Mr.Nopphadol Sumleeroung ")
    posts = Post.objects.all()
    return render(request, 'index.htm', {'test':posts})
