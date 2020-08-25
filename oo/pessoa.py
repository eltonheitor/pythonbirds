class Pessoa:
    def __init__(self, *filhos, nome=None,idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    filho = Pessoa(nome="Heitor")
    pai   = Pessoa(filho,nome='Elton')
    for filho in pai.filhos:
        print(filho.nome)
