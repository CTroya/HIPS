from .bloquear_ip import bloquear_ip
from .registrar_en_log import registrar_en_log

def verificar_ataque_DDOS_dns():
    ruta_ataque_DDOS_dns = '/ataques/Ataque_DNS_tcpdump.txt' # atender esto 
    f = open(ruta_ataque_DDOS_dns,'r')
    ip_ataques = {} # diccionario con ip atacante y victima : cantidad de ataques
    mensaje = ''
    se_bloqueo_alguna_ip = False
    ips_bloqueadas = []
    for linea in f:
        ip_atacante = linea.split()[2]
        ip_victima = linea.split()[4][:-1] # para sacar el : que tiene la ip de la victima del final
        if ((ip_atacante, ip_victima)) in ip_ataques:
            ip_ataques[(ip_atacante, ip_victima)] += 1
            if ip_ataques[(ip_atacante, ip_victima)] >= 10: # hay que elegir un numero adecuado
                se_bloqueo_alguna_ip = True
                if not ip_atacante in ips_bloqueadas:
                    mensaje += 'Se bloqueo la ip: ' + ip_atacante + ' por sospecha de ataque a la ip: ' + ip_victima + ' \n'
                    ips_bloqueadas.append(ip_atacante)
                    bloquear_ip(ip_atacante)
                    registrar_en_log('prevencion', 'ataque DDOS', ip_atacante,
                    'Se detecto posible ataque DDOS. Se bloqueo la ip sospechosa')
                    #avisar al admin
        else:
            ip_ataques[(ip_atacante, ip_victima)] = 1
        #registro = str(ip_ataques) es el diccionario en un string, quizas sea util
    if se_bloqueo_alguna_ip:
        return mensaje
    else:
        return 'No se detecto comportamiento parecido a un ataque DDOS'

#print(verificar_ataque_DDOS_dns())