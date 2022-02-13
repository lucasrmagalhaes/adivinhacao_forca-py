def jogar():
    print("***************************")
    print("Bem-vindo ao jogo de Forca!")
    print("***************************")

    palavra_secreta = "banana"
    letras_acertadas = ["_", "_", "_", "_", "_", "_"]

    enforcou = False
    acertou = False

    print(letras_acertadas)

    while not enforcou and not acertou:
        chute = input("Qual letra? ")
        chute = chute.strip()

        index = 0

        for letra in palavra_secreta:
            if chute.upper() == letra.upper():
                letras_acertadas[index] = letra
            index += 1

        print(letras_acertadas)

    print("Fim do Jogo")


if __name__ == "__main__":
    jogar()
