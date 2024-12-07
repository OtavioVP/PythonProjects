import random
import string

def passworGenerator(len_pass=8):
    #Concatenando caracteres para geração da senha
    ascii_options = string.ascii_letters
    number_options = string.digits
    punt_options = string.punctuation
    options = ascii_options + number_options + punt_options
    
    #GUARDA SENHA
    passwor_user = ""

    #ADICIONA CARACTERES A STRING QUE EM PYTHON É UMA LISTA DE CARACTERES
    for i in range(0, len_pass):
        digit = random.choice(options)
        passwor_user += digit
    
    
    return passwor_user

choice_user = input("Quantos digitos na senha? ")

#VALIDAÇÃO ENTRADA USUÁRIO
if choice_user.isdigit():
    choice_user = int(choice_user)

else:
    print("Entrada inválida")
    quit()

response = passworGenerator(len_pass = choice_user)
print("Senha gerada: ",response)