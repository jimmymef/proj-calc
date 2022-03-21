from msilib.schema import Error
import sys
import pytest
sys.path.insert(1, '../../src')
import calc

# Test get fraction
def obtener_datos_get_fraction():
    return([("3/4", 0.75), ("0/1", 0), ("30/40", 0.75), ("-300/400", -0.75), ("300/-400", -0.75)])

@pytest.mark.parametrize('fraccion, esperado', obtener_datos_get_fraction())
def test_get_fractions(fraccion, esperado):
    assert calc.get_fractions(fraccion) == esperado

@pytest.mark.xfail
def test_get_fractions_0_division():
    assert calc.get_fractions("30/0") == 30/0