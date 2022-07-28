from verificar_archivo import verificar_cambio_archivo
from pathlib import Path
import os.path

def verificar_binarios():
    pathlist = Path('/bin/')
    mensaje = ''
    se_cambio_alguno = False
    for path in pathlist.iterdir():
        if not os.path.isdir(path):
            if not verificar_cambio_archivo(path, '/backups/hashes/bin/' + path.name):
                se_cambio_alguno = True
                mensaje += 'El archivo: ' + str(path) + ' ha sido modificado\n'
    ruta_archivos = ['/etc/passwd', '/etc/group', '/etc/shadow']
    for ruta in ruta_archivos:
        if not verificar_cambio_archivo(ruta, '/backups/hashes/etc/' + ruta.split('/')[2]):
            se_cambio_alguno = True
            mensaje += 'El archivo: ' + ruta + ' ha sido modificado\n'
    if se_cambio_alguno:
        return 'Se detecto la modificacion de:\n' + mensaje
    else:
        return 'No se detectaron cambios en los binarios, ni en el /etc/passwd, /etc/group, /etc/shadow'
        
print(verificar_binarios())
