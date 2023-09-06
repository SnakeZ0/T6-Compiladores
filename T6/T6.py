# Trabalho feito por Gabriel Mansano Pires, RA: 790951, e Pedro Freire Baleeiro, RA: 790984.
# Para a disciplina de Compiladores 2023/1, ofertada pelo professor Daniel Lucrédio

import subprocess
from lexer import *
from generator import *
from parser import *
import sys

def main():
    print("PTypescript")

    if len(sys.argv) != 2:
        sys.exit("Erro: Compilador precisa de um arquivo source como argumento.")
    
    source_file = sys.argv[1]

    with open(source_file, 'r') as inputFile:
        source = inputFile.read()

    # Inicializa o lexer, o generator e o parser
    lexer = Lexer(source)
    generator = Generator("out.js")
    parser = Parser(lexer, generator)

    # Parcer é inicializado.
    parser.programa() 
    
    # Escreve a saída para o arquivo.
    generator.writeFile() 
    print("Compilacao Finalizada.")

if __name__ == "__main__":
    main()
    subprocess.run(["node", "out.js"])