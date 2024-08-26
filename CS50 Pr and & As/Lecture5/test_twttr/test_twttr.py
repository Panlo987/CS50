from twttr import shorten

def testNoVowels():
    assert shorten('hll wrld') == 'hll wrld'
def testWhiteSpace():
    assert shorten(' hello world ') == ' hll wrld '
def testNoInput():
    assert shorten('') == ''
def testUpper():
    assert shorten('HeLlO WOrld') == 'HLl Wrld'
def testPunctuation():
    assert shorten('Hello, world') == 'Hll, wrld'
def testNumbers():
    assert shorten('Comp Sci 50') == 'Cmp Sc 50'
