print("Bem-vindo ao jogo de Advinhação!")

numero_secreto = 42

chute_str = input("Digite o seu número: ")

print("Você digitou ", chute_str)

chute = int(chute_str)

if numero_secreto == chute:
    print("Você acertou")
else:
    print("Você errou")

print("Fim do Jogo")
