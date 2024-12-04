import random

pontos_usuario = 0
oponente_pontos = 0
 
options = ["r", "t", "p"]

while True:
    jogada_usuario = input("Escolha R/(pedra) T/(tesoura) /P(papel) ou Q para sair: ").lower()
    
    #FINALIZA O JOGO
    if jogada_usuario == 'q':
        break
    
    #VERIFICA ENTRADA VÁLIDA DO USUÁRIO
    if jogada_usuario not in options:
        print("Você digitou um caractere invalido, tente novamente")
        continue
    
    #A máquina irá escolher uma opção ao acaso e irá receber o valor no indice da lista options     
    jogada_oponente = random.randint (0,2)
    computer_options = options[jogada_oponente]
    
    print("O computador escolheu " + computer_options)

    #CASO DE EMPATE
    if jogada_usuario == computer_options:
        print("Ambos escolheram a mesma opção, deu empate!")
        
    #CONDIÇÕES DE JOGO usuário escolhe pedra
    elif jogada_usuario == 'r' and computer_options == 't':
        print("Você ganhou!")
        pontos_usuario +=1

    elif jogada_usuario == 't' and computer_options == 'p':
        print("Você ganhou!")
        pontos_usuario +=1

    elif jogada_usuario == 'p' and computer_options == 'r':
        print("Você ganhou!")
        pontos_usuario +=1
    else:
        print("Você perdeu!")
        oponente_pontos+=1
   

print(f"Você saiu do jogo, o placar foi {pontos_usuario}/{oponente_pontos}")