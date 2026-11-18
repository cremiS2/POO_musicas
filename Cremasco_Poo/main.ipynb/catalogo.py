from musica import Musica

class Catalogo:
    def __init__(self):
        self.musicas = []
        self.musica_atual = None
        self.reproducoes = {}
        self.favoritos = {}

    def adicionar_musica(self, musica):
        #Validação
        if not isinstance(musica, Musica):
            raise TypeError("É necessário informar um objeto da classe Musica")
        self.musicas.append(self.musica)
        self.reproducoes[musica] = 0
        # chamar um metodo de favorito aqui
        print(f"A musica {musica.nome} foi adicionada ao catalogo de musicas")

