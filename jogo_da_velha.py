class JogoDaVelha:
    def __init__(self):
        self.tabuleiro = [[' ' for _ in range(3)] for _ in range(3)]
        self.jogador_atual = 'X'  # Jogador X começa
        self.jogo_ativo = True

    def exibir_tabuleiro(self):
        for linha in self.tabuleiro:
            print('|'.join(linha))
            print('-' * 5)

    def fazer_jogada(self, linha, coluna):
        if not self.jogo_ativo:
            print("O jogo já acabou!")
            return False

        if self.tabuleiro[linha][coluna] != ' ':
            print("Essa posição já está ocupada!")
            return False

        self.tabuleiro[linha][coluna] = self.jogador_atual
        if self.verificar_vitoria():
            self.jogo_ativo = False
            print(f"Jogador {self.jogador_atual} venceu!")
            return True

        if self.verificar_empate():
            self.jogo_ativo = False
            print("Empate!")
            return True

        self.jogador_atual = 'O' if self.jogador_atual == 'X' else 'X'  # Alterna entre X e O
        return True

    def verificar_vitoria(self):
        # Verificar linhas
        for linha in self.tabuleiro:
            if linha[0] == linha[1] == linha[2] != ' ':
                return True
        
        # Verificar colunas
        for col in range(3):
            if self.tabuleiro[0][col] == self.tabuleiro[1][col] == self.tabuleiro[2][col] != ' ':
                return True
        
        # Verificar diagonais
        if self.tabuleiro[0][0] == self.tabuleiro[1][1] == self.tabuleiro[2][2] != ' ':
            return True
        if self.tabuleiro[0][2] == self.tabuleiro[1][1] == self.tabuleiro[2][0] != ' ':
            return True

        return False

    def verificar_empate(self):
        for linha in self.tabuleiro:
            if ' ' in linha:
                return False
        return True

    def reiniciar_jogo(self):
        self.tabuleiro = [[' ' for _ in range(3)] for _ in range(3)]
        self.jogador_atual = 'X'  # Reinicia com o jogador X
        self.jogo_ativo = True
        print("O jogo foi reiniciado.")
