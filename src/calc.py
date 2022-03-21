def get_fractions(valor: 'string') -> 'float':
    """ Convierte fracciones (i.e a/b a,b ∈ ℕ) de string a floats.

    Parameters
    ----------
    valor: 'string' :
        Una fracción a/b donde a,b ∈ ℕ.

    Returns
    -------
    float
        El valor de la fracción en decimales.

    """

    if type(valor) == int: return(valor)
    elif type(valor) == float: return(valor)
    elif("/" in valor):
        (a, b) = valor.split("/")
        decimal = int(a) / int(b)
        return decimal
    else:
        return float(valor)


def suma(a: 'num_racional', b: 'num_racional') -> 'suma_de_racionales':
    """Suma dos números racionales a y b (a, b ∈ ℚ).

    Parameters
    ----------
    a: 'num_racional' :
        Número tipo float, o devuelto por la función get_fractions.

    b: 'num_racional' :
        Número tipo float, o devuelto por la función get_fractions.

    Returns
    -------
    float
        El resultado de sumar a y b.

    """
    sumando_a = get_fractions(a)
    sumando_b = get_fractions(b)
    return sumando_a + sumando_b


def multiplica(a: 'num_racional', b: 'num_racional') \
      -> 'multiplicaion_de_racionales':
    """Multiplica dos números racionales a y b (a, b ∈ ℚ).

    Parameters
    ----------
    a: 'num_racional' :
        Número tipo float, o devuelto por la función get_fractions.

    b: 'num_racional' :
        Número tipo float, o devuelto por la función get_fractions.


    Returns
    -------
    float
        El resultado de multiplicar a y b.

    """
    multiplicando = get_fractions(a)
    multiplicador = get_fractions(b)
    return multiplicando * multiplicador
