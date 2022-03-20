def get_fractions(valor : 'string') -> 'float':
  if("/" in valor):
    decimal = int (valor[0:1]) / int (valor[2:3])
    return decimal
  else:
    return float(valor)    