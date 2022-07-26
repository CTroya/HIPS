from django.shortcuts import render, HttpResponse
import subprocess
# Create your views here.
def HTML(msg):
    html = '<p style = "color:#fbff00; font-family:Consolas; font-size: 12;" >%s</p>'%msg
    return html

def home(request):
    return render(request, 'home.html')
def bruh(request):
    input = request.GET['msg']
    return HttpResponse(usuarios_conectados())