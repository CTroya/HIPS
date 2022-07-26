import os

def check_cola_correo():
    lista_msg = []
    cmd = "mailq"
    resultado_cmd = os.popen(cmd).read()
    
    if "queue is empty" in resultado_cmd:
        print("La cola esta vacia")

    else:
        resultado = resultado_cmd.splitlines()

    mail_queue = resultado_cmd.splitlines()
    
    if len(mail_queue) > 5: # elegir una cantidad adecuada
        print("Se encontraron muchos mails en la cola, se aviso al administrador")

    else:
        print('no se encontraron muchos mails en la cola')

    return lista_msg

check_cola_correo()