from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def reverse(request):
    user_text = request.GET['username']
    reverse = user_text[::-1]
    return render (request, 'reverse.html', {'word': reverse})

def about(request):
    return HttpResponse('project_django2')


