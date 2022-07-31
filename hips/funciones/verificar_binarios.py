from .verificar_cambio_archivo import verificar_cambio_archivo
from pathlib import Path
import os
from .registrar_en_log import registrar_en_log
from django.core.mail import send_mail
from ..settings import *

def verificar_binarios():
    pathlist = Path('/bin/')
    mensaje = ''
    se_cambio_alguno = False
    for path in pathlist.iterdir():
        if not os.path.isdir(path):
            if verificar_cambio_archivo(path, '/backup/hashes/bin/' + path.name):
                se_cambio_alguno = True
                mensaje += 'El archivo: ' + str(path) + ' ha sido modificado\n'
                registrar_en_log('alarmas','cambio en /bin','',
                'El archivo: ' + str(path) + ' ha sido modificado')
                send_mail(
                    'Alarma',
                    'El archivo: ' + str(path) + ' ha sido modificado.',
                    EMAIL_HOST,
                    [RECIPIENT_ADDRESS],
                    fail_silently=False)
    ruta_archivos = ['/etc/passwd', '/etc/group', '/etc/shadow']
    for ruta in ruta_archivos:
        if verificar_cambio_archivo(ruta, '/backup/hashes/etc/' + ruta.split('/')[2]):
            se_cambio_alguno = True
            mensaje += 'El archivo: ' + ruta + ' ha sido modificado\n'
            registrar_en_log('alarmas','cambio en /etc','',
            'El archivo: ' + ruta + ' ha sido modificado')
            send_mail(
                    'Alarma',
                    'El archivo: ' + ruta + ' ha sido modificado.',
                    EMAIL_HOST,
                    [RECIPIENT_ADDRESS],
                    fail_silently=False)
    if se_cambio_alguno:
        return 'Se detecto la modificacion de:\n' + mensaje
    else:
        return 'No se detectaron cambios en los binarios, ni en el /etc/passwd, /etc/group, /etc/shadow'
        
#print(verificar_binarios())
