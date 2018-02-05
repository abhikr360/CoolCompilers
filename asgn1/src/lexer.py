#!/usr/bin/env python

# -----------------------\ n-------------------------------------
# lexer.py
# 
# ------------------------------------------------------------
import ply.lex as lex
from ply.lex import TOKEN
import sys
from table import Table

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
   'PERIOD',
   'MAIN',
   'OBJECT',

   # # DATA TYPES
   'CLASS_TYPE',
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
   'DIVIDE',
   'COMMA',

   # At
   'AT'

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
  'SELF_TYPE' : 'SELF_TYPE',
  'CLASS_TYPE' : 'CLASS_TYPE'

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
t_COMMA = r','
t_AT = r'@'


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

#ssion for integer
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
    print("Illegal character '%s' at line %d" % (t.value[0],t.lineno))
    t.lexer.skip(1)
    print("Exiting due to lexing error.....Abort!")
    exit()

states = (
   ('STRING','exclusive'),
   ('COMMENT','exclusive'),
)

def t_start_string(t): # try removing start -> begin
    r'\"'
    t.lexer.push_state("STRING")
    t.lexer.string_backslashed = False
    t.lexer.stringbuffer=''

def t_start_comment(t):
    r'\(\*'
    t.lexer.push_state("COMMENT")
    # t.lexer.no_comment = t.lexer.no_comment + 1

def t_COMMENT_end(t):
    r'\*\)'
    t.lexer.pop_state()

def t_COMMENT_anything(t):
    r'.|\n'
    # r'[^(\*\))]'


t_COMMENT_ignore=""

def t_COMMENT_error(t):
    print("Illegal COMMENT in line no. {0}, character {1}".format(t.lineno,t.value[0]))
    


def t_STRING_end(t):
  r'\"'
  if t.lexer.string_backslashed :
    t.lexer.stringbuffer += '"'
    t.lexer.string_backslashed = False
  else:
    t.lexer.pop_state()
    t.lexer.stringbuffer += ''
    t.value = t.lexer.stringbuffer
    t.type = "STRING"
    return t

def t_STRING_anything(t):
    r'.'
    if(t=='\n'):

      t.lexer.lineno += 1
      if not t.lexer.string_backslashed:
        dummy=0
      else:
        t.lexer.string_backslashed = False
    else:
      if t.lexer.string_backslashed:
        if t.value == 'b':
          t.lexer.stringbuffer += '\b'
        elif t.value == 'n':
          t.lexer.stringbuffer += '\n'
        elif t.value == 't':
          t.lexer.stringbuffer += '\t'
        elif t.value == '\\':
          t.lexer.stringbuffer += '\\'
        elif t.value == 'f':
          t.lexer.stringbuffer += '\f'
        else:
          t.lexer.stringbuffer += t.value
        t.lexer.string_backslashed = False
      else:

        if t.value != '\\':
            t.lexer.stringbuffer += t.value
        else:
          t.lexer.string_backslashed = True


t_STRING_ignore = ''

def t_STRING_error(t):
    print("Illegal character in line no. {0}, character {1}".format(t.lineno,t.value[0]))

lexer = lex.lex()

input_file = sys.argv[1]
with open(input_file) as file:
    data = file.read()

# Give the lexer some input
lexer.input(data)

collect = []
# Tokenize
while True:
    tok = lexer.token()
    if not tok: 
        break
    # print(tok)

#TOKEN HAS TYPE AND VALUE

    collect.append(tok)

print_list = []

for single_token in tokens:
	print_list_element = []
	token_list = []
	token_str = ""
	token_count = 0
	for lex_tokens in collect:
		if(single_token == lex_tokens.type):
			token_count = token_count + 1
			if(lex_tokens.value not in token_list):
				token_list.append(lex_tokens.value)
				if(token_count > 1):
					token_str = token_str + '                        '
				token_str = token_str + str(lex_tokens.value)
				#print(token_str)
	if(token_count == 0):
		continue
	if(single_token in reserved.values()):
		print_list.append(["Keyword_"+single_token, str(token_count), token_str])
	else:
		print_list.append([single_token, str(token_count), token_str])
	# print(single_token + ':' + str(token_count))
	# print(str(token_list))
	# print (single_token in reserved.values())
	# print("--------------------------------------------")

#print(print_list)
# print("------------------------------------------------------")

header = Table([["Tokens", "Occurences", "Lexemes"]],20,True)
print(header)
print("------------------------------------------------------")

table = Table(print_list, 20, True)

print(table)
