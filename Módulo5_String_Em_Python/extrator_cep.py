endereco = "Rua das Flores 72, apartamento 1002, Laranjeiras, Rio de Janeiro, RJ, 23440120"

import re   # Regular Expression -- RegEx

# 5 Digitos + Hifen (Opcional) + 3 Digitos

padrao = re.compile('[0123456789][0123456789][0123456789][0123456789][0123456789][-]?[0123456789][0123456789][0123456789]')
busca = padrao.search(endereco) # Match
if busca:
    cep = busca.group()
    print('\n', cep, '\n')
