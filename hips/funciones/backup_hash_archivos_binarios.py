# A cada archivo del /bin/ y los /etc/passwd /etc/group /etc/shadow le hashea y guarda en un archivo

from pathlib import Path
import os.path
from hash_archivo import hashear_archivo

def backup_hash():
    pathlist = Path('/bin/')
    for path in pathlist.iterdir():
        if not os.path.isdir(path):
            f = open('/backup/hashes/bin/'+ path.name, 'w')
            f.write(hashear_archivo(path))
            f.close()
    archivos_etc = ['/etc/passwd', '/etc/group', '/etc/shadow']
    for archivo in archivos_etc:
        f = open('/backup/hashes/etc/'+ archivo.split('/')[2], 'w')
        f.write(hashear_archivo(archivo))
        f.close()

backup_hash()