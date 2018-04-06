#!/usr/bin/env python

import ply.yacc as yacc
import sys
from lexer import tokens
import tree as TREE
from symtab import *

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

SymbolTables = []
current_symbol_table = [Symtab(parent=None, symtab_type='class', scope_name='GLOBAL')]  #not a list only one symboltable
ClassDict = {}

'''
     TO BE DONE
'''

tempCount=[0]
def newtemp():
  tempCount[0] += 1
  temp_name = 't.' + str(tempCount[0])
  current_symbol_table[0].enter(name = temp_name)
  return temp_name

jumpCount = [0]
def newjump():
  jumpCount[0] += 1
  return 'label.' + str(jumpCount[0]) 

letCount=[0]
def newLet():
  letCount[0] += 1
  return 'LET_' + str(letCount[0])

breaklist=[]

def p_start(p):
  'start : program'
  rule.append(0)

  p[0]=TREE.Start(code=p[1].code)
  t = newtemp()
  print "FUNC_CALL,THE_MAIN_CLASS,"+t
  print "EXIT"
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

def p_class_header_body(p):
  'class : class_header class_body'


  code = p[1].code
  code.extend(p[2].code)
  p[0] = TREE.Class(code=code)



def p_class_header_with_inheritance(p):
  'class_header : CLASS CLASS_TYPE INHERITS CLASS_TYPE'

  new_sym_tab = Symtab(parent=None, symtab_type="CLASS", scope_name=p[2])
  ClassDict[p[2]] = new_sym_tab
  SymbolTables.append(new_sym_tab)
  current_symbol_table[0] = new_sym_tab


  if(p[2]=='Main'):
    pass
    code = ['FUNC_LABEL,THE_MAIN_CLASS']
  else:
    code=["Class header code here with inheritance"]

  p[0] = TREE.ClassHeader(code=code)


def p_class_header(p):
  'class_header : CLASS CLASS_TYPE'

  if(p[2]=='Main'):
    pass
    code = ['FUNC_LABEL,THE_MAIN_CLASS']
  else:
    code=["Class header code here without inheritance"]
  p[0] = TREE.ClassHeader(code=code)

  new_sym_tab = Symtab(parent=None, symtab_type="CLASS", scope_name=p[2])
  ClassDict[p[2]] = new_sym_tab
  current_symbol_table[0] = new_sym_tab

def p_class_body_empty(p):
  'class_body : LBRACE RBRACE'

def p_class_body(p):
  'class_body : LBRACE features_list RBRACE'
  p[0] = TREE.Class(code=p[2].code)

# def p_class_with_inheritance_with_features_list(p):
#   'class : class_header INHERITS CLASS_TYPE LBRACE features_list RBRACE'
#   rule.append(7)

#   newSymboltable = Symtab(parent=None,symtab_type='class',scope_name=p[2])
#   current_symbol_table[0] = newSymboltable
#   print 'entering data in symbol table'
#   p[0]=TREE.Class(code=p[6].code, symtab=newSymboltable)

#   # CLASS, INHERITS Unimplemented

# def p_class_with_features_list(p):
#   'class : CLASS CLASS_TYPE LBRACE features_list RBRACE'
#   rule.append(8)

#   newSymboltable = Symtab(parent=None,symtab_type='class',scope_name=p[2])
#   current_symbol_table[0] = newSymboltable
#   p[0]=TREE.Class(code=p[4].code, symtab=newSymboltable)

#   # CLASS Unimplemented

# def p_class_with_features_inheritance(p):
#   'class : CLASS CLASS_TYPE INHERITS CLASS_TYPE LBRACE RBRACE'
#   rule.append(9)

#   newSymboltable = Symtab(parent=None,symtab_type='class',scope_name=p[2])
#   current_symbol_table[0] = newSymboltable
#   p[0]=TREE.Class(code=p[4].code, symtab=newSymboltable)

#   # CLASS Unimplemented

# def p_class(p):
#   'class : CLASS CLASS_TYPE LBRACE RBRACE'
#   rule.append(10)
#   newSymboltable = Symtab(parent=None,symtab_type='class',scope_name=p[2])
#   current_symbol_table[0] = newSymboltable
#   p[0]=TREE.Class(code=p[4].code, symtab=newSymboltable)

  # CLASS Unimplemented


def p_features_list_mult(p):
  'features_list : features_list feature SEMICOLON'
  rule.append(11)

  code = p[1].code
  code.extend(p[2].code)
  p[0] = TREE.FeatureList(code=code)


  
def p_features_list(p):
  'features_list : feature SEMICOLON'
  rule.append(12)

  p[0] = TREE.FeatureList(code = p[1].code)

def p_feature_header_body(p):
  'feature : feature_header feature_body'
  code = p[1].code
  code.extend(p[2].code)
  p[0] = TREE.FeatureHeader(code=code,datatype=p[1].datatype)


  current_symbol_table[0]=current_symbol_table[0].parent


def p_feature_header_with_modifier(p):
  'feature_header : DEF modifier ID COLON type'

  code = ['FUNC_LABEL,'+current_symbol_table[0].scope_name+'.'+p[3]]
  p[0] = TREE.FeatureHeader(code=code, datatype=p[5].place)

  new_sym_tab = Symtab(parent=current_symbol_table[0], symtab_type='METHOD', scope_name=p[3])
  # current_symbol_table[0].methods.append(new_sym_tab)
  current_symbol_table[0].enter_method(p[3],p[5])
  current_symbol_table[0] = new_sym_tab
  SymbolTables.append(new_sym_tab)

def p_feature_header(p):
  'feature_header : DEF ID COLON type'
  code = ['FUNC_LABEL,'+current_symbol_table[0].scope_name+'.'+p[2]]
  p[0] = TREE.FeatureHeader(code=code, datatype=p[4].place)

  new_sym_tab = Symtab(parent=current_symbol_table[0], symtab_type='METHOD', scope_name=p[2])
  current_symbol_table[0].enter_method(p[2],p[4])
  # current_symbol_table[0].methods.append(new_sym_tab,p[4])
  current_symbol_table[0] = new_sym_tab
  SymbolTables.append(new_sym_tab)

def p_feature_body_with_formal_parameter_list(p):
  'feature_body : LPAREN formal_parameter_list RPAREN LBRACE expression RBRACE'
  code = p[2].code
  code.extend(p[5].code)
  code.append('FUNC_RETURN')
  p[0]=TREE.FeatureBody(code=code)



def p_feature_body(p):
  'feature_body : LPAREN RPAREN LBRACE expression RBRACE'
  # print p[6]
  code = p[4].code
  code.append('FUNC_RETURN')
  p[0]=TREE.FeatureBody(code=code)


# def p_feature_with_modifier_with_formal_parameter_list(p):
#   'feature : modifier ID LPAREN formal_parameter_list RPAREN COLON type LBRACE expression RBRACE'
#   rule.append(13)



#   # modifier, type not implemented
#   code = p[4].code
#   code=code.append('FUNC_LABEL,'+p[2])
#   code.extend(p[8].code)
#   code.append('FUNC_RETURN')
#   p[0]=TREE.Feature(code=code)



# def p_feature_with_modifier(p):
#   'feature : modifier ID LPAREN RPAREN COLON type LBRACE expression RBRACE'
#   rule.append(14)

#   # modifier, type not implemented
#   code=['FUNC_LABEL,'+p[2]]
#   code.extend(p[8].code)
#   code.append('FUNC_RETURN')
#   p[0]=TREE.Feature(code=code)



# def p_feature_with_formal_parameter_list(p):
#   'feature : ID LPAREN formal_parameter_list RPAREN COLON type LBRACE expression RBRACE'
#   rule.append(15)

#   # type not implemented

#   code = p[3].code
#   code=code.append('FUNC_LABEL,'+p[1])
#   code.extend(p[7].code)
#   code.append('FUNC_RETURN')
#   p[0]=TREE.Feature(code=code)

# def p_feature(p):
#   'feature : ID LPAREN RPAREN COLON type LBRACE expression RBRACE'
#   rule.append(16)


#   # type not implemented

#   code=['FUNC_LABEL,'+p[1]]
#   code.extend(p[7].code)
#   code.append('FUNC_RETURN')
#   p[0]=TREE.Feature(code=code)




def p_feature_modifier_formal(p):
  'feature : modifier formal'
  rule.append(17)

  # modifier not implemented
  p[0] = TREE.Feature(code=p[2].code, datatype=p[2].datatype)

def p_feature_formal(p):
  'feature : formal'
  rule.append(18)

  p[0] = TREE.Feature(code=p[1].code, datatype=p[1].datatype)

def p_modifier_public(p):
  'modifier : PUBLIC'
  rule.append(19)

  # modifier not implemented

def p_modifier_private(p):
  'modifier : PRIVATE'
  rule.append(20)

  # modifier not implemented


def p_type_class_type(p):
  'type : CLASS_TYPE'
  rule.append(21)

  p[0] = TREE.Type(place=p[1])



  # type to be handled with symbol table

def p_type_integer_type(p):
  'type : INTEGER_TYPE'
  rule.append(22)
  p[0] = TREE.Type(place=p[1])

def p_type_bool_type(p):
  'type : BOOL_TYPE'
  rule.append(23)
  p[0] = TREE.Type(place=p[1])

def p_type_string_type(p):
  'type : STRING_TYPE'
  rule.append(24)
  p[0] = TREE.Type(place=p[1])

def p_type_object(p):
  'type : OBJECT'
  rule.append(25)
  p[0] = TREE.Type(place=p[1])

def p_type_self_type(p):
  'type : SELF_TYPE'
  rule.append(26)
  p[0] = TREE.Type(place=p[1])


def p_formal_parameter_list_many(p):
  'formal_parameter_list : formal_parameter_list COMMA formal_parameter'
  rule.append(27)

  code = p[1].code
  code.append('POP_STACK,' + p[3].place)
  p[0] = TREE.FormalParameterList(code=code)


def p_formal_parameter_list(p):
  'formal_parameter_list : formal_parameter'
  rule.append(28)

  code = ['POP_STACK,' + p[1].place]
  p[0] = TREE.FormalParameterList(code=code)




def p_formal_parameter(p):
  'formal_parameter : ID COLON type'
  rule.append(29)

  p[0] = TREE.FormalParameter(code=[], place=p[1], datatype=p[3])
  if p[3].place in ClassDict or p[3].place in ['Int','String']:
    pass
    # print ClassDict[p[3].place].scope_name
  else:
    sys.exit('No object found named ' + p[3].place)

  current_symbol_table[0].enter(name=p[1], datatype=p[3].place, size=4, isArray =False)

def p_formal_parameter_arr(p):
  'formal_parameter : ID LSQRBRACKET RSQRBRACKET COLON type'
  rule.append(30)

  p[0] = TREE.FormalParameter(code=[], place=p[1], datatype='Array')
  if p[5].place in ClassDict or p[5].place in ['Int','String']:
    pass
    # print ClassDict[p[3].place].scope_name
  else:
    sys.exit('No object found named ' + p[3].place)


  current_symbol_table[0].enter(name=p[1], datatype=p[5].place, size=4*1000, isArray=True)


def p_formal_with_assign(p):
  'formal : ID COLON type GETS expression'
  rule.append(31)

  code=['ASSIGN,%s,%s'%(p[1], p[5].place)]
  p[0]=TREE.Formal(code=code)

  if p[3].place in ClassDict or p[3].place in ['Int','String']:
    pass
    # print ClassDict[p[3].place].scope_name
  else:
    sys.exit('No object found named ' + p[3].place)

  current_symbol_table[0].enter(name=p[1], datatype=p[3].place, size=4, isArray =False)

def p_formal(p):
  'formal : ID COLON type'
  rule.append(32)
  p[0]=TREE.Formal(code=[])

  # print "type in formal " + p[3].place
  if p[3].place in ClassDict or p[3].place in ['Int','String']:
    pass
    # print ClassDict[p[3].place].scope_name
  else:
    sys.exit('No object found named ' + p[3].place)
  # quit()

  current_symbol_table[0].enter(name=p[1], datatype=p[3].place, size=4, isArray =False)

  # p[0] = TREE.SymTabEntry(id=p[1], datatype=p[3].datatype)

def p_formal_arr(p):
  'formal : ID COLON type LSQRBRACKET expression RSQRBRACKET'
  rule.append(33)

  p[0]=TREE.Formal(code=[])
  if p[3].place in ClassDict or p[3].place in ['Int','String']:
    pass
    # print ClassDict[p[3].place].scope_name
  else:
    sys.exit('No object found named ' + p[3].place)
  current_symbol_table[0].enter(name=p[1],datatype='Array',size=4*int(p[5].place), isArray =False)


#--------------------------------------------  Not DONE ----------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------

def p_expression_block_expression(p):
  'expression : block_expression'
  rule.append(34)

  p[0] = TREE.Expression(code=p[1].code, datatype=p[1].datatype) 



def p_block_expression(p):
  'block_expression : LBRACE block_list RBRACE'
  rule.append(35)

  p[0] = TREE.BlockExpression(code=p[2].code, datatype=p[2].datatype)

def p_block_list_many(p):
  'block_list : block_list expression SEMICOLON'
  rule.append(36)
  code = p[1].code
  code.extend(p[2].code)
  p[0] = TREE.BlockList(code=code, datatype=p[2].datatype)

def p_block_list(p):
  'block_list : expression SEMICOLON'
  rule.append(37)

  
  p[0] = TREE.BlockList(code=p[1].code,datatype=p[1].datatype)


def p_expression_assign(p):
  'expression : ID GETS expression'
  rule.append(38)
  var = current_symbol_table[0].getVariable(p[1])

  code = p[3].code
  # print("CODE : ", code, p[3].place, p[3])
  s = 'ASSIGN,' + p[1] +',' + p[3].place
  code.append(s)
  p[0] = TREE.Expression(code=code, datatype=p[3].datatype)
  # print("================")
  # print(p[0])

  # print("================")

def p_expression_assign_arr(p):
  'expression : ID LSQRBRACKET expression RSQRBRACKET GETS expression'
  rule.append(39)
  var = current_symbol_table[0].getVariable(p[1])

  code = p[6].code
  code.extend(p[3].code)
  code.append('INDEX_ASSIGN_L,'+p[1]+','+p[3].place+','+p[6].place)
  
  p[0] = TREE.Expression(code=code,place=p[6].place, datatype='Array')

def p_expression_function_call_with_arguments_2(p):
  'expression : ID LPAREN argument_list RPAREN'
  rule.append(40)
  met = current_symbol_table[0].getMethod(p[1])
  
  code = p[3].code
  code.append('FUNC_CALL,'+p[1])
  datatype = met.datatype
  p[0]=TREE.FunctionCall(code=code, datatype=datatype)


def p_expression_function_call_2(p):
  'expression : ID LPAREN RPAREN'
  rule.append(41)
  met = current_symbol_table[0].getMethod(p[1])

  t=newtemp()
  code = ['FUNC_CALL,'+p[1]+','+t]
  datatype = met.datatype
  p[0] = TREE.Expression(code=code,place=t, datatype=datatype)


def p_argument_list(p):
  'argument_list : expression'
  rule.append(42)

  code = ['FUNC_PARAM,{}'.format(p[1].place)]
  p[0]=TREE.ArgumentList(code=code)

def p_argument_list_many(p):
  'argument_list : argument_list COMMA expression'
  rule.append(43)

  code = []
  code.append('FUNC_PARAM,{}'.format(p[3].place))
  code.extend(p[1].code)

  p[0]=TREE.ArgumentList(code=code)

def p_expression_plus(p):
  'expression : expression PLUS expression'
  rule.append(44)

  t = newtemp()
  code = p[1].code
  code.extend(p[3].code)
  code.append('ADD,' + t + ',' + p[1].place + ',' + p[3].place)

  p[0] = TREE.Expression(place = t, code = code, datatype = p[1].datatype)




def p_expression_minus(p):
  'expression : expression MINUS expression'
  rule.append(45)

  t = newtemp()
  code = p[1].code
  code.extend(p[3].code)
  code.append('SUB,' + t + ',' + p[1].place + ',' + p[3].place)

  p[0] = TREE.Expression(place = t, code = code, datatype = p[1].datatype)

def p_expression_times(p):
  'expression : expression TIMES expression'
  rule.append(46)

  t = newtemp()
  code = p[1].code
  code.extend(p[3].code)
  code.append('MUL,' + t + ',' + p[1].place + ',' + p[3].place)

  p[0] = TREE.Expression(place = t, code = code, datatype = p[1].datatype)

def p_expression_divide(p):
  'expression : expression DIVIDE expression'
  rule.append(47)

  t = newtemp()
  code = p[1].code
  code.extend(p[3].code)
  code.append('DIV,' + t + ',' + p[1].place + ',' + p[3].place)

  p[0] = TREE.Expression(place = t, code = code, datatype = p[1].datatype)

def p_expression_mod(p):
  'expression : expression MOD expression'
  rule.append(48)

  t = newtemp()
  code = p[1].code
  code.extend(p[3].code)
  code.append('MOD,' + t + ',' + p[1].place + ',' + p[3].place)

  p[0] = TREE.Expression(place = t, code = code, datatype = p[1].datatype)

def p_expression_lt(p):
  'expression : expression LT expression'
  rule.append(49)

  t = newtemp()
  j_if = newjump()
  j_fi = newjump()
  # print("@@@@@@@@")
  # print(p[3].code)
  # print("@@@@@@@")
  code = p[1].code
  code.extend(p[3].code)
  # code.append('LESS_THAN,' + t + ',' + p[1].place + ',' + p[3].place)

  code.append("IFGOTO,LESS_THAN," + p[1].place + ',' + p[3].place + ',' + j_if)
  code.append("ASSIGN," + t + ',0')
  code.append("JUMP," + j_fi)
  code.append("LABEL,"+j_if)
  code.append("ASSIGN," + t + ',1')
  code.append("LABEL," + j_fi)

  p[0] = TREE.Expression(code = code, place = t, datatype = 'Int')

def p_expression_gt(p):
  'expression : expression GT expression'
  rule.append(50)

  t = newtemp()
  j_if = newjump()
  j_fi = newjump()
  code = p[1].code
  code.extend(p[3].code)
  # code.append('LESS_THAN,' + t + ',' + p[1].place + ',' + p[3].place)
  code.append("IFGOTO,GREATER_THAN," + p[1].place + ',' + p[3].place + ',' + j_if)
  code.append("ASSIGN," + t + ',0')
  code.append("JUMP," + j_fi)
  code.append("LABEL,"+j_if)
  code.append("ASSIGN," + t + ',1')
  code.append("LABEL," + j_fi)

  p[0] = TREE.Expression(code = code, place = t, datatype = 'Int')


def p_expression_lteq(p):
  'expression : expression LTEQ expression'
  rule.append(51)

  t = newtemp()
  j_if = newjump()
  j_fi = newjump()
  code = p[1].code
  code.extend(p[3].code)
  # code.append('LESS_THAN,' + t + ',' + p[1].place + ',' + p[3].place)
  code.append("IFGOTO,LESS_THAN_EQUALS," + p[1].place + ',' + p[3].place + ',' + j_if)
  code.append("ASSIGN," + t + ',0')
  code.append("JUMP," + j_fi)
  code.append("LABEL,"+j_if)
  code.append("ASSIGN," + t + ',1')
  code.append("LABEL," + j_fi)

  p[0] = TREE.Expression(code = code, place = t, datatype = 'Int')

def p_expression_gteq(p):
  'expression : expression GTEQ expression'
  rule.append(52)

  t = newtemp()
  j_if = newjump()
  j_fi = newjump()
  code = p[1].code
  code.extend(p[3].code)
  # code.append('LESS_THAN,' + t + ',' + p[1].place + ',' + p[3].place)
  code.append("IFGOTO,GREATER_THAN_EQUALS," + p[1].place + ',' + p[3].place + ',' + j_if)
  code.append("ASSIGN," + t + ',0')
  code.append("JUMP," + j_fi)
  code.append("LABEL,"+j_if)
  code.append("ASSIGN," + t + ',1')
  code.append("LABEL," + j_fi)

  p[0] = TREE.Expression(code = code, place = t, datatype = 'Int')

def p_expression_equal(p):
  'expression : expression EQUAL expression'
  rule.append(53)

  t = newtemp()
  j_if = newjump()
  j_fi = newjump()
  code = p[1].code
  code.extend(p[3].code)
  # code.append('LESS_THAN,' + t + ',' + p[1].place + ',' + p[3].place)
  code.append("IFGOTO,EQUALS," + p[1].place + ',' + p[3].place + ',' + j_if)
  code.append("ASSIGN," + t + ',0')
  code.append("JUMP," + j_fi)
  code.append("LABEL,"+j_if)
  code.append("ASSIGN," + t + ',1')
  code.append("LABEL," + j_fi)

  p[0] = TREE.Expression(code = code, place = t, datatype = 'Int')

def p_expression_or(p):
  'expression : expression OR expression'
  rule.append(54)

  # t = newtemp()
  # code = p[1].code
  # code.extend(p[3].code)
  # code.append('ADD,' + t + ',' + p[1].place + ',' + p[3].place)

  t = newtemp()
  l1 = newjump()
  l2 = newjump()
  l3 = newjump()

  code = p[1].code
  code.append('IFGOTO,EQUALS,' + p[1].place + ',0,' + l1)
  code.append('ASSIGN,'+t+',1')
  code.append('JUMP,'+l3)
  code.append('LABEL,' + l1)
  code.extend(p[3].code)
  code.append('IFGOTO,EQUALS,' + p[3].place + ',0,' + l2)
  code.append('ASSIGN,'+t+',1')
  code.append('JUMP,'+l3)
  code.append('LABEL,' + l2)
  code.append('ASSIGN,' + t + ',0')
  code.append('LABEL,' + l3)

  p[0] = TREE.Expression(place = t, code = code, datatype = p[1].datatype)

def p_expression_and(p):
  'expression : expression AND expression'
  rule.append(55)

  t = newtemp()
  l1 = newjump()
  l2 = newjump()
  l3 = newjump()

  code = p[1].code
  code.append('IFGOTO,GREATER_THAN,' + p[1].place + ',0,' + l1)
  code.append('ASSIGN,'+t+',0')
  code.append('JUMP,'+l3)
  code.append('LABEL,' + l1)
  code.extend(p[3].code)
  code.append('IFGOTO,GREATER_THAN,' + p[3].place + ',0,' + l2)
  code.append('ASSIGN,'+t+',0')
  code.append('JUMP,'+l3)
  code.append('LABEL,' + l2)
  code.append('ASSIGN,' + t + ',1')
  code.append('LABEL,' + l3)

  p[0] = TREE.Expression(place = t, code = code, datatype = p[1].datatype)

def p_expression_not(p):
  'expression : NOT expression'
  rule.append(56)

  t = newtemp()
  j_if = newjump()
  j_fi = newjump()
  code = p[2].code
  # code.append('LESS_THAN,' + t + ',' + p[1].place + ',' + p[3].place)
  code.append("IFGOTO,EQUALS," + p[2].place + ',0,' + j_if)
  code.append("ASSIGN," + t + ',0')
  code.append("JUMP," + j_fi)
  code.append("LABEL,"+j_if)
  code.append("ASSIGN," + t + ',1')
  code.append("LABEL," + j_fi)

  p[0] = TREE.Expression(code = code, place = t, datatype = 'Int')

def p_expression_tilda(p):
  'expression : TILDA expression'
  rule.append(57)

  t = newtemp()
  code = p[2].code
  code.append('SUB,' + t + ',0,' + p[2].place)

  p[0] = TREE.Expression(place = t, code = code, datatype = p[2].datatype)

def p_expression_paren(p):
  'expression : LPAREN expression RPAREN'
  rule.append(58)

  t = p[2].place
  code = p[2].code

  p[0] = TREE.Expression(place = t, code = code, datatype = p[2].datatype)


# ---------------------------------------------------------------------------
def p_expression_self(p):
  'expression : SELF'
  rule.append(59)

  p[0] = TREE.Expression(code = ['SELF'])
# ---------------------------------------------------------------------------


def p_expression_id(p):
  'expression : ID'
  rule.append(60)
  var = current_symbol_table[0].getVariable(p[1])

  t = p[1]

  p[0] = TREE.Expression(place = t, code=[])

def p_expression_arr(p):
  'expression : ID LSQRBRACKET expression RSQRBRACKET'
  rule.append(61)
  var = current_symbol_table[0].getVariable(p[1])

  t = newtemp()
  code = p[3].code
  code.append('INDEX_ASSIGN_R,' + t + ',' + p[1] + ',' + p[3].place)

  p[0] = TREE.Expression(place = t, code = code, datatype='Array')


def p_expression_integer(p):
  'expression : INTEGER'
  rule.append(62)

  p[0] = TREE.Expression(code=[], place=str(p[1]), datatype='Int')
  # print("----", p[0].code, p[0].place,p[0])

def p_expression_string(p):
  'expression : STRING'
  rule.append(63)
  p[0] = TREE.Expression(place=p[1], datatype='String', code=[])

def p_expression_true(p):
  'expression : TRUE'
  rule.append(64)
  p[0] = TREE.Expression(place='1', code=[])

def p_expression_false(p):
  'expression : FALSE'
  rule.append(65)
  p[0] = TREE.Expression(place='0', code=[])

def p_expression_break(p):
  'expression : BREAK'
  rule.append(66)
  p[0] = TREE.Expression(code=['BREAK'])

def p_expression_continue(p):
  'expression : CONTINUE'
  rule.append(67)
  p[0] = TREE.Expression(code=['CONTINUE'])

def p_expression_function_call_with_arguments(p):
  'expression : expression PERIOD ID LPAREN argument_list RPAREN'
  rule.append(68)
  t=newtemp()
  code = p[1].code
  code.extend(p[5].code)
  # print(".................................", p[1].place)
  code.append('FUNC_CALL,'+current_symbol_table[0].getVariable(p[1].place).datatype+'.'+p[3]+','+t)
  # print("..........", current_symbol_table[0].getVariable(p[1].place).datatype)
  datatype = (ClassDict[current_symbol_table[0].getVariable(p[1].place).datatype].getMethod(p[3])).datatype
  p[0] = TREE.Expression(code=code,place=t)

def p_expression_function_call(p):
  'expression : expression PERIOD ID LPAREN RPAREN'
  rule.append(69)
  t=newtemp()
  # print "calling object function : ",current_symbol_table[0].getVariable(p[1].place).datatype
  # quit()
  
  code = p[1].code
  code.append('FUNC_CALL,'+current_symbol_table[0].getVariable(p[1].place).datatype+'.'+p[3]+','+t)
  # print("..........", current_symbol_table[0].getVariable(p[1].place).datatype)
  datatype = (ClassDict[current_symbol_table[0].getVariable(p[1].place).datatype].getMethod(p[3])).datatype
  p[0] = TREE.Expression(code=code,place=t, datatype=datatype)

def p_expression_new(p):
  'expression : NEW type'
  rule.append(70)
  t=newtemp()
  current_symbol_table[0].getVariable(t).datatype = p[2].place
  code = ['FUNC_CALL,constructor,'+t]
  p[0] = TREE.Expression(code=code,place=t, datatype=p[2].place)

def p_expression_isvoid(p):
  'expression : ISVOID expression'
  rule.append(71)
  t=newtemp()
  code = ['FUNC_CALL,isvoid,'+t]
  p[0] = TREE.Expression(code=code,place=t, datatype=p[2].datatype)

def p_expression_let_expression(p):
  'expression : let_expression'
  rule.append(72)
  p[0] = TREE.Expression(code = p[1].code, datatype=p[1].datatype)


def p_let_to_let(p):
  'let : LET'

  let_id = newLet()

  new_sym_tab = Symtab(parent=current_symbol_table[0], symtab_type='LET', scope_name=let_id)
  current_symbol_table[0].lets.append(new_sym_tab)
  SymbolTables.append(new_sym_tab)
  current_symbol_table[0] = new_sym_tab



def p_let_expression(p):
  'let_expression : let formaldehyde IN expression TEL'
  rule.append(73)

  code = p[2].code
  code.extend(p[4].code)
  p[0] = TREE.Let(code = code, datatype=p[4].datatype)

  current_symbol_table[0] = current_symbol_table[0].parent




def p_expression_at_function_with_arguments(p):
  'expression : expression AT CLASS_TYPE PERIOD ID LPAREN argument_list RPAREN'
  rule.append(74)
  t=newtemp()

  code = p[1].code
  code.extend(p[7].code)
  code=['to handle AT']
  p[0] = TREE.Expression(code=code,place=t)

def p_expression_at_function(p):
  'expression : expression AT CLASS_TYPE PERIOD ID LPAREN RPAREN'
  rule.append(75)

  t=newtemp()
  ode = p[1].code
  code=['to handle AT']
  p[0] = TREE.Expression(code=code,place=t)


def p_expression_if_then_else(p):
  'expression : if_then_else'
  rule.append(76)

  p[0] = TREE.Expression(code=p[1].code, datatype=p[1].datatype)

def p_if_then_else(p):
  'if_then_else : IF expression THEN expression ELSE expression FI'
  rule.append(77)

  _if = newjump()
  _fi = newjump()
  code=p[2].code
  code.append('IFGOTO,GREATER_THAN,' + p[2].place + ',0,' +  _if)
  code.extend(p[6].code)
  code.append('JUMP,' + _fi)
  code.append('LABEL,' + _if)
  code.extend(p[4].code)
  code.append('LABEL,'+_fi)

  p[0] = TREE.If_Then_Else(code=code, datatype=p[6].datatype)

def p_expression_while(p):
  'expression : while'
  rule.append(78)

  p[0] = TREE.Expression(code=p[1].code, datatype=p[1].datatype)


def p_while(p):
  'while : WHILE expression LOOP expression POOL'
  rule.append(79)


  _loop = newjump()
  _pool = newjump()
  code = ['LABEL,' + _loop]
  code.extend(p[2].code)
  code.append('IFGOTO,EQUALS,' + p[2].place + ',0,' +  _pool)
  code.extend(p[4].code)
  code.append('JUMP,'+_loop)
  code.append('LABEL,'+_pool)
  for i in range(len(code)):
    if(code[i]=='BREAK'):
      code[i]=_pool
    elif(code[i]=='CONTINUE'):
      code[i]=_loop

  p[0] = TREE.While(code=code, datatype=p[4].datatype)


def p_expression_for(p):
  'expression : for'
  rule.append(80)

  p[0] = TREE.Expression(code=p[1].code, datatype=p[1].datatype)

def p_for(p):
  'for : FOR LPAREN expression SEMICOLON expression SEMICOLON expression RPAREN LOOP expression POOL'
  rule.append(81)

  _loop = newjump()
  _pool = newjump()

  code = p[3].code
  # print("==================")
  # print(p[3].code)
  # print("==================")
  code.append('LABEL,' + _loop)
  code.extend(p[5].code)
  code.append('IFGOTO,EQUALS,'+p[5].place+',0,' + _pool)
  code.extend(p[10].code)
  code.extend(p[7].code)
  code.append('JUMP,'+ _loop)
  code.append('LABEL,' + _pool)

  for i in range(len(code)):
    if(code[i]=='BREAK'):
      code[i]='JUMP,'+_pool
      # sys.exit(_pool)
    elif(code[i]=='CONTINUE'):
      code[i]='JUMP,'+_loop

  # print "agsdiagsdia"
  p[0] = TREE.For(code=code, datatype=p[10].datatype)


def p_formaldehyde_with_assign_many(p):
  'formaldehyde : formaldehyde COMMA ID COLON type GETS expression'
  # rule.append(31)

  code = p[1].code
  code.append('ASSIGN,%s,%s'%(p[3], p[7].place))

  if p[5].place in ClassDict or p[5].place in ['Int','String']:
    pass
    # print ClassDict[p[3].place].scope_name
  else:
    sys.exit('No object found named ' + p[3].place)

  p[0]=TREE.Formal(code=code)


  current_symbol_table[0].enter(name=p[3],datatype=p[5].place,size=4, isArray =False)

def p_formaldehyde_many(p):
  'formaldehyde : formaldehyde COMMA ID COLON type'
  # rule.append(32)
  p[0]=TREE.Formal(code=[])
  # print p[3]
  # quit()
  if p[5].place in ClassDict or p[5].place in ['Int','String']:
    pass
    # print ClassDict[p[3].place].scope_name
  else:
    sys.exit('No object found named ' + p[3].place)

  current_symbol_table[0].enter(name=p[3],datatype=p[5].place,size=4, isArray =False)


def p_formaldehyde_arr_many(p):
  'formaldehyde : formaldehyde COMMA ID COLON type LSQRBRACKET expression RSQRBRACKET'
  # rule.append(33)

  p[0]=TREE.Formal(code=[])
  if p[5].place in ClassDict or p[5].place in ['Int','String']:
    pass
    # print ClassDict[p[3].place].scope_name
  else:
    sys.exit('No object found named ' + p[3].place)

  current_symbol_table[0].enter(name=p[3],datatype='Array',size=4000, isArray =True)


def p_formaldehyde_with_assign(p):
  'formaldehyde : ID COLON type GETS expression'
  # rule.append(31)

  code=['ASSIGN,%s,%s'%(p[1], p[5].place)]
  # p[0] = TREE.SymTabEntry(id=p[1], datatype=p[3].datatype, code=code)
  p[0]=TREE.Formal(code=code)
  if p[3].place in ClassDict or p[3].place in ['Int','String']:
    pass
    # print ClassDict[p[3].place].scope_name
  else:
    sys.exit('No object found named ' + p[3].place)

  current_symbol_table[0].enter(name=p[1],datatype=p[3].place,size=4, isArray =False)

def p_formaldehyde(p):
  'formaldehyde : ID COLON type'
  # rule.append(32)
  p[0]=TREE.Formal(code=[])
  current_symbol_table[0].enter(name=p[1],datatype=p[3].place,size=4, isArray =False)
  if p[3].place in ClassDict or p[3].place in ['Int','String']:
    pass
    # print ClassDict[p[3].place].scope_name
  else:
    sys.exit('No object found named ' + p[3].place)

  # p[0] = TREE.SymTabEntry(id=p[1], datatype=p[3].datatype)

def p_formaldehyde_arr(p):
  'formaldehyde : ID COLON type LSQRBRACKET expression RSQRBRACKET'
  # rule.append(33)

  p[0]=TREE.Formal(code=[])
  if p[3].place in ClassDict or p[3].place in ['Int','String']:
    pass
    # print ClassDict[p[3].place].scope_name
  else:
    sys.exit('No object found named ' + p[3].place)

  current_symbol_table[0].enter(name=p[1],datatype='Array',size=4000, isArray =True)


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


input_file = sys.argv[1]
with open(input_file) as file:
    data = file.read()
parser.parse(data)
# print(rule)


for s in SymbolTables:
  print("===========")
  s.printsymtab()
# print "*****class dictionary*****"
# for x in ClassDict:
# 	print ClassDict[x].scope_name