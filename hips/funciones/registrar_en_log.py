from datetime import datetime

def registrar_en_log(log_alarmas_o_prevencion, tipo_alarma_o_prevencion, ip_origen = '', descripcion = ''):
    fecha_hora = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
    escribir = f'{fecha_hora}::{tipo_alarma_o_prevencion}::{ip_origen}::{descripcion}\n'
    if log_alarmas_o_prevencion.lower() == 'alarmas' or log_alarmas_o_prevencion.lower() == 'prevencion':
        f = open(f'/var/log/hips/{log_alarmas_o_prevencion}.log', 'a')
        f.write(escribir)
        f.close()

#registrar_en_log('prevencion','prueba')
#registrar_en_log('alarmas','prueba2')

