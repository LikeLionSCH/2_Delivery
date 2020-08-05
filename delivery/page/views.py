from django.shortcuts import render, redirect, get_object_or_404
from .models import Post

# Create your views here.
def order(request):
    return render(request, 'order.html')

def record(request):
    return render(request, 'record.html')

def change(request):
    return render(request, 'change.html')

def create(request):
    if request.method == 'POST':
        post = Post()
        post.name = request.POST['name']
        post.store = request.POST['store']
        post.address = request.POST['address']
        post.option = request.POST['option']

        post.save()

        return redirect('record')

    