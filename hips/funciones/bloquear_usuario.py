import subprocess
def bloquear_usuario(usuario):
    try:
        subprocess.call(['passwd',usuario,'-1'])
    except Exception:
        print("Ocurrio un problema al intentar bloquear un usuario")