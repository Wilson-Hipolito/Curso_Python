
def cria_conta(numero, titular, saldo):
    conta = {"numero": numero, "títular": titular, "saldo": saldo}
    return conta


def deposita(conta, valor):
    conta["saldo"] += valor


def saque(conta, valor):
    conta["saldo"] -= valor


def extrato(conta):
    print("Saldo é {}".format(conta["saldo"]))
