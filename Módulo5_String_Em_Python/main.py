#Trabalhando com URLs.

url = "\nhttps://bytebank.com/cambio?moedaDestino=Dolar&moedaOrigem=real\n"
#print(url)

procurando_string = url.find('?')
#print('A String está na posição: {}'.format(procurando_string))

indice_interrogacao = url.find('?')
url_base = url[:indice_interrogacao]
#print(url_base, '\n')

url_parametros = url[indice_interrogacao+1:]
print(url_parametros, '\n')

parametro_busca = 'moedaOrigem'
indice_parametro = url_parametros.find(parametro_busca)
print(indice_parametro)

indice_valor = indice_parametro + len(parametro_busca) + 1
valor = url_parametros[indice_valor:]
print(valor)
