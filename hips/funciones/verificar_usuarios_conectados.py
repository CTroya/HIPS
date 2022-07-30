#Usuarios conectados en el host
import subprocess

def verificar_usuarios_conectados():
    resultado = subprocess.run("w",capture_output=True, text=True)
    return resultado.stdout 

#print(usuarios_conectados())