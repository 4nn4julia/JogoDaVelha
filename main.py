from jogo_da_velha import JogoDaVelha

# Função principal para jogar
def jogar():
    jogo = JogoDaVelha()
    while jogo.jogo_ativo:
        jogo.exibir_tabuleiro()
        try:
            linha = int(input(f"Jogador {jogo.jogador_atual}, digite a linha (1-3): ")) - 1  # Ajuste para 1-3
            coluna = int(input(f"Jogador {jogo.jogador_atual}, digite a coluna (1-3): ")) - 1  # Ajuste para 1-3
        except ValueError:
            print("Entrada inválida. Por favor, insira números entre 1 e 3.")
            continue

        if not jogo.fazer_jogada(linha, coluna):
            continue

    jogo.exibir_tabuleiro()

    resposta = input("Deseja jogar novamente? (s/n): ").strip().lower()
    if resposta == 's':
        jogo.reiniciar_jogo()
        jogar()
    else:
        print("Obrigado por jogar!")

# Começar o jogo
if __name__ == '__main__':
    jogar()
