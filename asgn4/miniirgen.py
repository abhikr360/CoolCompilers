#!/usr/bin/env python

import ply.yacc as yacc
import sys
from lexer import tokens
import tree as TREE

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

def p_start(p):
  'start : program'
  rule.append(0)
  p[0]=TREE.Start(code=p[1].code)
  for a in p[0].code:
    print(a)

def p_program_with_imports(p):
  'program : imports classes'
  rule.append(1)

  # Import Unimplemented
  p[0]=TREE.ProgramImport(code=p[2].code)

def p_program(p):
  'program : classes'
  rule.append(2)
  p[0]=TREE.Program(code=p[1].code)

def p_imports_multiple(p):
  'imports : imports IMPORT ID SEMICOLON'
  rule.append(3)
  # Unimplemented

def p_imports(p):
  'imports : IMPORT ID SEMICOLON'
  rule.append(4)
  # Unimplemented


def p_classes_multiple(p):
  'classes : classes class SEMICOLON'
  rule.append(5)

  code=p[1].code
  code.extend(p[2].code)
  p[0]=TREE.Classes(code=code)

  # CLASS Unimplemented

def p_classes(p):
  'classes : class SEMICOLON'
  rule.append(6)

  p[0]=TREE.Classes(code=p[1].code)

  # CLASS Unimplemented



def p_class_with_inheritance_with_features_list(p):
    'class : CLASS CLASS_TYPE INHERITS CLASS_TYPE LBRACE features_list RBRACE'
    rule.append(7)


    p[0]=TREE.Class(code=p[6].code)

    # CLASS Unimplemented

def p_class_with_features_list(p):
  'class : CLASS CLASS_TYPE LBRACE features_list RBRACE'
  rule.append(8)

  p[0]=TREE.Class(code=p[4].code)

  # CLASS Unimplemented

def p_class_with_features_inheritance(p):
  'class : CLASS CLASS_TYPE INHERITS CLASS_TYPE LBRACE RBRACE'
  rule.append(9)

  # CLASS Unimplemented

def p_class(p):
  'class : CLASS CLASS_TYPE LBRACE RBRACE'
  rule.append(10)

  # CLASS Unimplemented

  #--------------------------------------------  DONE ----------------------------------------------

def p_features_list_mult(p):
  'features_list : features_list feature SEMICOLON'
  rule.append(11)

def p_features_list(p):
  'features_list : feature SEMICOLON'
  rule.append(12)

  code = p[1].code
  code.append('FUNC_RETURN')
  p[0]=TREE.FeatureList(code=code)


def p_feature_with_modifier_with_formal_parameter_list(p):
  'feature : modifier ID LPAREN formal_parameter_list RPAREN COLON type LBRACE expression RBRACE'
  rule.append(13)

def p_feature_with_modifier(p):
  'feature : modifier ID LPAREN RPAREN COLON type LBRACE expression RBRACE'
  rule.append(14)

def p_feature_with_formal_parameter_list(p):
  'feature : ID LPAREN formal_parameter_list RPAREN COLON type LBRACE expression RBRACE'
  rule.append(15)

def p_feature(p):
  'feature : ID LPAREN RPAREN COLON type LBRACE expression RBRACE'
  rule.append(16)
  code=['FUNC_LABEL,'+p[1]]
  # print(type(code), type(p[7].code), p[7])
  code.extend(p[7].code)
  p[0]=TREE.Feature(code=code)


def p_feature_modifier_formal(p):
  'feature : modifier formal'
  rule.append(17)

def p_feature_formal(p):
  'feature : formal'
  rule.append(18)

def p_modifier_public(p):
  'modifier : PUBLIC'
  rule.append(19)

def p_modifier_private(p):
  'modifier : PRIVATE'
  rule.append(20)

def p_type_class_type(p):
  'type : CLASS_TYPE'
  rule.append(21)

def p_type_integer_type(p):
  'type : INTEGER_TYPE'
  rule.append(22)

def p_type_bool_type(p):
  'type : BOOL_TYPE'
  rule.append(23)

def p_type_string_type(p):
  'type : STRING_TYPE'
  rule.append(24)

def p_type_object(p):
  'type : OBJECT'
  rule.append(25)

def p_type_self_type(p):
  'type : SELF_TYPE'
  rule.append(26)
  # print(p[0], p[1])

def p_formal_parameter_list_many(p):
  'formal_parameter_list : formal_parameter_list COMMA formal_parameter'
  rule.append(27)

def p_formal_parameter_list(p):
  'formal_parameter_list : formal_parameter'
  rule.append(28)

def p_formal_parameter(p):
  'formal_parameter : ID COLON type'
  rule.append(29)

def p_formal_parameter_arr(p):
  'formal_parameter : ID LSQRBRACKET RSQRBRACKET COLON type'
  rule.append(30)

def p_formal_with_assign(p):
  'formal : ID COLON type GETS expression'
  rule.append(31)

def p_formal(p):
  'formal : ID COLON type'
  rule.append(32)

def p_formal_arr(p):
  'formal : ID COLON type LSQRBRACKET RSQRBRACKET'
  rule.append(33)


def p_expression_block_expression(p):
  'expression : block_expression'
  rule.append(34)


def p_block_expression(p):
  'block_expression : LBRACE block_list RBRACE'
  rule.append(35)

def p_block_list_many(p):
  'block_list : block_list expression SEMICOLON'
  rule.append(36)

def p_block_list(p):
  'block_list : expression SEMICOLON'
  rule.append(37)


def p_expression_assign(p):
  'expression : ID GETS expression'
  rule.append(38)

def p_expression_assign_arr(p):
  'expression : ID LSQRBRACKET expression RSQRBRACKET GETS expression'
  rule.append(39)

def p_expression_function_call_with_arguments_2(p):
  'expression : ID LPAREN argument_list RPAREN'
  rule.append(40)
  code = p[3].code
  code.append('FUNC_CALL,'+p[1])
  p[0]=TREE.FunctionCall(code=code)


def p_expression_function_call_2(p):
  'expression : ID LPAREN RPAREN'
  rule.append(41)


def p_argument_list(p):
  'argument_list : expression'
  rule.append(42)

  code = ['FUNC_PARAM,{}'.format(p[1].place)]
  p[0]=TREE.ArgumentList(code=code)

def p_argument_list_many(p):
  'argument_list : argument_list COMMA expression'
  rule.append(43)


def p_expression_plus(p):
  'expression : expression PLUS expression'
  rule.append(44)

def p_expression_minus(p):
  'expression : expression MINUS expression'
  rule.append(45)

def p_expression_times(p):
  'expression : expression TIMES expression'
  rule.append(46)

def p_expression_divide(p):
  'expression : expression DIVIDE expression'
  rule.append(47)

def p_expression_mod(p):
  'expression : expression MOD expression'
  rule.append(48)

def p_expression_lt(p):
  'expression : expression LT expression'
  rule.append(49)

def p_expression_gt(p):
  'expression : expression GT expression'
  rule.append(50)

def p_expression_lteq(p):
  'expression : expression LTEQ expression'
  rule.append(51)

def p_expression_gteq(p):
  'expression : expression GTEQ expression'
  rule.append(52)

def p_expression_equal(p):
  'expression : expression EQUAL expression'
  rule.append(53)

def p_expression_or(p):
  'expression : expression OR expression'
  rule.append(54)

def p_expression_and(p):
  'expression : expression AND expression'
  rule.append(55)

def p_expression_not(p):
  'expression : NOT expression'
  rule.append(56)

def p_expression_tilda(p):
  'expression : TILDA expression'
  rule.append(57)

def p_expression_paren(p):
  'expression : LPAREN expression RPAREN'
  rule.append(58)

def p_expression_self(p):
  'expression : SELF'
  rule.append(59)

def p_expression_id(p):
  'expression : ID'
  rule.append(60)

def p_expression_arr(p):
  'expression : ID LSQRBRACKET expression RSQRBRACKET'
  rule.append(61)

def p_expression_integer(p):
  'expression : INTEGER'
  rule.append(62)

def p_expression_string(p):
  'expression : STRING'
  rule.append(63)
  p[0] = TREE.Expression(code=[], place=p[1], datatype='STRING')

def p_expression_true(p):
  'expression : TRUE'
  rule.append(64)

def p_expression_false(p):
  'expression : FALSE'
  rule.append(65)

def p_expression_break(p):
  'expression : BREAK'
  rule.append(66)

def p_expression_continue(p):
  'expression : CONTINUE'
  rule.append(67)

def p_expression_function_call_with_arguments(p):
  'expression : expression PERIOD ID LPAREN argument_list RPAREN'
  rule.append(68)

def p_expression_function_call(p):
  'expression : expression PERIOD ID LPAREN RPAREN'
  rule.append(69)

def p_expression_new(p):
  'expression : NEW type'
  rule.append(70)

def p_expression_isvoid(p):
  'expression : ISVOID expression'
  rule.append(71)

def p_expression_let_expression(p):
  'expression : let_expression'
  rule.append(72)

def p_let_expression(p):
  'let_expression : LET formal IN expression TEL'
  rule.append(73)

# Nested Lets

def p_expression_at_function_with_arguments(p):
  'expression : expression AT CLASS_TYPE PERIOD ID LPAREN argument_list RPAREN'
  rule.append(74)

def p_expression_at_function(p):
  'expression : expression AT CLASS_TYPE PERIOD ID LPAREN RPAREN'
  rule.append(75)


def p_expression_if_then_else(p):
  'expression : if_then_else'
  rule.append(76)

def p_if_then_else(p):
  'if_then_else : IF expression THEN expression ELSE expression FI'
  rule.append(77)

def p_expression_while(p):
  'expression : while'
  rule.append(78)

def p_while(p):
  'while : WHILE expression LOOP expression POOL'
  rule.append(79)

def p_expression_for(p):
  'expression : for'
  rule.append(80)

def p_for(p):
  'for : FOR LPAREN expression SEMICOLON expression SEMICOLON expression RPAREN LOOP expression POOL'
  rule.append(81)





def p_error(p):
  """Error rule for Syntax Errors handling and reporting."""
  print("-------------------------- Error ---------------------------------")
  if p is None:
    print("Error! Unexpected end of input!")
  else:
    error = "Syntax error! Line: {}, position: {}, character: {}, type: {}".format(p.lineno, p.lexpos, p.value, p.type)
    print(error)
    print type(p.type)

parser  = yacc.yacc()


# f = open(sys.argv[1], 'r')
# print(f.read())


input_file = 'test.cl'
with open(input_file) as file:
    data = file.read()
parser.parse(data)
print(rule)