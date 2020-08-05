from django.shortcuts import render

# Create your views here.
def order(request):
    return render(request, 'order.html')

def record(request):
    return render(request, 'record.html')

def change(request):
    return render(request, 'change.html')