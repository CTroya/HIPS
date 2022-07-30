# Le pasas la ruta de un archivo y otra ruta donde esta el hash anterior de ese archivo
# y te dice si se cambio o no el archivo
from .hash_archivo import hashear_archivo

def verificar_cambio_archivo(ruta_archivo, ruta_hash_antiguo):
    with open(ruta_hash_antiguo) as f:
        hash_antiguo = f.read()
    hash_antiguo = hash_antiguo.strip('\n') #le saco el \n que me trae al leer el hash del file
    if hash_antiguo == hashear_archivo(ruta_archivo):
        return True # si el archivo no se cambio
    else:
        return False # si el archivo se cambio
'''
# Para probar tenes que tene el hash antiguo del archivo en el txt que le pasas
if verificar_cambio_archivo("/etc/passwd", "hash"): # de prueba
    print('los archivos son iguales')
else:
    print('los archivos no son iguales')
'''
