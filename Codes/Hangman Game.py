import random

list = ["programaçao", "python", "java", "matematica", "ingles"]

sorteio = random.choice(list)

used = set()
miss = set()

show = ["_"] * len(sorteio)

while True:

    print("\nPalavra:","".join(show))

    choice_letter = str(input("\nEscolha uma letra")).lower()

    if choice_letter in used or choice_letter in miss:
        print("\nJá usou está letra")

    else:
        if choice_letter in sorteio:
            used.add(choice_letter)

            for posicao in range(len(sorteio)):

                if sorteio[posicao] == choice_letter:
                    show[posicao] = choice_letter

            print(f"Acertou miseravel")

        else:
            miss.add(choice_letter)
            print(f"Cemitério:\n     {miss}")

    if "_" not in show:
        print("\nVocê venceu!")
        print("Palavra:", sorteio)
        break
