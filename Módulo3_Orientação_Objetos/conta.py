 

class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print("Construindo Objetos ... {}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("Saldo de {} do titular {}".format(self.__saldo, self.__titular))

    def deposita(self, valor):
        self.__saldo += valor

    def __pode_sacar(self, valor_saque):
        disponivel_saque = self.__saldo + self.__limite
        return valor_saque <= disponivel_saque

    def saque(self, valor):
        if self.__pode_sacar(valor):
            self.__saldo -= valor
        else:
            print("O valor {} ultrapassou o limite".format(valor))

    def transfere(self, valor, destino):
        self.saque(valor)
        destino.deposita(valor)

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular.title()

    @titular.setter
    def titular(self, titular):
        self.__titular = titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    @staticmethod  #Metodo estático não depende da criação de um objeto.
    def codigos_bancos():
        return {'BB': '001', 'Caixa': '104', 'Bradesco':'237'}

    cartoes = {"Mastercard":"01", "Visa":"02", "Elo":"03", "AmericanExpress":"04"}
    #O atributo faz parte da classe, ou seja, é um atributo estático que pode ser usado sem ter criado um objeto.
