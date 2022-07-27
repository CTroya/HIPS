# Mira el directorio /tmp en busca de posibles scripts
import subprocess
from unittest import result

comando = "find /tmp/ -type f" #busco solo los archivos

def verificar_tmp():
    resultado = subprocess.run(['find','/tmp/','-type', 'f'], 
    capture_output=True, text=True)
    archivos = resultado.stdout.split()
    mensaje = ''
    for archivo in archivos:
        # si el archivo tiene como nombre alguna de estas extensiones
        #entonces se considera peligroso.
        if any(substring in archivo for substring in [ 
            ".cpp", ".py", ".c", ".exe", ".sh", ".ruby", ".php"
            ]):
            #print('Se encontro un script llamado: '+ archivo + ' se tomaran acciones')
            mensaje += 'Se encontro un script llamado: '+ archivo + ' se tomaran acciones\n'
            # mover a cuarentena o eliminar (falta decidir que hacer)
        else:
            f = open(archivo,'r')
            for linea in f:
                if '#!' in linea:
                    #print('Se encontro un script llamado: '+ f.name + ' se tomaran acciones')
                    mensaje += 'Se encontro un script llamado: '+ archivo + ' se tomaran acciones\n'
                    # eliminar o mover a cuarentena (falta decidir que hacer)
                    break
            f.close()
    if mensaje == '':
        mensaje = 'No se encontraron scripts en el directorio /tmp'
    return mensaje

print(verificar_tmp())

