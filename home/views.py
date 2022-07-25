from django.shortcuts import render, HttpResponse
import subprocess
# Create your views here.
def HTML(msg):
    html = '<p style = "color:black; font-family:Consolas; font-size: 12;" >%s</p>'%msg
    return html
def usuarios_conectados():

    listamsg = []

    try:
        #El retorno es de tipo bytes y no str
        cmd = subprocess.check_output("w", shell=True).decode('utf-8') 
        lista_usuarios = cmd.split('\n')
        #Eliminamos la cabezera del comando
        lista_usuarios.pop(0)
        #Eliminamos el ultimo valor de la lista
        lista_usuarios.pop(-1)
        msg = "Usuario------From:"
        listamsg.append(HTML(msg))
        for linea in lista_usuarios:
            usuario = linea.split()[0]
            desde   = linea.split()[3]
            listamsg.append(HTML(usuario + "-----" + desde))

    except Exception:
       msg = "No se pudo mostrar los usuarios conectados"
       listamsg.append(HTML(msg))
    return HTML(listamsg)
def home(request):
    return render(request, 'home.html')
def bruh(request):
    input = request.GET['msg']
    return HttpResponse(usuarios_conectados())