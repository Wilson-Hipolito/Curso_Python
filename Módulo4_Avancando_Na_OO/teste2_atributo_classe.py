class Pessoa:
    tamanho_cpf = 11

p = Pessoa()

print(p.tamanho_cpf)

p.tamanho_cpf = 12

print(p.tamanho_cpf)

print(Pessoa.tamanho_cpf)

#O que acontece é que, caso não exista o atributo tamanho_cpf na instância, o Python busca o atributo na classe. Em seguida, adicionamos um atributo tamanho_cpf na instância e quando dizemos que o valor é 12, o atributo da classe não é alterado, já que são atributos diferentes, um da classe e outro só da instância.