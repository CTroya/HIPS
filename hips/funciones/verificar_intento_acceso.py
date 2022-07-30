
import subprocess
from .bloquear_ip import bloquear_ip
from .registrar_en_log import registrar_en_log

def verificar_intento_acceso():
    resultado = subprocess.run(['bash', './checkear_intento_acceso.sh']) # ejecuto el script en bash
    f = open("/var/log/hips/intento_acceso.log","r") # abro el archivo que me crea el script hecho en bash
    ip_intentos = {} # un diccionario con el ip y los intentos de ingreso
    mensaje = ''
    se_bloqueo_alguna_ip = False
    for line in f:
        ip = line.split()[10]
        if ip in ip_intentos: 
            ip_intentos[ip] += 1
            if ip_intentos[ip] == 10:
                se_bloqueo_alguna_ip = True
                mensaje += 'La ip ' + ip + ' se va a bloquear porque intento fallidamente acceder al sistema muchas veces\n'
                bloquear_ip(ip)
                registrar_en_log('prevencion','intento acceso',ip, 
                'Se detecto muchos intentos de acceso fallidos. Se bloqueo la ip')
                # avisar al admin
        else:
            ip_intentos[ip] = 1
    #print(ip_intentos) te muestra cuantas veces intento cada ip
    if se_bloqueo_alguna_ip:
        return mensaje
    else:
        return 'No se detectaron intentos fallidos de acceso al sistema'

#print(verificar_intento_acceso())



    