import subprocess

def configuracion_inicial():
    resultado = subprocess.run(['bash', './configuracion_inicial.sh'], capture_output=True, text=True)
    return 'Se realizo la configuracion inicial, ya se puede utilizar el HIPS.'