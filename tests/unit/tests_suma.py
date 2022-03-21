from msilib.schema import Error
import sys
import pytest
sys.path.insert(1, '../../src')
import calc

# Test suma
def obtener_datos_suma():
    return([(5, 6, 11), (15, 60, 75), (-1, -2, -3), ("1/4", "3/4", 1), ("1/2", "-1/2", 0)])

@pytest.mark.parametrize("sumando_a, sumando_b, esperado", obtener_datos_suma())
def test_suma(sumando_a, sumando_b, esperado):
    assert calc.suma(sumando_a, sumando_b) == esperado