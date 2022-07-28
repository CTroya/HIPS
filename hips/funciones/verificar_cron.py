# Le pasas la ruta donde se guardan las tareas del cron y te imprime info sobre lq hay
# Normalmente esta aca: /var/spool/cron/crontabs
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

print(verificar_cron())