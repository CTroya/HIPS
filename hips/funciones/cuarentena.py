# Pone en cuarentena lq le pasas
import subprocess
 
def cuarentena(ruta):
    ruta_cuarentena = '/cuarentena' 
    comando = subprocess.run(['mv', ruta, ruta_cuarentena])

#cuarentena('/a')