from django.shortcuts import render

def index(request):
    return render(request, 'chat_api/index.html')