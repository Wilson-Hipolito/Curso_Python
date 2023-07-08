class Pessoa:
    tamanho_cpf = 11

    def __init__(self, cpf, nome):
        self.cpf = cpf
        self.nome = nome

    def valida_cpf(self):
        return True if len(self.cpf) == __class__.tamanho_cpf else False


pe = Pessoa("00000000001", "Renata")
print(pe.valida_cpf())

pe = Pessoa("0000000000002", "Wilson")
print(pe.valida_cpf())

#Veja como o valor de `tamanho_cpf` é usado por todas as instâncias. Esse é um atributo de classe. É possível alterar o valor deste atributo, mudando seu estado e não é necessário criar uma instância para acessá-lo. No trecho de código acima, precisamos usar o `__class__` para definir que queremos o atributo de classe. Dentro do nosso método de instância precisamos fazer desta forma. Se não fizermos deste jeito, podemos ter problemas.