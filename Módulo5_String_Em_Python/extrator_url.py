class ExtratorUrl:
    def __init__(self, url):
        self.url = self.sanitiza_url(url)
        self.valida_url()
        self.valida_url_base()

    def sanitiza_url(self, url):
        if type(url) == str:
            return url.strip()
        else:
            return ''

    def valida_url(self):
        if not self.url:
            raise ValueError('A URL Está Vazia.')

    def get_url_base(self):
        indice_interrogacao = self.url.find('?')
        url_base = self.url[:indice_interrogacao]
        return url_base

    def valida_url_base(self):
        if not self.get_url_base().startswith('https'):
            raise ValueError('Https não encontrado.')
        if not self.get_url_base().endswith('/cambio'):
            raise ValueError('Página Não Encontrada')

    def get_url_parametros(self):
        indice_interrogacao = self.url.find('?')
        url_parametros = self.url[indice_interrogacao + 1:]
        return url_parametros

    def get_valor_parametro(self, parametro_busca):
        indice_parametro = self.get_url_parametros().find(parametro_busca)
        indice_valor = indice_parametro + len(parametro_busca) + 1
        indice_e_comercial = self.get_url_parametros().find('&', indice_valor)
        if indice_e_comercial == -1:
            valor = self.get_url_parametros()[indice_valor:]
        else:
            valor = self.get_url_parametros()[indice_valor:indice_e_comercial]
        return valor


url_inicio = "https://bytebank.com/cambio?quantidade=100&moedaDestino=Dolar&moedaOrigem=real"
extrator_url = ExtratorUrl(url_inicio)

valor_quantidade = extrator_url.get_valor_parametro('quantidade')
valor_moeda_origem = extrator_url.get_valor_parametro('moedaOrigem')
valor_moeda_destino = extrator_url.get_valor_parametro('moedaDestino')

print('\n', valor_quantidade)
print(valor_moeda_origem)
print(valor_moeda_destino, '\n')
