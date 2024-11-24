import random

print("O jogo de adivinhar número irá começar...")

 
#SORTEIO DE NÚMERO ALEATORIO
numero_aleatorio = random.randint(0,10)
# print(numero_aleatorio)

#CONTADOR DE TENTATIVAS
quant_tentativas = 1

#TENTATIVAS
while True:
    numero_escolhido = int(input("Digite um número de 0 a 10: "))
    if numero_escolhido == numero_aleatorio:
        print(f"Você acertou! O número sorteado foi {numero_aleatorio}")
        break
    else:
        quant_tentativas += 1
        if numero_aleatorio > numero_escolhido:
            print("O número aleatório é maior")
        else:
            print("O número aleatório é menor")
print(f"E você tentou {quant_tentativas} vezes!")
        
