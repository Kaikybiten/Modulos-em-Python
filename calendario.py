import calendar

ano = 2024
mes = 7
dia = 9
DIAS_DA_SEMANA = list(calendar.day_name)

# Retorna o ultimo dia do mês e em qual dia da semana ele cai
print(calendar.monthrange(ano, mes))

# Retorna o dia da semana pedido
print(DIAS_DA_SEMANA[calendar.weekday(ano, mes, dia)])

# Retorna listas separadas por semanas do mês
print(calendar.monthcalendar(ano, mes))
