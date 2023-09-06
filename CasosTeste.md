# Exemplos de códigos para teste do compilador de PTypescript
## Código exemplo funcional
```
NUM foo =  3+4
CONSTNUM co 3
CONSTSTR cs "gg"
STR str="variavel string "
SE co > 0 ENTAO
    ENQUANTO foo<8 REPETE
        NUM foo=foo+1
        IMPRIME "sim!"
        IMPRIME str
    FIMENQUANTO
FIMSE
IMPRIME "SAIU"
```
## Códigos exemplos da análises de erros
testeErro1.txt - Atribuir um valor de tipo diferente da variavel:
```
NUM foo =  3+4
CONSTNUM co 3
CONSTSTR cs "gg"
STR str="variavel string "
SE co > 0 ENTAO
    ENQUANTO foo<8 REPETE
        STR foo="foo+1"
        IMPRIME "sim!"
        IMPRIME str
    FIMENQUANTO
FIMSE
IMPRIME "SAIU"
```

testeErro2.txt - Tentar atribuir um novo valor a uma constante:
```
NUM foo =  3+4
CONSTNUM co 3
CONSTSTR cs "gg"
STR str="variavel string "
SE co > 0 ENTAO
    ENQUANTO foo<8 REPETE
        NUM foo=foo+1
        CONSTSTR cs "gg"
        IMPRIME "sim!"
        IMPRIME str
    FIMENQUANTO
FIMSE
IMPRIME "SAIU"
```

testeErro3.txt - Tentar criar uma variavel com o mesmo nome de outra:
```
NUM foo =  3+4
CONSTNUM co 3
CONSTSTR cs "gg"
STR str="variavel string "
SE co > 0 ENTAO
    ENQUANTO foo<8 REPETE
        STR foo="foo+1"
        CONSTSTR cs "gg"
        IMPRIME "sim!"
        IMPRIME str
    FIMENQUANTO
FIMSE
IMPRIME "SAIU"
```

testeErro4.txt - Tentar usar uma variavel não declarada:
```
NUM foo =  3+4
CONSTNUM co 3
CONSTSTR cs "gg"
STR str="variavel string "
SE nexiste > 0 ENTAO
    ENQUANTO foo<8 REPETE
        STR foo="foo+1"
        CONSTSTR cs "gg"
        IMPRIME "sim!"
        IMPRIME str
    FIMENQUANTO
FIMSE
IMPRIME "SAIU"
```
