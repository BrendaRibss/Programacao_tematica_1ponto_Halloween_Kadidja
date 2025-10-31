import random
import time

def narrar(texto, atraso=1.5):
    """Imprime texto com pausa para efeito dramático."""
    print(texto)
    time.sleep(atraso)

def introducao():
    narrar("🌕 É meia-noite em um velho cemitério.")
    narrar("Dizem que uma abóbora mágica está escondida em algum lugar aqui...")
    narrar("Mas também dizem que espíritos protegem o local. 👻")
    narrar("Você segura sua lanterna e decide começar a procurar.")

def jogar():
    posicao_abobora = random.randint(1, 5)
    chances = 3

    for tentativa in range(1, chances + 1):
        narrar(f"\nTentativa {tentativa} de {chances}")
        escolha = input("👉 Escolha um túmulo para investigar (1 a 5): ")

        # validação simples
        if not escolha.isdigit() or not (1 <= int(escolha) <= 5):
            narrar("Digite um número de 1 a 5!")
            continue

        escolha = int(escolha)

        if escolha == posicao_abobora:
            narrar("✨ Você levanta a tampa do túmulo...")
            narrar("E lá está — a ABÓBORA MÁGICA brilha em dourado! 🎃")
            narrar("Os espíritos te saúdam e desaparecem na névoa...")
            narrar("🎉 Parabéns, você venceu o jogo!")
            break
        else:
            narrar("Você abre o túmulo... um vento gelado sopra...")
            if random.choice([True, False]):
                narrar("Um fantasma aparece! Você corre gritando! 😱")
            else:
                narrar("Nada acontece, mas o frio aumenta... 🥶")
    else:
        narrar("\nOs sinos tocam... o sol nasce e o cemitério desaparece.")
        narrar("Você falhou em encontrar a abóbora mágica. ☠️")

def jogar_novamente():
    while True:
        resposta = input("\nDeseja jogar novamente?: ").lower()
        if resposta == "s":
            jogar()
        elif resposta == "n":
            narrar("🦇 Até a próxima noite sombria...")
            break
        else:
            print("Digite 's' ou 'n'.")

# Início do jogo
if __name__ == "__main__":
    introducao()
    jogar()
    jogar_novamente()
