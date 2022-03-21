from msilib.schema import Error
import sys
import pytest
sys.path.insert(1, '../../src')
import calc

# Test multiplicación
def obtener_datos_multiplicacion():
    return([(5, 6, 30), (0, 10, 0), ("1/2", "1/2", 0.25), ("-1/2", "1/2", -0.25)])

@pytest.mark.parametrize("multiplicando, multiplicador, esperado", obtener_datos_multiplicacion())
def test_multiplicacion(multiplicando, multiplicador, esperado):
    assert calc.multiplica(multiplicando, multiplicador) == esperado