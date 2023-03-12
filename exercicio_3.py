"""
Exercício n° 3 - Se um produto que vc quer comprar custa (??) reais,
qual será o valor do mesmo com um desconto de (??)%.

Formular para resolver o exercício: vf = vi * desc / 100 - vi.

"""
print("Exercício n°3 - Calculadora de Desconto")

vi = input("Qual o valor do produto? ")
desc = input("Qual a porcentagem de desconto? ")
vf = float(vi) * float(desc) / 100
vd = float(vi) - float(vf)
print(f"O valor final com o desconto é R$ {vd}.")
