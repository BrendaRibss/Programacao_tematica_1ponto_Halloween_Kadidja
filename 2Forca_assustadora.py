import random
import os  # Módulo para limpar a tela do console

def exibir_forca(erros):
    """Desenha a forca de acordo com o número de erros."""
    # A forca é um exemplo de como o algoritmo pode representar estados.
    stages = [
        """
        ------
        |    |
        |
        |
        |
        |
        =========
        """,
        # 1 erro
        """
        ------
        |    |
        |    O
        |
        |
        |
        =========
        """,
        # 2 erros
        """
        ------
        |    |
        |    O
        |    |
        |
        |
        =========
        """,
        # 3 erros
        """
        ------
        |    |
        |    O
        |   /|
        |
        |
        =========
        """,
        # 4 erros
        """
        ------
        |    |
        |    O
        |   /|\\
        |
        |
        =========
        """,
        # 5 erros (CORPO COMPLETO)
        """
        ------
        |    |
        |    O
        |   /|\\
        |   / \\
        |
        =========
        """
    ]
    print(stages[erros])

def jogar_forca():
    """Função principal do Jogo da Forca com tema Halloween."""
    print("🕸️🎃 Bem-vindo ao Jogo da Forca de Halloween! 🧙‍♀️\n")
    print("Tente adivinhar a palavra MISTERIOSA (relacionada ao tema Halloween)")
    print("Mas cuidado... a cada erro a bruxa se aproxima até que o *FEITIÇO* se complete!\n")

    # 1. Configuração (Lista de Palavras e Sorteio)
    palavras_tema = ["ABÓBORA", "BRUXA", "MAGO", "VASSOURA", "FANTASMA", "ASSOMBRAÇÃO",
                     "CAVEIRA", "FEITIÇO", "ESQUELETO", "CALDEIRÃO", "MURCHO", "CONJURO"]
    palavra_secreta = random.choice(palavras_tema).upper()

    # 2. Variáveis de controle
    letras_descobertas = ["_" for letra in palavra_secreta]
    letras_erradas = []
    erros = 0
    max_erros = 5

    # 3. Loop Principal
    while erros < max_erros and "_" in letras_descobertas:
        os.system("cls" if os.name == "nt" else "clear")
        exibir_forca(erros)
        print("\nPalavra: ", " ".join(letras_descobertas))
        print(f"🩸 Letras erradas: {', '.join(letras_erradas)}")
        print(f"Tentativas restantes: {max_erros - erros}\n")

        # Entrada do jogador
        chute = input("🔮 Escolha uma letra: ").upper()

        if len(chute) != 1 or not chute.isalpha():
            print("⚠️ Digite apenas uma letra válida!\n")
            continue

        # 4. Verificação da letra
        if chute in letras_descobertas or chute in letras_erradas:
            print("⚠️ Você já tentou essa letra! Tente outra.\n")
            continue

        if chute in palavra_secreta:
            print("✨ Boa! A letra faz parte da palavra.\n")
            for i, letra in enumerate(palavra_secreta):
                if letra == chute:
                    letras_descobertas[i] = chute
        else:
            print("💀 A bruxa riu! Essa letra não está na palavra...\n")
            letras_erradas.append(chute)
            erros += 1

    # 5. Encerramento do jogo
    os.system("cls" if os.name == "nt" else "clear")
    exibir_forca(erros)

    if "_" not in letras_descobertas:
        print(f"🎉 Parabéns! Você quebrou o feitiço e descobriu a palavra: {palavra_secreta}!")
    else:
        print("👻 O feitiço foi lançado! A bruxa venceu desta vez...")
        print(f"A palavra secreta era: {palavra_secreta}")

if __name__ == "__main__":
    jogar_forca()


















    
