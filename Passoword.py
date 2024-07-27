import random
import string

def Password(long):
    caracteres = string.ascii_letters + string.digits + string.punctuation

    password = ''.join(random.choice(caracteres) for i in range(long)) 
    return password
    

long = int(input("Digite o comprimento da senha: "))

print(f"Senha gerada: {Password(long)}")
        


