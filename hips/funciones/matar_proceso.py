# Le das el pid de un proceso y te lo mata
import subprocess

def matar_proceso(pid):
    subprocess.run(['kill', '-9', str(pid)], capture_output=True, text=True)
    #print('Se mato al proceso: '+ str(pid))

#matar_proceso(38026)