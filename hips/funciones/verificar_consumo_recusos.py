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


