#Formatando datas em strings usando o método strftime().

from datetime import datetime
import pytz
from pytz import timezone

data_e_hora_atual = datetime.now()
fuso_horario = timezone('America/Sao_Paulo')

data_e_hora_sao_paulo = data_e_hora_atual.astimezone(fuso_horario)
data_e_hora_sao_paulo_em_texto = data_e_hora_sao_paulo.strftime('%d/%m/%y - %H:%M')

print('\n', data_e_hora_sao_paulo_em_texto, '\n')

for tz in pytz.all_timezones:
    print(tz)
