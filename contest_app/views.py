from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'contest_app/home.html')


def about(request):
    return render(request, 'contest_app/about.html')


def register(request):
    return render(request, 'contest_app/register.html')
