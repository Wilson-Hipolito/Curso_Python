#Erança Multipla.

class Funcionario:
    def __init__(self, nome):
        self.nome = nome

    def registra_horas(self, horas):
        print(f'Horas registradas...')

    def mostrar_tarefas(self):
        print(f'Fez muita coisa...')


class Caleum(Funcionario):
    def mostrar_tarefas(self):
        print(f'Fez muita coisa, Caelumer...')

    def busca_cursos_do_mes(self, mes=None):
        print(f'Mostrando cursos - {mes}' if mes else 'Mostrando cursos desse mês.')


class Alura(Funcionario):
    def mostrar_tarefas(self):
        print('Fez muita coisa, Alurete...')

    def buscar_perguntas_sem_resposta(self):
        print('Mostrando perguntas não respondidas do fórum...')


class Hipster:
    def __str__(self):
        return f'Hipster, {self.nome}'


class Junior(Alura):
    pass


class Pleno(Alura, Caleum, Hipster):
    pass


class Senior(Alura, Caleum, Hipster):
    pass


jose = Junior('José')
jose.buscar_perguntas_sem_resposta()

luan = Pleno('Luan')
luan.buscar_perguntas_sem_resposta()
luan.busca_cursos_do_mes()
luan.mostrar_tarefas()
print(luan)

joao = Senior('João')
print(joao)
