import datetime
from decimal import Decimal

tupla = (1, datetime.datetime(2022, 3, 28, 9, 10, 54), Decimal('22.00'), Decimal('175.00'))

dic = {tupla[0]: {'Fecha Actualización': tupla[1],
                    'Temperatura': tupla[1],
                     'Luminosidad': tupla[1],
                     }
      }

dic[2] = {'Fecha Actualización': tupla[1],
                    'Temperatura': tupla[1],
                     'Luminosidad': tupla[1],
                     }
print(dic)