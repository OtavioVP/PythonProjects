#TEXTI INICIAL DE BOAS VINDAS
print("Seja muito bem-vindo@ ao quiz do Otávio")
resposta_usuario = input("Deseja iniciar o quiz? (S/N)")


if resposta_usuario != 'S':
    print("Ok, o quiz será encerrado")
    quit()
print('começando...')

#Variável que irá armazenar a pontuação do jogador
score = 0

#Primeira pergunta
print("Quem é o técnico do Fortaleza atualmente? \n (A) Pepe Guardiola \n (B) Carlo Ancelotti \n (C) Juan Pablo Vojvoda \n (D) Rogério Ceni")
resposta_1 = input("Respota: ")
if resposta_1 == 'C':
    print("Resposta correta!")
    score += 1
else:
    print("Resposta incorreta! ")


#Segunda pergunta
print("Quem é o artilheiro do Fortaleza na temporada? \n (A) Thiago Galhardo \n (B) Moisés \n (C) Lucero \n (D) Pikachu")

resposta_2 = input("Respota: ")
if resposta_2 == 'C': 
    print("Resposta correta!")
    score += 1

else:
    print("Resposta incorreta! ")


#Terceira pergunta
print("Quem foi o campeão na Copa do Nordeste 2024? \n (A) Fortaleza \n (B) Ceará \n (C) Sport \n (D) Bahia")

resposta_3 = input("Respota: ")
if resposta_3 == 'A':
    print("Resposta correta!")
    score += 1

else:
    print("Resposta incorreta! ")


#Quarta pergunta
print("Qual clube do Nordeste detém a maior pontuação na história dentre clubes nordestinos no Campeonato Brasileiro de pontos corridos? \n (A) Fortaleza \n (B) Bahia \n (C) Ceará \n (D) Sport")

resposta_4 = input("Respota: ")
if resposta_4 == 'A':
    print("Resposta correta!")
    score += 1

else:
    print("Resposta incorreta! ")

#Quinta pergunta
print("Em que ano o Fortaleza conquistou seu primeiro título da Série B do Campeonato Brasileiro? \n (A) 2002 \n (B) 2009 \n (C) 2018 \n (D) 2022")

resposta_5 = input("Respota: ")
if resposta_5 == 'C':
    print("Resposta correta!")
    score += 1

else:
    print("Resposta incorreta! ")


print(f'O quiz chegou ao fim e sua pontuação foi de {score}/5, Parabéns!')