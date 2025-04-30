import ply . lex as lex

tokens = ('ID' ,)

def t_ID ( t ):
    r'[a-zA -Z][a-zA -Z0 -9]*'
    return t

t_ignore = ' \t'

def t_newline ( t ):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error ( t ):
    print ("Caractere invalido : '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()
# Tabela de simbolos para armazenar as palavras e suas contagens
TS = {}

# Funcao para adicionar uma palavra na tabela de simbolos
def coloca_palavra_na_TS(palavra):
    palavra = palavra.lower() # Converte a palavra para minusculas
    if palavra in TS:
        TS[palavra] += 1
    else :
        TS[palavra] = 1

coloca_palavra_na_TS("teste")

# Exibe a tabela de simbolos
print ("Tabela de Simbolos :")
for palavra, ocor in TS.items():
    print (f"{palavra}: {ocor}")

def main ():
    dado = "BLA Esse um exemplo de sequencia de palavras em TS"
    lexer.input(dado)
    while True :
        tok = lexer.token()
        if not tok :
            break
        coloca_palavra_na_TS (tok.value )
    # Exibe a tabela de simbolos
    print (" Tabela de Simbolos :")
    for palavra , ocor in TS . items ():
        print(f"{palavra}: ocor}")

if __name__ == " __main__ ":
    main()
