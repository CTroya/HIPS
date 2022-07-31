from asyncio import subprocess
import os
import shutil
from pathlib import Path
from .hash_archivo import hashear_archivo

def configuracion_inicial():
    # Creo el directorio y los .log para las alarmas y los modulos de prevencion
    if not os.path.isdir('/var/log/hips'):
        os.mkdir('/var/log/hips')    
    if not os.path.isdir('/var/log/hips/alarmas.log'):  
        f = open('/var/log/hips/alarmas.log', 'w')
        f.close()
    if not os.path.isdir('/var/log/hips/prevencion.log'):
        f = open('/var/log/hips/prevencion.log', 'w')
        f.close()
    # Creo los directorios para los backups que usamos de comparacion
    if not os.path.isdir('/backup'):
        os.mkdir('/backup')
    if not os.path.isdir('/backup/hashes'):
        os.mkdir('/backup/hashes')
    if not os.path.isdir('/backup/hashes/bin'):
        os.mkdir('/backup/hashes/bin')
    if not os.path.isdir('/backup/hashes/etc'):
        os.mkdir('/backup/hashes/etc')
    # Creo el directorio de cuarentena
    if not os.path.isdir('/cuarentena'):
        os.mkdir('/cuarentena')
    # Creo el directorio de ejemplos de ataques
    print(os.getcwd() + '/Ataque_DNS_tcpdump.txt')
    if not os.path.isdir('/ataques'):
        os.mkdir('/ataques')
    shutil.copy(os.getcwd() + '/Ataque_DNS_tcpdump.txt', '/ataques/Ataque_DNS_tcpdump.txt')
    # Creo los hashes de los binarios y del etc, shadow y group
    pathlist = Path('/bin/')
    for path in pathlist.iterdir():
        if not os.path.isdir(path):
            hash = hashear_archivo(str(path))
            f = open('/backup/hashes/bin/' + path.name, 'w')
            f.write(hash)
    ruta_archivos = ['/etc/passwd', '/etc/group', '/etc/shadow']
    for ruta in ruta_archivos:
        hash = hashear_archivo(ruta)
        f = open('/backup/hashes/etc/' + ruta.split('/')[2], 'w')
        f.write(hash)
    return 'Se realizo la configuracion inicial, ya se puede utilizar el HIPS.'

#configuracion_inicial()
