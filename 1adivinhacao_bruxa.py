import random

def jogar_adivinhacao():

    print("🧙‍♀️ Bem-vindo à Cabana da Bruxa! 🕯️")
    print("A Bruxa de Salem guardou um **Número Secreto** em seu caldeirão.")
    print("Você tem poucas chances para descobrir, ou **UM FEITIÇO** cairá sobre você!\n")

    numero_secreto = random.randint(1, 50)

    tentativas_maximas = 7
    tentativas_restantes = tentativas_maximas
    acertou = False

    while tentativas_restantes > 0 and not acertou:
        print(f"Tentativas restantes: {tentativas_restantes}")

        try:
            chute = int(input("Qual o seu palpite entre 1 e 50? "))
        except ValueError:
            print("⚠️ Entrada inválida! Digite apenas números inteiros.\n")
            continue  # volta para o início do loop sem perder tentativa

        if chute < 1 or chute > 50:
            print("O palpite deve estar entre 1 e 50. Preste atenção!\n")
            continue  # também não desconta tentativa por erro simples

        tentativas_restantes -= 1

        if chute == numero_secreto:
            print(f"\n🎉 PARABÉNS! Você quebrou o feitiço! O número era **{numero_secreto}** 🪄")
            acertou = True
        elif chute > numero_secreto:
            print("📉 Muito alto! O caldeirão borbulha dizendo que o número é **MENOR**.\n")
        else:
            print("📈 Muito baixo! A fumaça do caldeirão indica que o número é **MAIOR**.\n")

    if not acertou:
        print("\n💀 Suas chances acabaram! O feitiço está completo!")
        print(f"O número secreto da Bruxa era **{numero_secreto}** ☠️")

# Corrigido: este é o formato certo para executar o jogo diretamente
if __name__ == "__main__":
    jogar_adivinhacao()

    