import os

from cryptography.fernet import Fernet


def cargar_clave():
    if not os.path.exists("clave.key"):
        genera_clave()
    return open("clave.key", "rb").read()

def encriptar_password(password):
    clave = cargar_clave()
    f = Fernet(clave)
    return f.encrypt(password.encode())

def desencriptar_password(passwordencrypted):
    clave = cargar_clave()
    f = Fernet(clave)
    return f.decrypt(passwordencrypted)

def genera_clave():
    clave = Fernet.generate_key()
    with open("clave.key" ,"wb") as archivo_clave:
        archivo_clave.write(clave)