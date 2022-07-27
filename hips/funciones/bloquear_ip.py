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
#bloquear_ip(ip)