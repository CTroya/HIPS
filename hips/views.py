from re import X
from django.shortcuts import render, HttpResponse
import subprocess
# Create your views here.
def HTML(msg):
    html = '<p style = "color:black; font-family:Consolas; font-size: 12;" >%s</p>'%msg
    return html

import subprocess


def usuarios_conectados():
    resultado = subprocess.check_output("w",shell=True).decode('utf-8')
    #print(resultado.stdout.split('\n'))
    #for x in resultado.stdout.split('\n'):
    #    print(x)
    x = resultado.split('\n')
    x.pop(0)
    x.pop(-1)
    for i in range(len(x)):
        x[i] = HTML(x[i])
    
    print(x)
    return x #quizas nos sirva mas adelante, tenemos un string aca con la info

usuarios_conectados()

def home(request):
    return render(request, 'home.html')
def bruh(request):
    input = request.GET['msg']
    return HttpResponse(usuarios_conectados())
    
def home(request):
    return render(request, 'home.html')