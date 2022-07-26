# Le pasasla ruta de un archivo y te retorna el hash en hexadecimal como un string
import hashlib

def hashear_archivo(ruta_arvhivo):
    file = ruta_arvhivo
    BLOCK_SIZE = 65536 # The size of each read from the file
    file_hash = hashlib.md5() # Create the hash object, can use something other than `.sha256()` if you wish
    with open(file, 'rb') as f: # Open the file to read it's bytes
        fb = f.read(BLOCK_SIZE) # Read from the file. Take in the amount declared above
        while len(fb) > 0: # While there is still data being read from the file
            file_hash.update(fb) # Update the hash
            fb = f.read(BLOCK_SIZE) # Read the next block from the file
    return file_hash.hexdigest()
'''
hasheado = hashear_archivo("/etc/passwd")
print(hasheado)
'''