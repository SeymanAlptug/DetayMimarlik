from django.shortcuts import render
from .models import Post , Dosya
from django.shortcuts import render, get_object_or_404

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts':posts})

def dosya_list(request):
    dosya_listesi = Dosya.objects.all()
    return render(request, 'blog/proje.html',{'dosya_listesi': dosya_listesi})



    