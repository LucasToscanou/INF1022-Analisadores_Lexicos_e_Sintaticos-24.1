import ply.lex as lex

# List of token names . This is always required
tokens = ('NUMBER', 'PLUS', 'MINUS')
# Regular expression rules for simple tokens
t_PLUS = r'\+ '
t_MINUS = r'-'
# A regular expression rule with some action code
def t_NUMBER ( t ):
    r'\d+'
    t.value = int( t.value )
    return t

# A string containing ignored characters ( spaces and tabs )
t_ignore = ' \t'

# Define a rule so we can track line numbers
def t_newline (t):
    r'\n+'
    t.lexer.lineno += len( t.value )

# Error handling rule
def t_error ( t ):
    print ("Caractere invalido : '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()



# Entrada
data = "42 + 17"
# Entregue a entrada para o lexer e execute
lexer . input ( data )
# Iteracao sobre os tokens encontrados (com while )
while True :
    tok = lexer . token ()
    if not tok :
        break # No more input
    print ( tok )
    print (" type : "+str( tok . type ) , "| value : "+str( tok . value ) , "| lineno : "+str
    ( tok . lineno ) , "| lexpox : "+str( tok .
    lexpos ) )

    # Iteracao sobre os tokens encontrados (com for)
    for tok in lexer :
        print ( tok )
        print (" type : "+str( tok . type ) , "| value : "+str( tok . value ) , "| lineno : "+str
        ( tok . lineno ) , "| lexpox : "+str( tok .
        lexpos ) )
