from django.shortcuts import render

# Create your views hggggere.

def index(request):
    return render(request, 'base.html', context= {'text': 'Hello World'})
