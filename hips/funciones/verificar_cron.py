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

verificar_cron('/var/spool/cron/crontabs')