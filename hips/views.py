from django.shortcuts import render, HttpResponse
import subprocess
from requests import request
from sqlalchemy import false

from sympy import fu
# Le pasas una ip como string y te bloquea la ip si es que no se bloqueo anteriormente

import subprocess

from urllib3 import HTTPResponse
#Checkea si la ip esta en los registros de iptables, retorna un booleano
def esta_bloqueada(ip):
    comando = subprocess.run(['iptables','-L','INPUT','-v','-n'], capture_output=True, text=True)
    linea = 0
    bloqueado = False
    for x in comando.stdout.split('\n')[:-1]: 
        if linea >= 2:
            ip_iptable = x.split()[7] # saco la ip de la iptable
            #print('ip_iptable:' + ip_iptable)
            #print('ip', ip)
            if ip == ip_iptable:
                bloqueado = True
                break
        linea += 1
    return bloqueado

# Te bloquea la ip, hace uso de la funcion esta_bloqueadadef bruh(request):
def bloquear_ip(ip):
    # primero veo si la ip ya esta bloqueada
    if esta_bloqueada(ip):
        print('la ip: ' + ip + ' ya esta bloqueada')
    else:
        # Bloqueo la conexion de la ip para todo los servicios
            print('se bloqueo la ip: ' + ip)
            resultado = subprocess.run(['iptables', '-A' ,'INPUT', '-s',  ip, '-j','DROP'])
    
#prueba
#ip = '80.80.80.80'
#bloquear_ip(ip)#prueba
#ip = '80.80.80.80'
#bloquear_ip(ip)

# Le das el pid de un proceso y te lo mata
def matar_proceso(pid):
    subprocess.run(['kill', '-9', str(pid)], capture_output=True, text=True)
    #print('Se mato al proceso: '+ str(pid))

# Le pasas la ruta de un archivo y te retorna el hash en hexadecimal como un string
import hashlib

def hashear_archivo(ruta_arvhivo):
    file = ruta_arvhivo
    BLOCK_SIZE = 65536 # The size of each read from the file
    file_hash = hashlib.md5() # Create the hash object, can use something other than `.sha256()` if you wish
    with open(file, 'rb') as f: # Open the file to read it's bytes
        fb = f.read(BLOCK_SIZE) # Read from the file. Take in the amount declared above
        while len(fb) > 0: # While there is still data being read from the file
            file_hash.update(fb) # Update the hash
            fb = f.read(BLOCK_SIZE) # Read the next block from the file
    return file_hash.hexdigest()
#hasheado = hashear_archivo("/etc/passwd")
#print(hasheado)


from pathlib import Path
import os.path
# Te crea un txt en /home/alain/backups/hashes/(bin o etc) el hash para comparar
# A ESTE HAY QUE LLAMARLE SI O SI ANTES PQ TE CREAR EL BACKUP DE LOS HASHES
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

# Le pasas un archivo y la ruta donde esta el antiguo hash y compara el hash nuevo con el viejo
def verificar_cambio_archivo(ruta_archivo, ruta_hash_antiguo):
    with open(ruta_hash_antiguo) as f:
        hash_antiguo = f.read()
    hash_antiguo = hash_antiguo.strip('\n') #le saco el \n que me trae al leer el hash del file
    if hash_antiguo == hashear_archivo(ruta_archivo):
        return True # si el archivo no se cambio
    else:
        return False # si el archivo se cambio

# Te mira todo el /bin y los /etc/passwd, /etc/shadow y /etc/group para saber si se cambio algo
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


def verificar_ataque_DDOS_dns():
    ruta_ataque_DDOS_dns= 'ataques/Ataque_DNS_tcpdump.txt' # atender esto 
    f = open(ruta_ataque_DDOS_dns,'r')
    ip_ataques = {} # diccionario con ip atacante y victima : cantidad de ataques
    mensaje = ''
    se_bloqueo_alguna_ip = False
    for linea in f:
        ip_atacante = linea.split()[2]
        ip_victima = linea.split()[4][:-1] # para sacar el : que tiene la ip de la victima del final
        if ((ip_atacante, ip_victima)) in ip_ataques:
            ip_ataques[(ip_atacante, ip_victima)] += 1
            if ip_ataques[(ip_atacante, ip_victima)] >= 5: # hay que elegir un numero adecuado
                se_bloqueo_alguna_ip = True
                #print('Se va a bloquear la ip: '+ ip_atacante + ' por sospecha de ataque a la ip: ' + ip_victima)
                mensaje += 'Se bloqueo la ip: ' + ip_atacante + ' por sospecha de ataque a la ip: ' + ip_victima + ' \n'
                bloquear_ip(ip_atacante)
                #avisar al admin
        else:
            ip_ataques[(ip_atacante, ip_victima)] = 1
        #registro = str(ip_ataques) es el diccionario en un string, quizas sea util
    if se_bloqueo_alguna_ip:
        return mensaje
    else:
        return 'No se detecto comportamiento parecido a un ataque DDOS'


import os

def check_cola_correo():
    lista_msg = []
    cmd = "mailq"
    resultado_cmd = os.popen(cmd).read()
    
    if "queue is empty" in resultado_cmd:
        print("La cola esta vacia")

    else:
        resultado = resultado_cmd.splitlines()

    mail_queue = resultado_cmd.splitlines()
    
    if len(mail_queue) > 5: # elegir una cantidad adecuada
        print("Se encontraron muchos mails en la cola, se aviso al administrador")

    else:
        print('no se encontraron muchos mails en la cola')

    return lista_msg

# Mira el consumo de recursos en el host.
def verificar_consumo_recursos():
    # CONSUMO CPU
    comando_ps = subprocess.run(['ps', 'aux', '--sort', '-pcpu'], 
    check=True, capture_output=True, text=True)
    #print(comando_ps.stdout)
    comando_awk = subprocess.run(['awk', '{print $1, $2, $3, $4, $5, $10, $11}'], 
    input=comando_ps.stdout, capture_output=True, text=True)
    #print(comando_awk.stdout)
    comando_head = subprocess.run(['head', '-10'],
    input = comando_awk.stdout, capture_output=True, text=True)
    mensaje = comando_head.stdout.split('\n')
    del mensaje[-1] # le saco el '' que tiene la lista al final
    bandera = True
    mensaje_retorno = ''
    for linea in mensaje:
        # %cpu or %mem
        if bandera == True:
            bandera = False
            continue
        if float(linea.split()[2]) >= 90:
            #print('El proceso: ' + linea.split()[1] + ' esta consumiendo: ' +
            #linea.split()[2] + '% de cpu')
            mensaje_retorno += 'El proceso: ' + linea.split()[1] + ' esta consumiendo: ' 
            + linea.split()[2] + '% de cpu, se procede a matar al proceso \n'
            matar_proceso(linea.split()[1])
            # avisar al admin
    bandera = True
    # CONSUMO MEMORIA
    comando_ps_mem = subprocess.run(['ps', 'aux', '--sort', '-%mem'],
    check=True, capture_output=True, text=True)
    comando_awk_mem = subprocess.run(['awk', '{print $1, $2, $3, $4, $5, $10, $11}'], 
    input=comando_ps_mem.stdout, capture_output=True, text=True)
    comando_head_mem = subprocess.run(['head', '-10'],
    input = comando_awk_mem.stdout, capture_output=True, text=True)
    mensaje_mem = comando_head_mem.stdout.split('\n')
    del mensaje[-1] # le saco el '' que tiene la lista al final
    for linea in mensaje:
        # %cpu or %mem
        if bandera == True:
            bandera = False
            continue
        if float(linea.split()[3]) >= 90: 
            #print('El proceso: ' + linea.split()[1] + ' esta consumiendo: ' +
            #linea.split()[3] + '% de memoria ram')
            mensaje_retorno += 'El proceso: ' + linea.split()[1] + ' esta consumiendo: ' 
            + linea.split()[2] + '% de memoria ram, se procede a matar al proceso \n'
            matar_proceso(linea.split()[1])
            # avisar al admin
    if mensaje_retorno == '':
        return 'No se detecto consumos significativos de los recursos'
    else:
        return mensaje_retorno

# SE NECESITAN PERMISOS PARA EJECUTAR ESTE SCRIPT

from pathlib import Path

def verificar_cron():
    directory = '/var/spool/cron/crontabs'
    pathlist = Path(directory)
    mensaje = ''
    for path in pathlist.iterdir():
        #print('El usuario ' + path.name + ' tiene tareas en el cron, las cuales son:')
        mensaje += 'El usuario ' + path.name + ' tiene tareas en el cron, las cuales son: \n' 
        archivo = directory + '/' + path.name # completo la ruta del crontab de ese usuario
        f = open(archivo, "r") # ahora abro el archivo crontab del usuario
        for line in f:
            if line[0] != '#':
                mensaje += line + '\n'
                #print(line)     # muestro que es lq tiene como tarea programada
        f.close()
    return mensaje


def verificar_intento_acceso():
    resultado = subprocess.run(['bash', './checkear_intento_acceso.sh']) # ejecuto el script en bash
    f = open("/intento_acceso.txt","r") # abro el archivo que me crea el script hecho en bash
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
                # avisar al admin
                # dejar registro de la alarma en el log
                # print(mensaje)
                bloquear_ip(ip)
        else:
            ip_intentos[ip] = 1
    #print(ip_intentos) te muestra cuantas veces intento cada ip
    if se_bloqueo_alguna_ip:
        return mensaje
    else:
        return 'No se detectaron intentos fallidos de acceso al sistema'


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
    if mensaje == "":
        mensaje = 'No se encontraron scripts en el directorio /tmp'
    return mensaje
# Create your views here.
def HTML(msg):
    html = '<p style = "color:#fbff00; font-family:Consolas; font-size: 12;" >%s</p>'%msg
    return html

import subprocess


def usuarios_conectados():
    resultado = subprocess.check_output("w",shell=True).decode('utf-8')
    #print(resultado.stdout.split('\n'))
    #for x in resultado.stdout.split('\n'):
    #    print(x)
    #print(x)
    return resultado #quizas nos sirva mas adelante, tenemos un string aca con la info


def verificar_cola_correo():
    cmd = "mailq"
    resultado_cmd = os.popen(cmd).read()
    mensaje = ''
    if "queue is empty" in resultado_cmd:
        #print("La cola esta vacia")
        mensaje += "La cola esta vacia\n"
    else:
        resultado = resultado_cmd.splitlines()
    mail_queue = resultado_cmd.splitlines()
    if len(mail_queue) > 5: # elegir una cantidad adecuada
        #print("Se encontraron muchos mails en la cola, se aviso al administrador")
        mensaje += "Se encontraron muchos mails (" + str(len(mail_queue)) + ") en la cola, se aviso al administrador\n"
    else:
        #print('no se encontraron muchos mails en la cola')
        mensaje += "No se encontraron muchos mails en la cola\n"
    return mensaje

def configuracion_inicial():
    return 'Se ejecutaron varios scripts iniciales, el sistema esta listo'

def ayuda():
    mensaje = 'Los comandos son los siguientes:\n'
    for llave, valor in funclist.items():
        mensaje += str(llave) +': '+ str(valor.__name__) + '\n'
    return mensaje

def verificar_sniffers():
    sniffers = ['tcpdump','ethereal','wireshark','Ngrep','Snort'] # lista negra de sniffers
    librerias = ['libpcat'] # posibles librerias que los snifffers usan regularmente
    mensaje = ''
    detectados = []
    # Veo si algun sniffer esta ejecutandose
    for sniffer in sniffers:
        comando = f"ps -aux | grep {sniffer} | grep -v grep | awk '{{print $1, $2, $NF}}'"
        resultado_comando = os.popen(comando).read().split('\n')
        resultado_comando.pop(-1)
        for resultado in resultado_comando:
            #resultado.split()[0]  usuario
            #resultado.split()[1]  pid
            #resultado.split()[2]  programa
            # avisar al admin
            # poner en el registro de alarmas
            # matar al proceso
            matar_proceso(resultado.split()[1])
            if not resultado.split()[2] in detectados:
                detectados.append(resultado.split()[2])
                mensaje += 'Se encontro el sniffer: ' + resultado.split()[2] + ' ejecutandose. Se envio el sniffer a cuarentena\n'            
            # poner en cuarentena el sniffer
    # Veo si existe alguna herramienta
    if mensaje == '':
        return 'No se detectaron sniffers en el sistema'
    else:
        return mensaje

def verificar_logs():
    return 'falta hacer xd'

funclist = {"1":verificar_binarios,
        "2":usuarios_conectados,
        "3":verificar_sniffers,
        "4":verificar_logs,
        "5":verificar_cola_correo,
        "6":verificar_consumo_recursos,
        "7":verificar_tmp,
        "8":verificar_ataque_DDOS_dns,
        "9":verificar_cron,
        "10":verificar_intento_acceso,
        "11":configuracion_inicial,
        "12": ayuda}

def home(request):
    return render(request, 'home.html')
from django.core.mail import send_mail
from hips.settings import *
    
def bruh(request):
    input = request.GET['msg']
    print(input)
    if input in funclist:
        send_mail('Subject here','Here is the message',EMAIL_HOST,[RECIPIENT_ADDRESS],fail_silently=false)
        #print(input)
        resultado = funclist[input]()
        #print(resultado)
        x = resultado.split('\n')
        #x.pop(0)
        #x.pop(-1)
        for i in range(len(x)):
            x[i] = HTML(x[i])
        return HttpResponse(x)
    return HttpResponse(HTML(f"ERROR: \"{input}\" is not a command"))
def home(request):
    return render(request, 'home.html')




