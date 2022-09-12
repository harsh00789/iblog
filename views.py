from django.shortcuts import render
from django.http import HttpResponse
from .models import post , category

# Create your views here.
def home(request):
    #load all post from database
    posts = post.objects.all()[:11]

    categories =  category.objects.all()[:11]
    #print(posts)
    data = {
        'posts': posts,
         'cate' : categories

    }
    return render(request,"home.html",data)