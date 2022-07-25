from django.shortcuts import render, HttpResponse
import subprocess
# Create your views here.
def HTML(msg):
    html = '<p style = "color:black; font-family:Consolas; font-size: 12;" >%s</p>'%msg
    return html

def usuarios_conectados():
    resultado = subprocess.run("w",capture_output=True, text=True)
    print(resultado.stdout)
    return HTML(resultado) #quizas nos sirva mas adelante, tenemos un string aca con la info

usuarios_conectados()
def home(request):
    return render(request, 'home.html')
def bruh(request):
    input = request.GET['msg']
    return HttpResponse(usuarios_conectados())
    
def home(request):
    return render(request, 'home.html')