# ------------------------------------------------------------
# lexer.py
# 
# ------------------------------------------------------------
import ply.lex as lex

# List of token names.
tokens = (
  # KEYWORDS
   'IMPORT',
   'CLASS',
   'INHERITS',
   'PUBLIC',
   'PRIVATE',
   'SEMICOLON',
   'COLON',
   'ID',
   'LSQRBRACKET',
   'RSQRBRACKET',
   'LPAREN',
   'RPAREN',
   'LBRACE',
   'RBRACE',
   'MAIN',
   'OBJECT',

   # # DATA TYPES
   'INTEGER',
   # 'BOOL',
   # 'STRING',
   # 'TRUE',
   # 'FALSE'
   # # OPERATORS 
   # 'PLUS',
   # 'MINUS',
   # 'TIMES',
   # 'DIVIDE',
   # 'MOD',
   # 'TILDA',
   # 'GT',
   # 'LT',
   # 'EQUAL',
   # 'LTEQ',
   # 'GTEQ',
   # 'GETS',
   # 'OR',
   # 'AND',
   # 'NOT',
   # # LOOP AND CONDITIONAL
   # 'IF',
   # 'THEN',
   # 'ELSE',
   # 'FI',
   # 'WHILE',
   # 'LOOP',
   # 'POOL',
   # 'FOR',
   # 'LET',
   # 'IN',
   # 'SELF',
   # 'BREAK',
   # 'CONTINUE',
   # 'ISVOID',
   # 'NEW'
   'PLUS',
   'MINUS',
   'TIMES',
   'DIVIDE'

   )
# reserved Keyword
reserved = {
  'import' : 'IMPORT',
  'class' : 'CLASS',
  'inherits' : 'INHERITS',
  'public' : 'PUBLIC',
  'private' : 'PRIVATE',
  'main' : 'MAIN',
  'Object' : 'OBJECT'

}

# Regular expression rules for simple tokens
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_LBRACE  = r'\{'
t_RBRACE  = r'\}'
t_LSQRBRACKET = r'\['
t_RSQRBRACKET = r'\]'


# A regular expression rule with some action code

# REgular expression for Identifier
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'ID')    # Check for reserved words
    return t
# regular expression for integer
def t_INTEGER(t):
    r'\d+'
    t.value = int(t.value)    
    return t

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()
# Test it out
data = '''
import abara
main
[43]
3 + 4 * 10}
  + -20 *2
'''
# data="( 3 + 2 )"

# Give the lexer some input
lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok: 
        break      # No more input
    print(tok)