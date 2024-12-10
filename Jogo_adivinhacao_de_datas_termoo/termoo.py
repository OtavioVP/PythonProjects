import json
import random

file = open("words.json", encoding="utf8")

words = json.load(file)

choice_a = random.choice(list(words.keys()))

print("Bem vindo ao jogo de adivinhação")
print("Você deve conseguir advidinhar a data de um acontecimento histórico, digite 8 número de acordo com o formato abaixo")
print("================================")

trys = 5
win = False

while trys > 0 and win is not True:
    print("Dica: " + words[choice_a])
    user_choice = input("Data: DDMMAAAA\n")
    print("===============================")

    trys-=1
    if len(user_choice) != 8:
        print("Erro de entrada, sua resposta deve ter exatamente 8 dígitos")
        continue
    #stop on minute 18:31
    if user_choice.isdigit():
        check = []
        points = 0
        for i in range(8):
            if user_choice[i] == choice_a[i]:
                check.append("✅")
                points += 1
            else:
                check.append("❌")
        
        print("Resposta: \n")
        print("|".join(check))
        print(" |".join(user_choice))
        print("============================\n")
        if points == 8:
            win = True      
    else:
        print("Erro na entrada, a resposta precisa necessariamente ser uma data!")
        continue

if win == True:
    print("Vitória")
else:
    print("Derrota")