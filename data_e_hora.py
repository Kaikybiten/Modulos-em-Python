# https://docs.python.org/3/library/datetime.html
from datetime import datetime, timedelta
from pytz import timezone

# Ano, Mês, Dia, Horas, Minutos, Segundos, Microsegundos...
data = datetime(2024, 7, 9, 12, 15)
print(data)  # 2024-07-09 12:15:00
print()

data_str_data = '09/07/2024 12:20:00'
data_str_formato = '%d/%m/%Y %H:%M:%S'  # Diretiva

data_str = datetime.strptime(data_str_data, data_str_formato)
print(data_str)  # 2024-07-09 12:20:00
print(data_str.strftime(data_str_formato))  # 09/07/2024 12:20:00

data_atual = datetime.now()
print(data_atual)
print()

# Timezones : https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
# Para ultilizar as Timezones, é necessario instalar a biblioteca pytz, com os
# tipos types-typz - pip install pytz types-pytz -
tempo_sp = datetime.now(timezone('America/Sao_Paulo'))
print(tempo_sp)
print()

# Segundos desde 00:00:00 UTC de 1 de janeiro de 1970 (inicio da época Unix)
print(data_atual.timestamp())
print(datetime.fromtimestamp(1720541484.823622))
print()

# Timedelta é a diferença entre duas datas
data_inicio = datetime(2024, 7, 9, 12, 30)
data_fim = datetime(2026, 7, 9, 15, 46)

delta = data_fim - data_inicio
print(delta)

print(delta.days, delta.seconds)
print(delta.total_seconds())

DELTA_DEZ_DIAS = timedelta(days=10)  # Criando um delta
print(data_inicio + DELTA_DEZ_DIAS)
