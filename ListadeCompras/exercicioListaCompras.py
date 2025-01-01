import os

listadeCompras = []

while True: 
    print("\n")

    print("Selecione uma opção:")
    #Opções de entrada do usuário
    choise = input("[i]nserir [a]pagar [l]istar: ").lower()

    #Nesta variável está guardada todas as opções de números de 0 a 10 em formato de string para invalidar a opção selecionada pelo usuário, caso ele escolha um número como opção. Pode ser aperfeiçoada para qualquer número.
    numberCondition = choise == '0' or choise == '1' or choise == '2' or choise == '3' or choise == '4' or choise == '5' or choise == '6' or choise == '7' or  choise == '8' or choise == '9' or choise == '0' or choise == '10'
    
    #Invalida entrada caso ele deixe o campo vazio
    if choise == ' ' or choise == '':
        print("Campo vazio, tente novamente")
        continue
    
    #Invalida entrada do usuário caso ele digite um número
    elif numberCondition:
        print("Caractere inválido, digite uma string")
        continue
    
    #Inserir elemento na lista de compras
    elif choise == 'i':
        inserir = input("Digite o item da sua lista de compra: ")
        listadeCompras.append(inserir)
        os.system('cls')

    #Apaga um elemento na lista com base no indice da lista escolhido pelo usuário   
    elif choise == 'a':
        indice = int(input("Digite o número correspondente ao item da lista que gostaria de apagar: "))
        listadeCompras.pop(indice)
    
    #Faz a listagem enumerada da lista de compras
    elif choise == 'l':
        os.system('cls')
        for indiceLista in enumerate(listadeCompras):
            indice, nome = indiceLista
            print(indice, nome)

    else:
        os.system('cls')
        print("Opção inválida, tente novamente com uma das opções válidas")