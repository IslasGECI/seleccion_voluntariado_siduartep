import pytest
from seleccion_voluntariado_2023 import generar_codigo, ERROR_DE_STRING_VACIO, ERROR_DE_TIPO

class TestGenerarCodigo():
    def testCodeGenerationCodeWithOneWord(self):
        assert generar_codigo('Dunlin') ==  'DUNL'
        assert generar_codigo('Dovekie') == 'DOVE'
        assert generar_codigo('Ou') == 'OU'
        assert generar_codigo('Gadwall') == 'GADW'

    def testCodeGenerationCodeWithTwoWord(self):
        assert generar_codigo('American Wigeon') == 'AMWI'
        assert generar_codigo('Eastern Meadowlark') == 'EAME'

    def testCodeGenerationCodeWithThreeWordAndDash(self):
        assert generar_codigo('Eastern Screech-Owl') == 'EASO'
        assert generar_codigo('Western Wood-Pewee') == 'WEWP'
        assert generar_codigo('Red-tailed Hawk') == 'RTHA'
        assert generar_codigo('White-winged Crossbill') == 'WWCR'
        assert generar_codigo('Whip-poor-will') == 'WPWI'

    def testCodeGenerationCodeWithFourWordAndDash(self):
        assert generar_codigo('Black-crowned Night-Heron') == 'BCNH'
        assert generar_codigo('American Swallow-tailed Kite') == 'ASTK'
        assert generar_codigo('Northern Saw-whet Owl') == 'NSWO'

    def testCodeGenerationMoreThanOneWordSeparatedByDashes(self):
        assert generar_codigo('Dunlin-SDf') == 'DUSD'
        assert generar_codigo('Dunlin-SDf-ASD') == 'DSAS'
        assert generar_codigo('Dunlin-SDf-ASD-ASD') == 'DSAA'

    def testCodeGenerationMoreThanOneWordNonSeparatedByDashes(self):
        assert generar_codigo('Dunlin SDf') == 'DUSD'
        assert generar_codigo('Dunlin SDf ASD') == 'DSAS'
        assert generar_codigo('Dunlin SDf ASD ASD') == 'DSAA'

    def testCodeGenerationWithMalformedStrings(self):
        assert generar_codigo('23243!@#$%') == '2324'
        assert generar_codigo('23243-!@#$%') == '23!@'
        assert generar_codigo('23-243-!@#-$%') == '22!$'
        assert generar_codigo('232-43-!@#$%') == '24!@'

    def testCodeGenerationWithAnEmptyString(self):
        with pytest.raises(ValueError, match=ERROR_DE_STRING_VACIO):
            generar_codigo('')
        with pytest.raises(ValueError, match=ERROR_DE_STRING_VACIO):
            generar_codigo(' ')
        with pytest.raises(ValueError, match=ERROR_DE_STRING_VACIO):
            generar_codigo('  ')

    def testCodeGenerationWithInvalidParameterType(self):
        with pytest.raises(ValueError, match=ERROR_DE_TIPO):
            generar_codigo(12345)
        with pytest.raises(ValueError, match=ERROR_DE_TIPO):
            generar_codigo(True)
        with pytest.raises(ValueError, match=ERROR_DE_TIPO):
            generar_codigo([])
        with pytest.raises(ValueError, match=ERROR_DE_TIPO):
            generar_codigo({})

    def testCodeGenerationWithEmptyParameter(self):
        with pytest.raises(ValueError, match=ERROR_DE_STRING_VACIO):
            generar_codigo()
        with pytest.raises(ValueError, match=ERROR_DE_TIPO):
            generar_codigo(None)
