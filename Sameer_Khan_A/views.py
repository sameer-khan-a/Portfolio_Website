from django.shortcuts import render

def index(request):
    return render(request, 'sameer_khan_a/templates/index.html')
