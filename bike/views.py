from django.shortcuts import render

# Create your views here.
from .models import Post

def home(request):
    return render(request,'home.html')
def Add(request):
    if request.method == 'GET':
        if request.GET.get('nn', None) and request.GET.get('bb', None):
            post = Post()
            post.Name = request.GET.get('nn', None)
            post.Bike= request.GET.get('bb', None)
            post.save()
        return render(request, 'Add.html')
    else:
        return render(request, 'Add.html')
def see(request):
    data=Post.objects.all()
    return render(request,'see.html',{'data':data})