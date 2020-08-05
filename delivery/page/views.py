from django.shortcuts import render, redirect, get_object_or_404
from .models import Post

# Create your views here.
def order(request):
    return render(request, 'order.html')

def record(request):
    return render(request, 'record.html')

def change(request):
    return render(request, 'change.html')

def create(request): # 주문 생성
    if request.method == 'POST':
        post = Post()
        post.name = request.POST['name']
        post.store = request.POST['store']
        post.address = request.POST['address']
        post.option = request.POST['option']

        post.save()

        return redirect('record')

def update(request, post_id): # 주문 업데이트
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        post = Post()
        post.name = request.POST['name']
        post.store = request.POST['store']
        post.address = request.POST['address']
        post.option = request.POST['option']

        post.save()

        return redirect('record')


def delete(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.delete()

    return redirect('order')
    