# Le pasas la ruta de un archivo y otra ruta donde esta el hash anterior de ese archivo
# y te dice si se cambio o no el archivo
import hashlib
from hash_archivo import hashear_archivo

def verificar_archivo(ruta_archivo, ruta_hash_antiguo):
    with open(ruta_hash_antiguo) as f:
        contenido = f.read()
    contenido = contenido.strip('\n') #le saco el \n que me trae al leer el hash del file
    if contenido == hashear_archivo(ruta_archivo):
        return True
    else:
        return False

# Para probar tenes que tener el hash antiguo del archivo en el txt que le pasas
if verificar_archivo("/etc/passwd", "hash"): # de prueba
    print('los archivos son iguales')
else:
    print('los archivos no son iguales')
