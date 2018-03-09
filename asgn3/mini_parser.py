#!/usr/bin/env python

import ply.yacc as yacc
import sys
from lexer import tokens

precedence = (
        ('right', 'GETS'),
        ('left', 'OR'),
        ('left', 'AND'),
        ('right', 'NOT'),
        ('nonassoc', 'LTEQ', 'GTEQ', 'LT', 'GT', 'EQUAL'),
        ('left', 'PLUS', 'MINUS'),
        ('left', 'TIMES', 'DIVIDE', 'MOD'),
        ('right', 'ISVOID'),
        ('right', 'TILDA'),
        ('left', 'AT'),
        ('left', 'PERIOD')
    )

rule = []


def p_program(p):
  'program : classes'
  rule.append(2)

def p_classes(p):
  'classes : class SEMICOLON'
  rule.append(6)

# def p_class_with_inheritance_with_features_list(p):
#   'class : CLASS CLASS_TYPE INHERITS CLASS_TYPE LBRACE RBRACE'
#   rule.append(7)


def p_class_with_inheritance_with_features_list(p):
    'class : CLASS CLASS_TYPE INHERITS CLASS_TYPE LBRACE features_list RBRACE'
    rule.append(7)

def p_features_list(p):
  'features_list : feature SEMICOLON'
  rule.append(12)

def p_feature(p):
    'feature : ID LPAREN RPAREN COLON type LBRACE expression RBRACE'
    rule.append(16)


def p_type_self_type(p):
  'type : SELF_TYPE'
  rule.append(78)

def p_expression_function_call_with_arguments_2(p):
  'expression : ID LPAREN argument_list RPAREN'
  rule.append(79)

def p_argument_list(p):
  'argument_list : expression'
  rule.append(68)


def p_expression_string(p):
  'expression : STRING'
  rule.append(62)

def p_error(p):
  """Error rule for Syntax Errors handling and reporting."""
  if p is None:
    print("Error! Unexpected end of input!")
  else:
    error = "Syntax error! Line: {}, position: {}, character: {}, type: {}".format(p.lineno, p.lexpos, p.value, p.type)

parser  = yacc.yacc()


# f = open(sys.argv[1], 'r')
# print(f.read())


input_file = sys.argv[1]
with open(input_file) as file:
    data = file.read()

parser.parse(data)
# f.close()
print(rule)