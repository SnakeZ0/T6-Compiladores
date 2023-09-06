# PTypescript
Trabalho 6 para a Disciplina de Compiladores 2023/1, ofertada pelo professor Daniel Lucrédio.

Feito por Gabriel Mansano Pires, RA: 790951, e Pedro Freire Baleeiro, RA: 790984.

  Após termos como inspiração a linguagem Typescript, que adiciona tipagem estático, ou seja existe declaração de tipos para as variáveis de forma explícita durante a compilação do código, decidimos criar uma versão similar ao Typescript porém sendo em Português (PT) e daí nasceu o PTypescript!
  
  Assim como o original, o PTypescript também compila para Javascript antes de ser compilado novamente e rodado. Além disso, PTypescript declara variáveis em vez de apenas com "let" também com o seu tipo "NUM" ou "STR" por exemplo. Atribuições de variáveis são feitas com (NUM | STR) {nome variável} = (valor | "cadeia"). O uso de ponto vírgula ao fim de cada linha não é necessário, assim como decidimos pela a utilização de palavras chaves para definir como por exemplo: SE comparacao ENTAO código FIMSE.

  Para maiores explicações da sintaxe e gramática que definem o PTypescript aqui estará disponibilizado um vídeo que explicamos a gramática, passamos por cima das principais partes do código e das análises de erros léxicos, sintáticos e semânticos cobertos.
  
  Link Vídeo: https://drive.google.com/file/d/14Oc0goKii1ELRdkwcIO21151e1j8dBMX/view?usp=drive_link

  (primeiros 4:40 de vídeo apresentamos a ideia e a gramática, após isso aprofundamos um pouco nas partes do código do lexer, parser e principal)

# Para Rodar
Para rodar o nosso compilador da linguagem PTypescript é necessário ter Python baixado, estar no diretório que o T6 está localizado e rodar o seguinte comando:

```
python caminho\T6.py caminho\teste.txt
```
caminho = Path do arquivo

caminho\teste.txt é o exemplo de código da linguagem PTypescript

## Exemplo Código PTypescript
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

## Exemplo Código Typescript normal
```
let foo: number = 3 + 4;
const co: number = 3;
const cs: string  = "gg";
let str: string = "variavel string";
if (co > 0) {
  while (foo < 8) {
    foo += 1;
    console.log("sim!");
    console.log(`${str}`);
  }
}
console.log("SAIU");
```

## Código Javascript gerado em ambos os exemplos
```
let foo;
let str;
foo = 3+4;
const co = 3;
const cs= "gg"
str = "variavel string ";
if(co>0){
while(foo<8){
foo = foo+1;
console.log("sim!")
console.log(`${str}`);
}
}
console.log("SAIU")
```
