# Mira el consumo de recursos en el host.
import subprocess
from matar_proceso import matar_proceso

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

print(verificar_consumo_recursos())