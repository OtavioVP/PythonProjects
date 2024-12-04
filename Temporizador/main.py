import time

tempo = input("Digite a quantidade de tempo em segundos: ")

#VERIFICA SE A ENTRADA É UM NÚMERO
if tempo.isdigit():
    tempo = int(tempo)
else:
    print("Entrada inválida")
    quit()

#CONVERTENDO PARA SEGUNDOS E REALIZANDO A CONTAGEM
while tempo>0:
    minutes, seconds = divmod(tempo,60 )
    #ajustando exibição para o usuário
    timer = "{:02d}:{:02d}".format(minutes, seconds)
    print(timer, end="\r")
    time.sleep(1)
    tempo = tempo - 1

print("Time is over")