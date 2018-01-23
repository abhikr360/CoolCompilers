# ------------------------------------------------------------
# lexer.py
# 
# ------------------------------------------------------------
import ply.lex as lex
from ply.lex import TOKEN

# List of token names.
######                        TRY keeping exactly same order across all
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
   'PERIOD',
   'MAIN',
   'OBJECT',

   # # DATA TYPES
   'CLASS_TYPE'
   'INTEGER',
   'INTEGER_TYPE',
   'BOOL_TYPE',
   'STRING_TYPE',
   'SELF_TYPE',
   'STRING',
   'TRUE',
   'FALSE',
   'MOD',
   'TILDA',
   'GT',
   'LT',
   'EQUAL',
   'LTEQ',
   'GTEQ',
   'GETS',
   'OR',
   'AND',
   'NOT',
   # # LOOP AND CONDITIONAL
   'IF',
   'THEN',
   'ELSE',
   'FI',
   'WHILE',
   'LOOP',
   'POOL',
   'FOR',
   'LET',
   'IN',
   'SELF',
   'BREAK',
   'CONTINUE',
   'ISVOID',
   'NEW',
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
  'Object' : 'OBJECT',
  'while' : 'WHILE',
  'loop' : 'LOOP',
  'pool' : 'POOL',
  'for' : 'FOR',
  'let' : 'LET',
  'in' : 'IN',
  'self' : 'SELF',
  'break' : 'BREAK',
  'continue' : 'CONTINUE',
  'isvoid' : 'ISVOID',
  'new' : 'NEW',
  'if' : 'IF',
  'then' : 'THEN',
  'else' : 'ELSE',
  'fi' : 'FI',
  'and' : 'AND',
  'not' : 'NOT',
  'or' : 'OR',
  'Int' : 'INTEGER_TYPE',
  'Bool' : 'BOOL_TYPE',
  'String' : 'STRING_TYPE',
  'TRUE' : 'TRUE',
  'FALSE' : 'FALSE',
  'SELF_TYPE' : 'SELF_TYPE'

}

# Regular expression rules for simple tokens
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_MOD = r'%'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_LBRACE  = r'\{'
t_RBRACE  = r'\}'
t_LSQRBRACKET = r'\['
t_RSQRBRACKET = r'\]'
t_SEMICOLON = r';'
t_COLON = r':'
t_TILDA = r'~'
t_GT = r'>'
t_LT = r'<'
t_EQUAL = r'='
t_LTEQ = r'<='
t_GTEQ = r'>='
t_GETS = r'<-'
t_PERIOD = r'\.'



# A regular expression rule with some action code


# REgular expression for Identifier
def t_ID(t):
    r'[a-z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'ID')    # Check for reserved words
    return t

# Regex for Class Name
def t_CLASS_TYPE(t):
  r'[A-Z][a-zA-Z_0-9]*'
  t.type = reserved.get(t.value, 'CLASS_TYPE')
  return t

# regular expression for String
def t_STRING(t):
    r"^\"*\"$"
    t.value = str(t.value)
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


lexer = lex.lex()

data = '''
class Main inherits IO {
  x : Int;
   main(): SELF_TYPE {
  out_string("Hello World\n")
  a<-23.;
  let a in Int:xyz;
   };
};
'''

# Give the lexer some input
lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok: 
        break
    print(tok)