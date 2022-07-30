# Mira el consumo de recursos en el host.
import subprocess
from .matar_proceso import matar_proceso
from .registrar_en_log import registrar_en_log

def verificar_consumo_recursos():
    # CONSUMO CPU
    comando_ps = subprocess.run(['ps', 'aux', '--sort', '-pcpu'], 
    check=True, capture_output=True, text=True)
    comando_awk = subprocess.run(['awk', '{print $2, $3, $11}'], 
    input=comando_ps.stdout, capture_output=True, text=True)
    comando_head = subprocess.run(['head', '-10'],
    input = comando_awk.stdout, capture_output=True, text=True)
    resultado_cpu = comando_head.stdout.split('\n')
    del resultado_cpu[-1] # le saco el '' que tiene la lista al final
    bandera = True
    mensaje = ''
    for linea in resultado_cpu:
        # Para saltarme la primera linea del output del comando
        if bandera == True:
            bandera = False
            continue
        if float(linea.split()[1]) >= 90:
            mensaje += 'El proceso: ' + linea.split()[2] + ' con pid = '
            + linea.split()[0] + ' esta consumiendo: ' + linea.split()[1] 
            + '% de cpu. Se procede a matar al proceso \n'
            matar_proceso(linea.split()[0])
            registrar_en_log('prevencion','consumo cpu','',
            'El proceso: ' + linea.split()[2] + ' esta consumiendo: ' 
            + linea.split()[1] + '% de cpu. Se termino su ejecucion')
            # avisar al admin
    bandera = True
    # CONSUMO MEMORIA
    comando_ps_mem = subprocess.run(['ps', 'aux', '--sort', '-%mem'],
    check=True, capture_output=True, text=True)
    comando_awk_mem = subprocess.run(['awk', '{print $2, $4, $11}'], 
    input=comando_ps_mem.stdout, capture_output=True, text=True)
    comando_head_mem = subprocess.run(['head', '-10'],
    input = comando_awk_mem.stdout, capture_output=True, text=True)
    resultado_mem = comando_head_mem.stdout.split('\n')
    del resultado_mem[-1] # le saco el '' que tiene la lista al final
    for linea in resultado_mem:
        # Para saltarme la primera linea del output del comando
        if bandera == True:
            bandera = False
            continue
        if float(linea.split()[1]) >= 90: 
            mensaje += 'El proceso: ' + linea.split()[2] + ' con pid = '
            + linea.split()[0] + ' esta consumiendo: ' + linea.split()[1] 
            + '% de memporia ram. Se procede a matar al proceso \n'
            matar_proceso(linea.split()[0])
            registrar_en_log('prevencion','consumo ram','',
            'El proceso: ' + linea.split()[2] + ' esta consumiendo: ' 
            + linea.split()[1] + '% de ram. Se termino su ejecucion')
            # avisar al admin
    if mensaje == '':
        return 'No se detecto consumos significativos de los recursos'
    else:
        return mensaje

#print(verificar_consumo_recursos())