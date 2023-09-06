import sys
from lexer import *

# o objeto Parser rastreia o token atual, verifica se o código corresponde à gramática e gera o código ao longo da execução
class Parser:
    def __init__(self, lexer, generator):
        self.lexer = lexer
        self.generator = generator

        self.simbolos = set()
        self.constsnum = set()    
        self.constsstring = set() 
        self.strings = set() 

        self.TokenAtual = None
        self.checaToken = None
        self.proximoToken()
        self.proximoToken()   

    def checkToken(self, kind):
        return kind == self.TokenAtual.kind

    def match(self, kind):
        if not self.checkToken(kind):
            self.abort("1 Esperado -"+self.TokenAtual.text +"-"+ kind.name + ", recebeu " + self.TokenAtual.kind.name)
        self.proximoToken()

    def proximoToken(self):
        self.TokenAtual = self.checaToken
        self.checaToken = self.lexer.pegaToken()

    def ehOperadorComparacao(self):
        return self.checkToken(TokenTipo.MAISQUE) or self.checkToken(TokenTipo.MAISIGUAL) or self.checkToken(TokenTipo.MENOSQUE) or self.checkToken(TokenTipo.MENOSIGUAL) or self.checkToken(TokenTipo.IGUALIGUAL) or self.checkToken(TokenTipo.DIFERENTE)

    def abort(self, mensagem):
        sys.exit("Erro! " + mensagem)


    def programa(self):
        
        while self.checkToken(TokenTipo.NOVALINHA):
            self.proximoToken()

        while not self.checkToken(TokenTipo.EOF):
            self.declaracao()

#Confere e trata os tipos de token, contendo a logica de cada operação
    def declaracao(self):

        #confere se o que foi passado é uma string ou uma variavel, pois no js o tratamento é diferente
        if self.checkToken(TokenTipo.IMPRIME):
            self.proximoToken()

            if self.checkToken(TokenTipo.STRING):
                self.generator.genLine("console.log(\" \\n" + self.TokenAtual.text + "\")")
                self.proximoToken()

            else:
                self.generator.gen("console.log(`\\n${")
                self.expressao()
                self.generator.genLine("}`);")

        #O se é feito com fim-se e não da pra ter dois então para um se
        elif self.checkToken(TokenTipo.SE):
            self.proximoToken()
            self.generator.gen("if(")
            self.comparacao()

            self.match(TokenTipo.ENTAO)
            self.nl()
            self.generator.genLine("){")

            while not self.checkToken(TokenTipo.FIMSE):
                self.declaracao()

            self.match(TokenTipo.FIMSE)
            self.generator.genLine("}")

        #assim como o se ele tem um fimenquanto
        elif self.checkToken(TokenTipo.ENQUANTO):
            self.proximoToken()
            self.generator.gen("while(")
            self.comparacao()

            self.match(TokenTipo.REPETE)
            self.nl()
            self.generator.genLine("){")

            while not self.checkToken(TokenTipo.FIMENQUANTO):
                self.declaracao()

            self.match(TokenTipo.FIMENQUANTO)
            self.generator.genLine("}")
        
        #variavel numerica
        elif self.checkToken(TokenTipo.NUM):
            self.proximoToken()
            if self.TokenAtual.text in self.constsnum or self.TokenAtual.text in self.constsstring:
                self.abort("2 Nao pode atribuir um valor para a constante: " + self.TokenAtual.text)
            
            elif self.TokenAtual.text in self.strings:
                self.abort("3 Nao pode atribuir um numero para a string: " + self.TokenAtual.text)
                
            if self.TokenAtual.text not in self.simbolos:

                self.simbolos.add(self.TokenAtual.text)
                self.generator.headerLine("let " + self.TokenAtual.text + ";")

            self.generator.gen(self.TokenAtual.text + " = ")
            self.match(TokenTipo.IDENT)
            self.match(TokenTipo.IGUAL)
            if self.checkToken(TokenTipo.STRING):
                self.abort("4 Nao pode atribuir uma string para um numero: " + self.TokenAtual.text)
            
            self.expressao()
            self.generator.genLine(";")

        #variavel string
        elif self.checkToken(TokenTipo.STR):
            self.proximoToken()
            if self.TokenAtual.text in self.constsnum or self.TokenAtual.text in self.constsstring:
                self.abort("5 Nao pode atribuir um valor para a constante: " + self.TokenAtual.text)
                
            elif self.TokenAtual.text in self.simbolos:
                self.abort("6 Nao pode atribuir uma string para um numero: " + self.TokenAtual.text)
            elif self.TokenAtual.text not in self.strings:
                self.simbolos.add(self.TokenAtual.text)
                self.generator.headerLine("let " + self.TokenAtual.text + ";")

            self.generator.gen(self.TokenAtual.text + " = ")
            self.match(TokenTipo.IDENT)
            self.match(TokenTipo.IGUAL)
            if self.checkToken(TokenTipo.NUMERO):
                self.abort("7 Nao pode atribuir um numero para a string: " + self.TokenAtual.text)
            
            self.expressao()
            self.generator.genLine(";")

        #constante numerica
        elif self.checkToken(TokenTipo.CONSTNUM):
            self.proximoToken()
            if self.TokenAtual.text in self.simbolos or self.TokenAtual.text in self.strings:
                self.abort("8 Variavel ja existe: " + self.TokenAtual.text)
            if self.TokenAtual.text in self.constsnum or self.TokenAtual.text in self.constsstring:
                self.abort("9 Constante ja existe: " + self.TokenAtual.text)
            self.constsnum.add(self.TokenAtual.text)
            self.generator.gen("const "+self.TokenAtual.text + " = ")
            self.match(TokenTipo.IDENT)
            if self.checkToken(TokenTipo.STRING):
                self.abort("10 Nao pode atribuir uma string constante para um numero constante: " + self.TokenAtual.text)

            self.expressao()
            self.generator.genLine(";")

        #constante string
        elif self.checkToken(TokenTipo.CONSTSTR):
            self.proximoToken()
            if self.TokenAtual.text in self.simbolos or self.TokenAtual.text in self.strings:
                self.abort("11 Variavel ja existe: " + self.TokenAtual.text)
            if self.TokenAtual.text in self.constsnum or self.TokenAtual.text in self.constsstring:
                self.abort("12 Constante ja existe: " + self.TokenAtual.text)
            self.constsstring.add(self.TokenAtual.text)
            self.generator.gen("const "+self.TokenAtual.text + "= ")
            self.match(TokenTipo.IDENT)
            if self.checkToken(TokenTipo.NUMERO):
                self.abort("13 Nao pode atribuir um numero constante para uma string constante: " + self.TokenAtual.text)

            self.expressao()
            self.generator.genLine("\n")

        #é para receber uma entrada
        elif self.checkToken(TokenTipo.ENTRADA):
            self.proximoToken()
            """ for i in self.constsnum or self.TokenAtual.text in self.constsstring:
                print(i)
                print(self.TokenAtual) """
            if self.TokenAtual in self.constsnum or self.TokenAtual.text in self.constsstring:
                self.abort("14 Nao pode atribuir um valor para a constante: " + self.TokenAtual.text)
            if self.TokenAtual.text not in self.simbolos:
                self.simbolos.add(self.TokenAtual.text)
                self.generator.headerLine("let " + self.TokenAtual.text + "=")

            text=("parseInt(prompt())")
            self.generator.genLine(self.TokenAtual.text + " = "+ text)
            self.match(TokenTipo.IDENT)

        else:
            self.abort("15 declaração invalida em " + self.TokenAtual.text + " (" + self.TokenAtual.kind.name + ")")

        self.nl()

    # Define o que é uma comparação na gramática
    def comparacao(self):
        self.expressao()
        if self.ehOperadorComparacao():
            self.generator.gen(self.TokenAtual.text)
            self.proximoToken()
            self.expressao()
        while self.ehOperadorComparacao():
            self.generator.gen(self.TokenAtual.text)
            self.proximoToken()
            self.expressao()

    # Define o que é uma expressão na gramática
    def expressao(self):
        self.termo()
        while self.checkToken(TokenTipo.MAIS) or self.checkToken(TokenTipo.MENOS):
            self.generator.gen(self.TokenAtual.text)
            self.proximoToken()
            self.termo()

    # Define o que é um termo na gramática
    def termo(self):
        self.unario()
        while self.checkToken(TokenTipo.VEZES) or self.checkToken(TokenTipo.BARRA):
            self.generator.gen(self.TokenAtual.text)
            self.proximoToken()
            self.unario()

    # Define o que é um termo unário na gramática
    def unario(self):
        # Operação unária opcional +/-
        if self.checkToken(TokenTipo.MAIS) or self.checkToken(TokenTipo.MENOS):
            self.generator.gen(self.TokenAtual.text)
            self.proximoToken()        
        self.primario()

    # Define o que é um termo primário na gramática
    def primario(self):
        if self.checkToken(TokenTipo.NUMERO): 
            self.generator.gen(self.TokenAtual.text)
            self.proximoToken()
        elif self.checkToken(TokenTipo.STRING):
            self.generator.gen("\""+self.TokenAtual.text+"\"")
            self.proximoToken()
        elif self.checkToken(TokenTipo.IDENT):
            if self.TokenAtual.text not in self.simbolos and self.TokenAtual.text not in self.strings and self.TokenAtual.text not in self.constsnum and self.TokenAtual not in self.constsstring:
                self.abort("16 Referenciando variável ou constante antes da atribuição: " + self.TokenAtual.text)
            self.generator.gen(self.TokenAtual.text)
            self.proximoToken()
        else:
            self.abort("17 Token inesperado em " + self.TokenAtual.text)

    # Define o que é um espaço em branco de acordo com a gramática
    def nl(self):
        self.match(TokenTipo.NOVALINHA)
        while self.checkToken(TokenTipo.NOVALINHA):
            self.proximoToken()