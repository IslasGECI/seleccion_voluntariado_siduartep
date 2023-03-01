import sys

import pytest
from seleccion_voluntariado_2023 import (
    generate_code
)


def testCodeGenerationCodeWithOneWord():
    assert generate_code("Dunlin") == "DUNL"
    assert generate_code("Dovekie") == "DOVE"
    assert generate_code("Ou") == "OU"
    assert generate_code("Gadwall") == "GADW"

def testCodeGenerationCodeWithTwoWord():
    assert generate_code("American Wigeon") == "AMWI"
    assert generate_code("Eastern Meadowlark") == "EAME"

def testCodeGenerationCodeWithThreeWordAndDash():
    assert generate_code("Eastern Screech-Owl") == "EASO"
    assert generate_code("Western Wood-Pewee") == "WEWP"
    assert generate_code("Red-tailed Hawk") == "RTHA"
    assert generate_code("White-winged Crossbill") == "WWCR"
    assert generate_code("Whip-poor-will") == "WPWI"

# def testMutation(capsys):
    #sys.stderr.write("-\n")
    #assert captured.out == "- \n"
    #assert captured.err == "XX-XX\n"

def testCodeGenerationCodeWithFourWordAndDash():
    assert generate_code("Black-crowned Night-Heron") == "BCNH"
    assert generate_code("American Swallow-tailed Kite") == "ASTK"
    assert generate_code("Northern Saw-whet Owl") == "NSWO"

def testCodeGenerationMoreThanOneWordSeparatedByDashes():
    assert generate_code("Dunlin-SDf") == "DUSD"
    assert generate_code("Dunlin-SDf-ASD") == "DSAS"
    assert generate_code("Dunlin-SDf-ASD-ASD") == "DSAA"

def testCodeGenerationMoreThanOneWordNonSeparatedByDashes():
    assert generate_code("Dunlin SDf") == "DUSD"
    assert generate_code("Dunlin SDf ASD") == "DSAS"
    assert generate_code("Dunlin SDf ASD ASD") == "DSAA"

def testCodeGenerationWithMalformedStrings():
    assert generate_code("23243!@#$%") == "2324"
    assert generate_code("23243-!@#$%") == "23!@"
    assert generate_code("23-243-!@#-$%") == "22!$"
    assert generate_code("232-43-!@#$%") == "24!@"

def testCodeGenerationWithAnEmptyString():
    with pytest.raises(ValueError, match="^ERROR$"):
        generate_code("")
    with pytest.raises(ValueError, match="^ERROR$"):
        generate_code(" ")
    with pytest.raises(ValueError, match="^ERROR$"):
        generate_code("  ")

def testCodeGenerationWithInvalidParameterType():
    with pytest.raises(ValueError, match="^ERROR$"):
        generate_code(12345)
    with pytest.raises(ValueError, match="^ERROR$"):
        generate_code(True)
    with pytest.raises(ValueError, match="^ERROR$"):
        generate_code([])
    with pytest.raises(ValueError, match="^ERROR$"):
        generate_code({})

def testCodeGenerationWithEmptyParameter():
    with pytest.raises(ValueError, match="^ERROR$"):
        generate_code()
    with pytest.raises(ValueError, match="^ERROR$"):
        generate_code(None)
