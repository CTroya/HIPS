#Usuarios conectados en el host
import subprocess
from django.core.mail import send_mail
from ..settings import *

def verificar_usuarios_conectados():
    resultado = subprocess.run("w",capture_output=True, text=True)
    return resultado.stdout 

#print(usuarios_conectados())