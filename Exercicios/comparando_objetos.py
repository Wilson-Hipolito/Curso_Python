# Comparando objetos no Python.

class Filmes():
    def __init__(self, titulo, diretor):
        self.titulo = titulo
        self.diretor = diretor

    def __str__(self):
        return self.titulo + ' - ' + self.diretor

    def __eq__(self, outro_filme):
        return self.titulo == outro_filme.titulo


teoria_de_tudo = Filmes('A Teoria de Tudo', 'James Marsh')
la_la_land = Filmes('La La Land', 'Damien Chazelle')
poderoso_chefao = Filmes('O Poderoso Chefão', 'Francis Ford Coppola')


def pega_todos_os_filmes():
    meus_filmes = [teoria_de_tudo, la_la_land, poderoso_chefao]
    return meus_filmes


meus_filmes = pega_todos_os_filmes()
for filme in meus_filmes:
    print(filme)


def tenho_o_filme(filme_procurado):
    meus_filmes = pega_todos_os_filmes()
    return filme_procurado in meus_filmes


filme_procurado = Filmes('A Teoria de Tudo', 'James Marsh')


if tenho_o_filme(filme_procurado):
    print('\nTenho o Filme!')
else:
    print('\nNão Tenho :(')
