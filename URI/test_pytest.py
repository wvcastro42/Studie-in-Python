from ex1051 import imposto

def test_quando_imposto_receber_numero_menor_2000_entao_deve_retornar_isento():
    assert imposto(1701.12) == 'Isento'

def test_quando_imposto_receber_numero_300200_entao_deve_retornar_8036():
    assert imposto(3002.00) == 'R$ 80.36'
