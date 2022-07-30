# Mira el directorio /tmp en busca de posibles scripts
import subprocess
#from unittest import result
from .registrar_en_log import registrar_en_log
from .cuarentena import cuarentena

def verificar_tmp():
    #busco solo los archivos
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
            cuarentena(archivo)
            mensaje += 'Se encontro un script llamado: '+ archivo + ' se lo pondra en cuarentena\n'
            registrar_en_log('prevencion','script en /tmp','',
            'Se encontro un script llamado: '+ archivo + ' en el directorio /tmp. Se puso el script en cuarentena')
            # avisar al admin
        else:
            f = open(archivo,'r')
            for linea in f:
                if '#!' in linea:
                    cuarentena(archivo)
                    mensaje += 'Se encontro un script llamado: '+ archivo + ' se lo pondra en cuarentena\n'
                    registrar_en_log('prevencion','script en /tmp','',
                    'Se encontro un script llamado: '+ archivo + ' en el directorio /tmp. Se puso el script en cuarentena')
                    # avisar al admin
                    break
            f.close()
    if mensaje == '':
        return 'No se encontraron scripts en el directorio /tmp'
    else:
        return mensaje

print(verificar_tmp())

