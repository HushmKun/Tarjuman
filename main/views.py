from django.shortcuts import render

# Create your views here.


def coming_soon(request):
    return render(request, "coming_soon.html")

def home(request):
    return render(request, 'main/index.html')
