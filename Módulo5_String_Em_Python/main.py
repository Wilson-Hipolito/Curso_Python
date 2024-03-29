#Trabalhando com URLs.

# url = "\nhttps://bytebank.com/cambio?quantidade=100&moedaDestino=Dolar&moedaOrigem=real\n"
url = '  '

# Sanitização da URl.
url = url.strip()

# Validação da URL.
if url == '':
    raise ValueError('A URL Está Vazia.')

# Separa base de parâmetros.
indice_interrogacao = url.find('?')
url_base = url[:indice_interrogacao]
url_parametros = url[indice_interrogacao+1:]
print('\n', url_parametros, '\n')

# Busca o valor de um parâmentro.
parametro_busca = 'moedaDestino'
indice_parametro = url_parametros.find(parametro_busca)
indice_valor = indice_parametro + len(parametro_busca) + 1
indice_e_comercial = url_parametros.find('&', indice_valor)
if indice_e_comercial == -1:
    valor = url_parametros[indice_valor:]
else:
    valor = url_parametros[indice_valor:indice_e_comercial]

print(valor, '\n')
