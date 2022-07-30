import os
from .matar_proceso import matar_proceso
from .registrar_en_log import registrar_en_log
import subprocess
from .cuarentena import cuarentena

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
            pid = resultado.split()[1] 
            programa = resultado.split()[2]
            matar_proceso(pid)
            if not programa in detectados:
                detectados.append(programa)
                ruta_sniffer = subprocess.run(['which',programa], capture_output=True, text=True)
                print(ruta_sniffer.stdout.split()[0])
                cuarentena(ruta_sniffer.stdout.split()[0])
                mensaje += 'Se encontro el sniffer: ' + programa + ' ejecutandose. Se envio el sniffer a cuarentena\n'
                registrar_en_log(
                    'prevencion', 'sniffer encontrado', '',
                    'Se encontro el sniffer: ' + programa + ' ejecutandose. Se envio el sniffer a cuarentena'
                )
                # avisar al admin
    # Veo si existe alguna herramienta
    if mensaje == '':
        return 'No se detectaron sniffers en el sistema'
    else:
        return mensaje

#print(verificar_sniffers())