# Le pasas una ip como string y te bloquea la ip si es que no se bloqueo anteriormente

import subprocess
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

# Te bloquea la ip, hace uso de la funcion esta_bloqueada
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


def usuarios_conectados():
    resultado = subprocess.run("w",capture_output=True, text=True)
    print(resultado.stdout)
    return resultado #quizas nos sirva mas adelante, tenemos un string aca con la info

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
def verificar_ataque_DDOS_dns():
    ruta_ataque_DDOS_dns= 'ataques/Ataque_DNS_tcpdump.txt' # atender esto
    f = open(ruta_ataque_DDOS_dns,'r')
    ip_ataques = {} # diccionario con ip atacante y victima : cantidad de ataques
    for linea in f:
        ip_atacante = linea.split()[2]
        ip_victima = linea.split()[4][:-1] # para sacar el : que tiene la ip de la victima del final
        if ((ip_atacante, ip_victima)) in ip_ataques:
            ip_ataques[(ip_atacante, ip_victima)] += 1
            if ip_ataques[(ip_atacante, ip_victima)] >= 5: # hay que elegir un numero adecuado
                print('Se va a bloquear la ip: '+ ip_atacante + ' por sospecha de ataque a la ip: ' + ip_victima)
                # bloquear_ip
        else:
            ip_ataques[(ip_atacante, ip_victima)] = 1
        mensaje = str(ip_ataques)
    return mensaje
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
import subprocess

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
for linea in mensaje:
    # %cpu or %mem
    if bandera == True:
        bandera = False
        continue
    if float(linea.split()[2]) >= 20:
        print('El proceso: ' + linea.split()[1] + ' esta consumiendo\n' +
        linea.split()[2] + '% de cpu')

# Le pasas la ruta donde se guardan las tareas del cron y te imprime info sobre lq hay
# Normalmente esta aca: /var/spool/cron/crontabs
# SE NECESITAN PERMISOS PARA EJECUTAR ESTE SCRIPT

from pathlib import Path

def verificar_cron(ruta_del_cron):
    directory = ruta_del_cron
    pathlist = Path(directory)
    for path in pathlist.iterdir():
        print('El usuario ' + path.name + ' tiene tareas en el cron, las cuales son:')
        archivo = directory + '/' + path.name # completo la ruta del crontab de ese usuario
        f = open(archivo, "r") # ahora abro el archivo crontab del usuario
        for line in f:
            if line[0] != '#':
                print(line)     # muestro que es lq tiene como tarea programada
        f.close()

import subprocess

def verificar_intento_acceso():
    resultado = subprocess.run(['bash', './checkear_intento_acceso.sh']) # ejecuto el script en bash
    f = open("intento_acceso.txt","r") # abro el archivo que me crea el script hecho en bash
    ip_intentos = {} # un diccionario con el ip y los intentos de ingreso
    for line in f:
        ip = line.split()[10]
        if ip in ip_intentos: 
            ip_intentos[ip] += 1
            if ip_intentos[ip] == 10:
                mensaje = 'la ip '+ip+ ' se va a bloquear porque intento muchas veces'
                print(mensaje)
                bloquear_ip(ip)
        else:
            ip_intentos[ip] = 1
    #print(ip_intentos) te muestra cuantas veces intento cada ip
    return mensaje



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





    
