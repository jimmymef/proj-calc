def get_fractions(valor : 'string') -> 'float':
  if("/" in valor):
    decimal = int (valor[0:1]) / int (valor[2:3])
    return decimal
  else:
    return float(valor)    

def suma(a : 'num_racional',b: 'num_racional') -> 'suma_de_racionales':
  sumando_a = get_fractions(a)
  sumando_b = get_fractions(b)
  return sumando_a + sumando_b