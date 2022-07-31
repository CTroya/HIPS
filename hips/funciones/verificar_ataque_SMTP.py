import os
from .bloquear_usuario import bloquear_usuario
from .registrar_en_log import registrar_en_log
from django.core.mail import send_mail
from ..settings import *

def verificar_ataque_SMTP():
    comando = "sudo cat /var/log/messages | grep -i 'service=smtp' | grep -i 'auth failure'"
    resultado_comando = os.popen(comando).read().split("\n")
    resultado_comando.pop(-1)
    usuarios_contador = {}
    mensaje = ''
    for linea in resultado_comando:
        linea  = linea.split()
        usuario = linea[9].split("=")[1][:-1]
        # Si ya esta incializado un contador para el usuario, entonces procedemos, sino, inicializamos
        if usuario in usuarios_contador:
            usuarios_contador[usuario] +=  + 1 # si existe le sumamos uno al contador de failure en ese usuario
            # Si el contador de failure del usuario supera un limite, es una alarma, procedemos a cambiar la contra
            if usuarios_contador[usuario] == 50:
                #procedemos a bloquar al usuario
                bloquear_usuario(usuario)
                mensaje += 'El usuario: ' + usuario + ' tiene muchas entradas de falla de autenticacion de SMTP. Se le cambio la contra'
                registrar_en_log('prevencion','Ataque SMTP', '',
                'El usuario: ' + usuario + ' tiene muchas entradas de falla de autenticacion de SMTP. Se le cambio la contra')
                send_mail(
                    'Prevencion',
                    'El usuario: ' + usuario + ' tiene muchas entradas de falla de autenticacion de SMTP. Se le cambio la contra',
                    EMAIL_HOST,
                    [RECIPIENT_ADDRESS],
                    fail_silently=False)
                    
        else:
            usuarios_contador[usuario] = 1
