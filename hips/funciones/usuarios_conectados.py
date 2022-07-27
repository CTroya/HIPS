#Usuarios conectados en el host
import subprocess

def usuarios_conectados():
    resultado = subprocess.run("w",capture_output=True, text=True)
    print(resultado.stdout)
    return resultado #quizas nos sirva mas adelante, tenemos un string aca con la info

usuarios_conectados()