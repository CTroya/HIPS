
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

print(verificar_ataque_DDOS_dns())