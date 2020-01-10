


"""
EXEMPLO DE USO SENHAS:

senha = criar_hash_senha('teste')
print(senha)
print(verificar_hash_senha(senha,'teste'))
"""
import hashlib, binascii, os
def criar_hash_senha(password):
    #Hash uma senha para armazenar
    salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
    pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), 
                                salt, 100000)
    pwdhash = binascii.hexlify(pwdhash)    
    return (salt + pwdhash).decode('ascii')
 
def verificar_hash_senha(stored_password, provided_password):
    #Verifique uma senha armazenada em relação à fornecida pelo usuário
    salt = stored_password[:64]
    stored_password = stored_password[64:]
    pwdhash = hashlib.pbkdf2_hmac('sha512', 
                                  provided_password.encode('utf-8'), 
                                  salt.encode('ascii'), 
                                  100000)
    pwdhash = binascii.hexlify(pwdhash).decode('ascii')
    return pwdhash == stored_password

import calendar
def lista_meses():
    lista = [('', 'Select month')] + [(str(x), calendar.month_name[x]) for x in range(1, 13)]
    return lista

