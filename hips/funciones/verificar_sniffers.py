import os
from matar_proceso import matar_proceso

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

print(verificar_sniffers())