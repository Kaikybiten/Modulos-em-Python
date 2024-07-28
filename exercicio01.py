from datetime import datetime
from dateutil.relativedelta import relativedelta
from itertools import count

EMPRESTIMO = 1_000_000
data_parcelas = datetime(2020, 12, 20)
DATA_FIM = datetime(2025, 12, 20)

TEMPO_ENTRE_PARCELAS = relativedelta(months=1)
contador_parcelas = count(start=1)
total_pago = 0
valor_parcelas = int(EMPRESTIMO / (12 * 5))

while (data_parcelas < DATA_FIM):
    print()
    data_parcelas += TEMPO_ENTRE_PARCELAS
    numero_parcela = next(contador_parcelas)
    print(f'{numero_parcela}° Parcela - {data_parcelas}')
    if (numero_parcela < 12 * 5):
        total_pago += valor_parcelas
        print(f'R$ {total_pago:.2f}')
        continue
    total_pago += valor_parcelas + int(EMPRESTIMO % (12 * 5))
    print(f'R$ {total_pago:.2f}')
