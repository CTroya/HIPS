from django.shortcuts import render, HttpResponse
from requests import request
from sqlalchemy import false, func
from sympy import fu
from urllib3 import HTTPResponse
# Las funciones 
from .funciones.verificar_binarios import verificar_binarios
from .funciones.verificar_usuarios_conectados import verificar_usuarios_conectados
from .funciones.verificar_sniffers import verificar_sniffers
from .funciones.verificar_logs import verificar_logs
from .funciones.verificar_cola_mails import verificar_cola_correo
from .funciones.verificar_consumo_recusos import verificar_consumo_recursos
from .funciones.verificar_tmp import verificar_tmp
from .funciones.verificar_ataque_DDOS_dns import verificar_ataque_DDOS_dns
from .funciones.verificar_cron import verificar_cron
from .funciones.verificar_intento_acceso import verificar_intento_acceso
from .funciones.configuracion_inicial import configuracion_inicial

def HTML(msg):
    html = '<p style = "color:#fbff00; font-family:Consolas; font-size: 12;" >%s</p>'%msg
    return html

def ayuda():
    mensaje = 'Esta es la lista de comandos disponibles:\n'
    for numero, funcion in funclist.items():
        mensaje += numero + ': ' + str(funcion.__name__) + '\n'
    return mensaje

funclist = {"1":verificar_binarios,
        "2":verificar_usuarios_conectados,
        "3":verificar_sniffers,
        "4":verificar_logs,
        "5":verificar_cola_correo,
        "6":verificar_consumo_recursos,
        "7":verificar_tmp,
        "8":verificar_ataque_DDOS_dns,
        "9":verificar_cron,
        "10":verificar_intento_acceso,
        "11":configuracion_inicial,
        "12": ayuda}

def home(request):
    return render(request, 'home.html')
from django.core.mail import send_mail
from .settings import *
    
def bruh(request):
    input = request.GET['msg']
    print(input)
    if input in funclist:
        send_mail('Subject here','Here is the message',EMAIL_HOST,[RECIPIENT_ADDRESS],fail_silently=false)
        resultado = funclist[input]()
        x = resultado.split('\n')
        for i in range(len(x)):
            x[i] = HTML(x[i])
        return HttpResponse(x)
    return HttpResponse(HTML(f"ERROR: \"{input}\" no es un comando. Digite: 12 para mas informacion de la lista de comandos disponibles"))
def home(request):
    return render(request, 'home.html')




