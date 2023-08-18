# datetime.timedelta e dateutil.relativetimedelta (calculando datas)
# Docs:
# https://dateutil.readthedocs.io/en/stable/relativedelta.html
# https://docs.python.org/3/library/datetime.html#timedelta-objects
from datetime import datetime, timedelta

from dateutil.relativedelta import relativedelta

fmt = '%d/%m/%Y %H:%M:%S'
date_inicio = datetime.strptime('20/04/1987 09:30:30', fmt)
date_fim = datetime.strptime('12/12/2022 08:20:20', fmt)

delta_ = timedelta(days=10, hours=2)
print(date_fim + delta_)

delta = relativedelta(date_fim, date_inicio)
print(delta)
print(delta.years, delta.days)

print(date_fim)
print(date_fim + relativedelta(seconds=59, minutes=10))

# delta = date_fim - date_inicio
# print(delta.days, delta.seconds, delta.microseconds)
# print(delta.total_seconds())

# print(date_fim > date_inicio)
# print(date_fim < date_inicio)
# print(date_fim == date_inicio)
