#!/usr/bin/env python

import ply.yacc as yacc
import sys
from lexer import tokens
import tree as TREE
from symtab import *
from codegen import main
from copy import deepcopy
import string

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
current_symbol_table = [Symtab(parent=None, symtab_type='CLASS', scope_name='GLOBAL')]  #not a list only one symboltable
ClassDict = {}

ClassTable = {}
currentClass=['Main']
basicDataType = ['Int','String','Bool']

String_Dict = {}
'''
     TO BE DONE
'''

def get_expression_place(name):
  if is_int(name):
    return name
  if current_symbol_table[0].search(name):
    var = current_symbol_table[0].getVariable(name)
    expression_place = var.changed_name
  else:
    expression_place = name
  return expression_place

flag=[0]
tempCount=[0]

stringcount = [0]



def newstring( input_str, datatype='String'):
  stringcount[0] += 1
  str_name = 'str.' + str(stringcount[0])
  output_str = input_str.replace("\n", "%c%c"%("\\","n"))
  output_str = output_str.replace("\t", "%c%c"%("\\","t"))
  # print input_str
  # output_str = input_str.replace('\n', '*nl*')
  # output_str = output_str.replace("\t", "*tb*")
  String_Dict[str_name] = "'" + output_str + "'"
  # print output_str,"!!!!"
  return str_name


def newtemp(datatype='Int'):
  tempCount[0] += 1
  temp_name = 't.' + str(tempCount[0])
  current_symbol_table[0].enter(name = temp_name,changed_name=current_symbol_table[0].scope_name + '.' + temp_name, datatype=datatype)
  
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
  # t = newtemp()
  print "1,GOTO,CLASS.Main"
  print "2,EXIT"
  i=3
  f=open(sys.argv[2], 'wb')
  f.write("1,GOTO,CLASS.Main,"+'\n')
  f.write("2,EXIT\n")
  for a in p[0].code:
    if(len(a)):
      print(str(i) + ',' + a)
      f.write(str(i) + ',' + a + '\n')
      i+=1
  f.close()

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

  new_sym_tab = Symtab(parent=ClassDict[p[4]], symtab_type="CLASS", scope_name=p[2])
  ClassDict[p[2]] = new_sym_tab
  SymbolTables.append(new_sym_tab)
  current_symbol_table[0] = new_sym_tab

  ClassTable[p[2]] = ClassObject(p[2])
  ClassTable[p[2]].parent = ClassTable[p[4]]



  currentClass[0]=p[2]



  ClassTable[p[2]].variables = deepcopy(ClassTable[p[4]].variables)
  ClassTable[p[2]].size = ClassTable[p[4]].size
  ClassTable[p[2]].parentprivatevariables = ClassTable[p[4]].private[:]
  ClassTable[p[2]].parentprivatevariables.extend(ClassTable[p[4]].parentprivatevariables)
  ClassTable[p[2]].privateFunctions = ClassTable[p[4]].privateFunctions[:]


  p[0] = TREE.ClassHeader(code=[])


def p_class_header(p):
  'class_header : CLASS CLASS_TYPE'

  code = ['LABEL,CLASS.' + p[2]]


  p[0] = TREE.ClassHeader(code=code)


  new_sym_tab = Symtab(parent=None, symtab_type="CLASS", scope_name=p[2])
  ClassDict[p[2]] = new_sym_tab
  SymbolTables.append(new_sym_tab)
  current_symbol_table[0] = new_sym_tab

  currentClass[0]=p[2]
  ClassTable[p[2]] = ClassObject(p[2])

def p_class_body_empty(p):
  'class_body : LBRACE RBRACE'

def p_class_body(p):
  'class_body : LBRACE features_list RBRACE'

  p[0] = TREE.Class(code=p[2].code)


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
  p[0] = TREE.FeatureHeader(code=code,datatype=p[1].datatype,name = p[1].name)

  met = current_symbol_table[0].getMethod(p[1].name)
  met.nargs = p[2].nargs

  # ClassTable[current_symbol_table[0].parent.scope_name].function_parameters[p[1].name] = p[2].nargs

  # print current_symbol_table[0].parent.scope_name,p[1].name,p[2].nargs
  # raw_input()

  current_symbol_table[0]=current_symbol_table[0].parent


def p_feature_header_with_modifier(p):
  'feature_header : DEF modifier ID COLON type'

  if p[2].name == 'PRIVATE':
    ClassTable[currentClass[0]].privateFunctions.append(p[3])
  code=[]
  if current_symbol_table[0].scope_name == 'Main':
    if(not flag[0]):
      code.append('FUNC_CALL,Main.main')
      code.append('EXIT')
      flag[0]=1
  code.append('FUNC_LABEL,'+current_symbol_table[0].scope_name+'.'+p[3])
  p[0] = TREE.FeatureHeader(code=code, datatype=p[5].place,name = p[3])

  new_sym_tab = Symtab(parent=current_symbol_table[0], symtab_type='METHOD', scope_name=current_symbol_table[0].scope_name+'.'+p[3])
  # current_symbol_table[0].methods.append(new_sym_tab)
  current_symbol_table[0].enter_method(p[3],p[5].place,current_symbol_table[0].scope_name)

  ClassTable[current_symbol_table[0].scope_name].functions[p[3]] = current_symbol_table[0].scope_name+'.'+p[3]

  current_symbol_table[0] = new_sym_tab
  SymbolTables.append(new_sym_tab)

def p_feature_header(p):
  'feature_header : DEF ID COLON type'
  code=[]
  if current_symbol_table[0].scope_name == 'Main':
    if(not flag[0]):
      code.append('FUNC_CALL,Main.main')
      code.append('EXIT')
      flag[0]=1

  if(p[2] in ClassTable[currentClass[0]].privateFunctions ):
    ClassTable[currentClass[0]].privateFunctions.remove(p[2])
  code.append('FUNC_LABEL,'+current_symbol_table[0].scope_name+'.'+p[2])
  p[0] = TREE.FeatureHeader(code=code, datatype=p[4].place,name = p[2])

  new_sym_tab = Symtab(parent=current_symbol_table[0], symtab_type='METHOD', scope_name=current_symbol_table[0].scope_name+'.'+p[2])

  current_symbol_table[0].enter_method(p[2],p[4].place,current_symbol_table[0].scope_name)

  ClassTable[current_symbol_table[0].scope_name].functions[p[2]] = current_symbol_table[0].scope_name+'.'+p[2]

  current_symbol_table[0] = new_sym_tab
  SymbolTables.append(new_sym_tab)


def p_feature_body_with_formal_parameter_list(p):
  'feature_body : LPAREN formal_parameter_list RPAREN LBRACE expression RBRACE'
  code = p[2].code
  code = list(reversed(code))
  code.extend(p[5].code)
  for i in range(p[2].nargs):
  	code.append('POP_STACK')

  code.append('FUNC_RETURN')
  p[0]=TREE.FeatureBody(code=code,nargs = p[2].nargs)



def p_feature_body(p):
  'feature_body : LPAREN RPAREN LBRACE expression RBRACE'
  code = p[4].code

  if current_symbol_table[0].scope_name == 'Main.main':
    code.append('EXIT')
  else:
    code.append('FUNC_RETURN')

  p[0]=TREE.FeatureBody(code=code, nargs = 0)




def p_feature_modifier_formal(p):
  'feature : modifier formal'
  rule.append(17)

  if p[1].name == 'PRIVATE':
    ClassTable[currentClass[0]].private.append(p[2].name)


  p[0] = TREE.Feature(code=p[2].code, datatype=p[2].datatype)

def p_feature_formal(p):
  'feature : formal'
  rule.append(18)

  p[0] = TREE.Feature(code=p[1].code, datatype=p[1].datatype)

def p_modifier_public(p):
  'modifier : PUBLIC'
  rule.append(19)

  p[0] = TREE.Modifier(name = 'PUBLIC')


def p_modifier_private(p):
  'modifier : PRIVATE'
  rule.append(20)
  p[0] = TREE.Modifier(name = 'PRIVATE')



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
  # changed_name = p[3].place

  _,class_name = current_symbol_table[0].scope_name.split('.')
  ClassTable[current_symbol_table[0].parent.scope_name].function_parameters[class_name] = p[1].nargs+1

  # if p[3].datatype.place == 'Int':
  #   changed_name = current_symbol_table[0].getVariable(p[3].place).parent_scope_name + '.' + p[3].place
  var = current_symbol_table[0].getVariable(p[3].place)
  code.append('READ_STACK,' + var.changed_name)
  p[0] = TREE.FormalParameterList(code=code,nargs=p[1].nargs+1)


def p_formal_parameter_list(p):
  'formal_parameter_list : formal_parameter'
  rule.append(28)

  _,class_name = current_symbol_table[0].scope_name.split('.')
  # print  current_symbol_table[0].scope_name, class_name
  ClassTable[current_symbol_table[0].parent.scope_name].function_parameters[class_name] = 1
  # print ClassTable[current_symbol_table[0].parent.scope_name].function_parameters

  # raw_input()
  
  # changed_name = p[1].place
  # if p[1].datatype.place == 'Int':
  #   changed_name = current_symbol_table[0].getVariable(p[1].place).parent_scope_name + '.' + p[1].place
  var = current_symbol_table[0].getVariable(p[1].place)
  
  code = ['READ_STACK,' + var.changed_name]
  p[0] = TREE.FormalParameterList(code=code,nargs=1)




def p_formal_parameter(p):
  'formal_parameter : ID COLON type'
  rule.append(29)

  p[0] = TREE.FormalParameter(code=[], place=p[1], datatype=p[3])
  if p[3].place in ClassDict or p[3].place in basicDataType:
    pass
  else:
    sys.exit('No object found named ' + p[3].place)

  current_symbol_table[0].enter(name = p[1], changed_name=current_symbol_table[0].scope_name +'.' + p[1], datatype=p[3].place, size=4, isArray =False)


def p_formal_parameter_arr(p):
  'formal_parameter : ID LSQRBRACKET RSQRBRACKET COLON type'
  rule.append(30)

  p[0] = TREE.FormalParameter(code=[], place=p[1], datatype='Array')
  if p[5].place in ClassDict or p[5].place in basicDataType:
    pass
  else:
    sys.exit('No object found named ' + p[3].place)


  current_symbol_table[0].enter(name = p[1], changed_name=current_symbol_table[0].scope_name +'.' + p[1], datatype=p[5].place, size=4, isArray=True)


def p_formal_with_assign(p):
  'formal : ID COLON type GETS expression'
  rule.append(31)
  code = p[5].code
  if(p[3].place == 'String'):
    code.append('ALLOCATE,' +current_symbol_table[0].scope_name + '.' + p[1] + ',100')
    current_symbol_table[0].enter(name = p[1], changed_name=current_symbol_table[0].scope_name +'.' + p[1], datatype=p[3].place, size=100, isArray =False)

  else:
    current_symbol_table[0].enter(name = p[1], changed_name=current_symbol_table[0].scope_name +'.' + p[1], datatype=p[3].place, size=4, isArray =False)

  code.append('ASSIGN,%s,%s'%(get_expression_place(p[1]), get_expression_place(p[5].place)))
  p[0]=TREE.Formal(code=code,name = p[1])

  if p[3].place in ClassDict or p[3].place in basicDataType:
    pass
  else:
    sys.exit('No object found named ' + p[3].place)



  if(current_symbol_table[0].scope_name in ClassTable):
    if(p[1] in ClassTable[current_symbol_table[0].scope_name].variables):
      sys.exit("Variable already present in ancestor")
    else:
      ClassTable[current_symbol_table[0].scope_name].variables[p[1]] = ClassTable[current_symbol_table[0].scope_name].size/4
      ClassTable[current_symbol_table[0].scope_name].size += 4


def p_formal(p):
  'formal : ID COLON type'
  rule.append(32)

  code = []

  if(p[3].place == 'String'):
    code.append('ALLOCATE,' +current_symbol_table[0].scope_name + '.' + p[1] + ',100')
    current_symbol_table[0].enter(name = p[1], changed_name=current_symbol_table[0].scope_name +'.' + p[1], datatype=p[3].place, size=100, isArray =False)

  else:
    current_symbol_table[0].enter(name = p[1], changed_name=current_symbol_table[0].scope_name +'.' + p[1], datatype=p[3].place, size=4, isArray =False)

  p[0]=TREE.Formal(code=code,name = p[1])

  if p[3].place in ClassDict or p[3].place in basicDataType:
    pass
  else:
    sys.exit('No object found named ' + p[3].place)
  
  # current_symbol_table[0].enter(name = p[1], changed_name=current_symbol_table[0].scope_name +'.' + p[1], datatype=p[3].place, size=4, isArray =False)

  if(current_symbol_table[0].scope_name in ClassTable):
    if(p[1] in ClassTable[current_symbol_table[0].scope_name].variables):
      sys.exit("Variable already present in ancestor")
    else:
      ClassTable[current_symbol_table[0].scope_name].variables[p[1]] = ClassTable[current_symbol_table[0].scope_name].size/4
      ClassTable[current_symbol_table[0].scope_name].size += 4




def p_formal_arr(p):
  'formal : ID COLON type LSQRBRACKET expression RSQRBRACKET'
  rule.append(33)


  code = p[5].code
  code.append('ALLOCATE,' +current_symbol_table[0].scope_name + '.' + p[1] + ',' + p[5].place)

  p[0]=TREE.Formal(code=code,name = p[1])
  if p[3].place in ClassDict or p[3].place in basicDataType:
    pass
  else:
    sys.exit('No object found named ' + p[3].place)
  current_symbol_table[0].enter(name = p[1], changed_name=current_symbol_table[0].scope_name + '.' + p[1],datatype=p[3].place,size=4*int(p[5].place), isArray =True)

  if(current_symbol_table[0].scope_name in ClassTable):
    if(p[1] in ClassTable[current_symbol_table[0].scope_name].variables):
      sys.exit("Variable already present in ancestor")
    else:
      ClassTable[current_symbol_table[0].scope_name].variables[p[1]] = ClassTable[current_symbol_table[0].scope_name].size/4
      ClassTable[current_symbol_table[0].scope_name].size += 4



def p_expression_block_expression(p):
  'expression : block_expression'
  rule.append(34)

  p[0] = TREE.Expression(code=p[1].code, datatype='block',place=p[1].place) 



def p_block_expression(p):
  'block_expression : LBRACE block_list RBRACE'
  rule.append(35)

  p[0] = TREE.BlockExpression(code=p[2].code, datatype=p[2].datatype,place=p[2].place)

def p_block_list_many(p):
  'block_list : block_list expression SEMICOLON'
  rule.append(36)
  code = p[1].code
  code.extend(p[2].code)
  p[0] = TREE.BlockList(code=code, datatype=p[2].datatype,place=p[2].place)

def p_block_list(p):
  'block_list : expression SEMICOLON'
  rule.append(37)

  
  p[0] = TREE.BlockList(code=p[1].code,datatype=p[1].datatype,place=p[1].place)


def p_expression_assign(p):
  'expression : ID GETS expression'
  rule.append(38)

  var = current_symbol_table[0].getVariable(p[1])
  if(var.datatype <> p[3].datatype and (var.datatype <> 'Int' and p[3].datatype <> 'Bool')):
    sys.exit("Type Check Error "+var.name+" is assigned "+p[3].datatype)

  code = p[3].code
  var1 = current_symbol_table[0].getVariable(p[1])

  if(current_symbol_table[0].search(p[3].place)):
    var2 = current_symbol_table[0].getVariable(p[3].place)
    expression_place = var2.changed_name
  else:
  	expression_place = p[3].place


  code.append('ASSIGN,' + get_expression_place(p[1]) +',' + get_expression_place(p[3].place))
  p[0] = TREE.Expression(code=code, datatype=p[3].datatype,place=p[3].place)

def p_expression_assign_arr(p):
  'expression : expression LSQRBRACKET expression RSQRBRACKET GETS expression'
  rule.append(39)
  var = current_symbol_table[0].getVariable(p[1].place)
 


  if(p[3].datatype <> 'Int'):
    sys.exit('Array index should be ineteger not '+p[3].datatype)

  if(var.datatype <> p[6].datatype and var.isArray):
    sys.exit("Type Check Error "+var.name+" is assigned "+p[3].datatype)
  code = p[1].code
  code.extend(p[6].code)
  code.extend(p[3].code)
  code.append('INDEX_ASSIGN_L,'+ get_expression_place(p[1].place) +','+get_expression_place(p[3].place)+','+get_expression_place(p[6].place))
  
  p[0] = TREE.Expression(code=code,place=p[6].place, datatype=p[6].datatype)


def p_expression_outint(p):
  'expression : OUT_INT LPAREN expression RPAREN'
  code = p[3].code
  if p[3].datatype not in  ['Int','Bool']:
    sys.exit("Type Check Error : out_int takes integer")
  code.append('PRINT_INT,'+get_expression_place(p[3].place))
  p[0]=TREE.FunctionCall(code=code)

def p_expression_outstring(p):
  'expression : OUT_STRING LPAREN expression RPAREN'
  code = p[3].code
  if p[3].datatype <> 'String':
    sys.exit("Type Check Error : out_string takes string")
  # code.append('SPACE')
  code.append('PRINT_STRING,'+get_expression_place(p[3].place))
  p[0]=TREE.FunctionCall(code=code)

def p_expression_scanint(p):
  'expression : SCAN_INT LPAREN expression RPAREN'
  code = p[3].code
  if p[3].datatype <> 'Int':
    sys.exit("Type Check Error : scan_int takes integer")
  code.append('SCAN_INT,'+get_expression_place(p[3].place))
  p[0]=TREE.FunctionCall(code=code)

def p_expression_scanstring(p):
  'expression : SCAN_STRING LPAREN expression RPAREN'
  code = p[3].code
  if p[3].datatype <> 'String':
    sys.exit("Type Check Error : scan_string takes string")
  code.append('SCAN_STRING,'+get_expression_place(p[3].place))
  p[0]=TREE.FunctionCall(code=code)

def p_expression_function_call_with_arguments_2(p):
  'expression : ID LPAREN argument_list RPAREN'
  rule.append(40)

  met = current_symbol_table[0].getMethod(p[1])

  
  t = newtemp()

  code = p[3].code
  function_args = ClassTable[met.parent_class].function_parameters[p[1]]
  if function_args <> p[3].nargs:
    sys.exit(met.name + " function takes %d"%met.nargs + " argument : Given %d"%p[3].nargs)
  code.append('FUNC_CALL,'+met.parent_class + '.' + p[1])
  code.append('READ_STACK,' + get_expression_place(t))
  datatype = met.datatype
  p[0]=TREE.FunctionCall(code=code, datatype=datatype, place=t)


def p_expression_function_call_2(p):
  'expression : ID LPAREN RPAREN'
  rule.append(41)
  met = current_symbol_table[0].getMethod(p[1])

  t=newtemp()

  function_args = ClassTable[met.parent_class].function_parameters[p[1]]
  if function_args <> 0:
    sys.exit(met.name + " function takes %d"%met.nargs + " argument : Given 0")

  code = ['FUNC_START']
  code.append('FUNC_CALL,'+met.parent_class +'.'+p[1])
  code.append('READ_STACK,'+get_expression_place(t))
  datatype = met.datatype
  p[0] = TREE.Expression(code=code,place=t, datatype=datatype)


def p_argument_list(p):
  'argument_list : expression'
  rule.append(42)

  # if current_symbol_table[0].search(p[1].place):
	 #  var = current_symbol_table[0].getVariable(p[1].place)
	 #  expression_place = var.changed_name
  # else:
		# expression_place = p[1].place

  code = p[1].code

  code.append('FUNC_START')
  code.append('FUNC_PARAM,{}'.format(get_expression_place(p[1].place)))
  p[0]=TREE.ArgumentList(code=code, place=p[1].place,nargs = 1)

def p_argument_list_many(p):
  'argument_list : argument_list COMMA expression'
  rule.append(43)
 


  code = p[1].code
  # code.append('FUNC_START')
  code.extend(p[3].code)
  code.append('FUNC_PARAM,{}'.format(get_expression_place(p[3].place)))

  p[0]=TREE.ArgumentList(code=code,place = p[3].place,nargs = p[1].nargs+1)

def p_expression_plus(p):
  'expression : expression PLUS expression'
  rule.append(44)



  if(p[1].datatype <> p[3].datatype or p[1].datatype <> 'Int' ):
    sys.exit("Type Check Error : "+p[1].datatype+" and "+p[3].datatype+" are getting added in "+p[1].place+" "+p[3].place)
  if(p[1].isArray or p[3].isArray):
    sys.exit("Type Check Error : "+p[1].place +" or "+p[3].place +" is array")
  t = newtemp()
  code = p[1].code
  code.extend(p[3].code)
  code.append('ADD,' + get_expression_place(t) + ',' + get_expression_place(p[1].place) + ',' + get_expression_place(p[3].place))

  p[0] = TREE.Expression(place = t, code = code, datatype = p[1].datatype)




def p_expression_minus(p):
  'expression : expression MINUS expression'
  rule.append(45)

  if(p[1].datatype <> p[3].datatype or p[1].datatype <> 'Int' ):
    sys.exit("Type Check Error : "+p[1].datatype+" and "+p[3].datatype+" are getting subtracted in "+p[1].place+" "+p[3].place)
  if(p[1].isArray or p[3].isArray):
    sys.exit("Type Check Error : "+p[1].place +" or "+p[3].place +" is array")
  t = newtemp()
  code = p[1].code
  code.extend(p[3].code)
  code.append('SUB,' + get_expression_place(t) + ',' +  get_expression_place(p[1].place) + ',' + get_expression_place(p[3].place))

  p[0] = TREE.Expression(place = t, code = code, datatype = p[1].datatype)

def p_expression_times(p):
  'expression : expression TIMES expression'
  rule.append(46)

  if(p[1].datatype <> p[3].datatype or p[1].datatype <> 'Int'):
    sys.exit("Type Check Error : "+p[1].datatype+" and "+p[3].datatype+" are getting multiplied in "+p[1].place+" "+p[3].place)
  if(p[1].isArray or p[3].isArray):
    sys.exit("Type Check Error : "+p[1].place +" or "+p[3].place +" is array")
  t = newtemp()
  code = p[1].code
  code.extend(p[3].code)
  code.append('MUL,' + get_expression_place(t) + ',' +  get_expression_place(p[1].place) + ',' + get_expression_place(p[3].place))

  p[0] = TREE.Expression(place = t, code = code, datatype = p[1].datatype)

def p_expression_divide(p):
  'expression : expression DIVIDE expression'
  rule.append(47)

  if(p[1].datatype <> p[3].datatype or p[1].datatype <> 'Int'):
    sys.exit("Type Check Error : "+p[1].datatype+" and "+p[3].datatype+" are getting divide in "+p[1].place+" "+p[3].place)
  if(p[1].isArray or p[3].isArray):
    sys.exit("Type Check Error : "+p[1].place +" or "+p[3].place +" is array")
  t = newtemp()
  code = p[1].code
  code.extend(p[3].code)
  code.append('DIV,' + get_expression_place(t) + ',' +  get_expression_place(p[1].place) + ',' + get_expression_place(p[3].place))

  p[0] = TREE.Expression(place = t, code = code, datatype = p[1].datatype)

def p_expression_mod(p):
  'expression : expression MOD expression'
  rule.append(48)

  if(p[1].datatype <> p[3].datatype or p[1].datatype <> 'Int'):
    sys.exit("Type Check Error : "+p[1].datatype+" and "+p[3].datatype+" are getting modulus in "+p[1].place+" "+p[3].place)
  if(p[1].isArray or p[3].isArray):
    sys.exit("Type Check Error : "+p[1].place +" or "+p[3].place +" is array")
  t = newtemp()
  code = p[1].code
  code.extend(p[3].code)
  code.append('MOD,' + get_expression_place(t) + ',' + get_expression_place(p[1].place) + ',' + get_expression_place(p[3].place))

  p[0] = TREE.Expression(place = t, code = code, datatype = p[1].datatype)

def p_expression_lt(p):
  'expression : expression LT expression'
  rule.append(49)

  if(p[1].datatype <> p[3].datatype or p[1].datatype not in  ['Int','Bool'] ):
    sys.exit("TYPE Check Error : Both "+p[1].place + " and "+p[3].place+" are NOT Int or Bool Type")
  if(p[1].isArray or p[3].isArray):
    sys.exit("Type Check Error : "+p[1].place +" or "+p[3].place +" is array")
  t = newtemp()
  # j_if = newjump()
  # j_fi = newjump()
 
  code = p[1].code
  code.extend(p[3].code)
  code.append('LESS_THAN,' + get_expression_place(t) + ',' +  get_expression_place(p[1].place) + ',' + get_expression_place(p[3].place))

  # code.append("IFGOTO,LESS_THAN," + p[1].place + ',' + p[3].place + ',' + j_if)
  # code.append("ASSIGN," + t + ',0')
  # code.append("GOTO," + j_fi)
  # code.append("LABEL,"+j_if)
  # code.append("ASSIGN," + t + ',1')
  # code.append("LABEL," + j_fi)

  p[0] = TREE.Expression(code = code, place = t, datatype = 'Bool')

def p_expression_gt(p):
  'expression : expression GT expression'
  rule.append(50)
  if(p[1].datatype <> p[3].datatype or p[1].datatype not in  ['Int','Bool']):
    sys.exit("TYPE Check Error : Both "+p[1].place + " and "+p[3].place+" are NOT Bool Type")

  if(p[1].isArray or p[3].isArray):
    sys.exit("Type Check Error : "+p[1].place +" or "+p[3].place +" is array")
  t = newtemp()
  j_if = newjump()
  j_fi = newjump()
  code = p[1].code
  code.extend(p[3].code)
  code.append('GREATER_THAN,' + get_expression_place(t) + ',' + get_expression_place(p[1].place) + ',' + get_expression_place(p[3].place))

  # code.append("IFGOTO,GREATER_THAN," + p[1].place + ',' + p[3].place + ',' + j_if)
  # code.append("ASSIGN," + t + ',0')
  # code.append("GOTO," + j_fi)
  # code.append("LABEL,"+j_if)
  # code.append("ASSIGN," + t + ',1')
  # code.append("LABEL," + j_fi)

  p[0] = TREE.Expression(code = code, place = t, datatype = 'Bool')


def p_expression_lteq(p):
  'expression : expression LTEQ expression'
  rule.append(51)
  if(p[1].datatype <> p[3].datatype or p[1].datatype not in  ['Int','Bool']):
    sys.exit("TYPE Check Error : Both "+p[1].place + " and "+p[3].place+" are NOT Bool Type")
  if(p[1].isArray or p[3].isArray):
    sys.exit("Type Check Error : "+p[1].place +" or "+p[3].place +" is array")

  t = newtemp()
  j_if = newjump()
  j_fi = newjump()
  code = p[1].code
  code.extend(p[3].code)
  code.append('LESS_THAN_EQUALS,' + get_expression_place(t) + ',' + get_expression_place(p[1].place) + ',' + get_expression_place(p[3].place))

  # code.append("IFGOTO,LESS_THAN_EQUALS," + p[1].place + ',' + p[3].place + ',' + j_if)
  # code.append("ASSIGN," + t + ',0')
  # code.append("GOTO," + j_fi)
  # code.append("LABEL,"+j_if)
  # code.append("ASSIGN," + t + ',1')
  # code.append("LABEL," + j_fi)

  p[0] = TREE.Expression(code = code, place = t, datatype = 'Bool')

def p_expression_gteq(p):
  'expression : expression GTEQ expression'
  rule.append(52)
  if(p[1].datatype <> p[3].datatype or p[1].datatype not in  ['Int','Bool']):
    sys.exit("TYPE Check Error : Both "+p[1].place + " and "+p[3].place+" are NOT Bool Type")

  if(p[1].isArray or p[3].isArray):
    sys.exit("Type Check Error : "+p[1].place +" or "+p[3].place +" is array")

  t = newtemp()
  j_if = newjump()
  j_fi = newjump()
  code = p[1].code
  code.extend(p[3].code)
  code.append('GREATER_THAN_EQUALS,' + get_expression_place(t) + ',' +  get_expression_place(p[1].place) + ',' + get_expression_place(p[3].place))


  # code.append("IFGOTO,GREATER_THAN_EQUALS," + p[1].place + ',' + p[3].place + ',' + j_if)
  # code.append("ASSIGN," + t + ',0')
  # code.append("GOTO," + j_fi)
  # code.append("LABEL,"+j_if)
  # code.append("ASSIGN," + t + ',1')
  # code.append("LABEL," + j_fi)

  p[0] = TREE.Expression(code = code, place = t, datatype = 'Bool')

def p_expression_equal(p):
  'expression : expression EQUAL expression'
  rule.append(53)
  
  if(p[1].datatype <> p[3].datatype or p[1].datatype not in  ['Int','Bool']):
    sys.exit("TYPE Check Error : Both "+p[1].place + " and "+p[3].place+" are NOT Bool/Int Type")

  if(p[1].isArray or p[3].isArray):
    sys.exit("Type Check Error : "+p[1].place +" or "+p[3].place +" is array")
  t = newtemp()
  j_if = newjump()
  j_fi = newjump()
  code = p[1].code
  code.extend(p[3].code)
  code.append('EQUALS,' + get_expression_place(t) + ',' + get_expression_place(p[1].place) + ',' + get_expression_place(p[3].place))


  # code.append("IFGOTO,EQUALS," + p[1].place + ',' + p[3].place + ',' + j_if)
  # code.append("ASSIGN," + t + ',0')
  # code.append("GOTO," + j_fi)
  # code.append("LABEL,"+j_if)
  # code.append("ASSIGN," + t + ',1')
  # code.append("LABEL," + j_fi)

  p[0] = TREE.Expression(code = code, place = t, datatype = 'Bool')

def p_expression_or(p):
  'expression : expression OR expression'
  rule.append(54)
  if(p[1].datatype <> p[3].datatype or p[1].datatype <> 'Bool'):
    sys.exit("TYPE Check Error : Both "+p[1].place + " and "+p[3].place+" are NOT Bool/Int Type")
  


  # t = newtemp()
  # code = p[1].code
  # code.extend(p[3].code)
  # code.append('ADD,' + t + ',' + p[1].place + ',' + p[3].place)

  t = newtemp()
  l1 = newjump()
  l2 = newjump()

  code = p[1].code
  code.append('IFGOTO,' + get_expression_place(p[1].place) + ',' + l1)
  code.extend(p[3].code)
  code.append('IFGOTO,' + get_expression_place(p[3].place) + ',' + l1)
  code.append('ASSIGN,' + get_expression_place(t) + ',0')
  code.append('GOTO,'+l2)
  code.append('LABEL,' + l1)
  code.append('ASSIGN,'+get_expression_place(t)+',1')
  code.append('LABEL,' + l2)

  p[0] = TREE.Expression(place = t, code = code, datatype = p[1].datatype)

def p_expression_and(p):
  'expression : expression AND expression'
  rule.append(55)
  if(p[1].datatype <> p[3].datatype or p[1].datatype <> 'Bool'):
    sys.exit("TYPE Check Error : Both "+p[1].place + " and "+p[3].place+" are NOT Bool Type")

  t = newtemp()
  l1 = newjump()
  l2 = newjump()

  code = p[1].code
  code.append('IFFALSE,' + get_expression_place(p[1].place) + ',' + l1)
  code.extend(p[3].code)
  code.append('IFFALSE,' + get_expression_place(p[3].place) + ',' + l1)
  code.append('ASSIGN,' + get_expression_place(t) + ',1')
  code.append('GOTO,'+l2)
  code.append('LABEL,' + l1)
  code.append('ASSIGN,'+get_expression_place(t)+',0')
  code.append('LABEL,' + l2)

  p[0] = TREE.Expression(place = t, code = code, datatype = p[1].datatype)

def p_expression_not(p):
  'expression : NOT expression'
  rule.append(56)
  if(p[2].datatype <> 'Bool'):
    sys.exit("TYPE Check Error : Both "+p[2].place + " is NOT Bool Type")

  t = newtemp()
  j_if = newjump()
  j_fi = newjump()
  code = p[2].code
  # code.append('LESS_THAN,' + t + ',' + p[1].place + ',' + p[3].place)
  code.append("IFGOTO,EQUALS," + get_expression_place(p[2].place) + ',0,' + j_if)
  code.append("ASSIGN," + get_expression_place(t) + ',0')
  code.append("GOTO," + j_fi)
  code.append("LABEL,"+j_if)
  code.append("ASSIGN," + get_expression_place(t) + ',1')
  code.append("LABEL," + j_fi)

  p[0] = TREE.Expression(code = code, place = t, datatype = p[2].datatype)

def p_expression_tilda(p):
  'expression : TILDA expression'
  rule.append(57)
  if(p[2].datatype <> 'Int'):
    sys.exit("TYPE Check Error : "+p[2].place+" is not Int Type")

  t = newtemp()
  code = p[2].code
  code.append('SUB,' + get_expression_place(t) + ',0,' + get_expression_place(p[2].place))

  p[0] = TREE.Expression(place = t, code = code, datatype = p[2].datatype,isArray=False)

def p_expression_paren(p):
  'expression : LPAREN expression RPAREN'
  rule.append(58)

  t = p[2].place
  code = p[2].code

  p[0] = TREE.Expression(place = t, code = code, datatype = p[2].datatype,isArray=p[2].isArray)

def p_expression_id(p):
  'expression : ID'
  rule.append(60)
  var = current_symbol_table[0].getVariable(p[1])
  t = p[1]

  p[0] = TREE.Expression(place = t, code=[],datatype=var.datatype,isArray=var.isArray)

def p_expression_arr(p):
  'expression : expression LSQRBRACKET expression RSQRBRACKET'
  rule.append(61)
  var = current_symbol_table[0].getVariable(p[1].place)


  t = newtemp(p[1].datatype)
  
  code = p[1].code
  code.extend(p[3].code)
  code.append('INDEX_ASSIGN_R,' + get_expression_place(t) + ',' + get_expression_place(p[1].place) + ',' + get_expression_place(p[3].place))
  p[0] = TREE.Expression(place = t, code = code, datatype=var.datatype,isArray=False)


def p_expression_integer(p):
  'expression : INTEGER'
  rule.append(62)

  p[0] = TREE.Expression(code=[], place=str(p[1]), datatype='Int',isArray=False)

def p_expression_string(p):
  'expression : STRING'
  rule.append(63)

  newstring(input_str = p[1])
  p[0] = TREE.Expression(place = "'" + p[1].replace("\n", "\\%c"%'n') + "'", datatype='String', code=[],isArray=False)

def p_expression_true(p):
  'expression : TRUE'
  rule.append(64)
  p[0] = TREE.Expression(place='1', code=[],datatype='Bool',isArray=False)

def p_expression_false(p):
  'expression : FALSE'
  rule.append(65)
  p[0] = TREE.Expression(place='0', code=[],datatype='Bool',isArray=False)

def p_expression_break(p):
  'expression : BREAK'
  rule.append(66)
  p[0] = TREE.Expression(place=None,code=['BREAK'],datatype='break',isArray=False)

def p_expression_continue(p):
  'expression : CONTINUE'
  rule.append(67)
  p[0] = TREE.Expression(code=['CONTINUE'],datatype='continue',isArray=False,place=None)

def p_expression_return(p):
  'expression : RETURN expression SEMICOLON'
  rule.append(67)
  func = [x.strip() for x in current_symbol_table[0].scope_name.split('.')][1]
  if current_symbol_table[0].getMethod(func).datatype <> p[2].datatype:
  	sys.exit("return type doesnot match for fucntion "+ func)
  changed_name = p[2].place
  if(p[2].datatype=='Int'):
    if(current_symbol_table[0].getVariable(p[2].place)):
      changed_name = current_symbol_table[0].getVariable(p[2].place).parent_scope_name+'.'+p[2].place
  code = p[2].code
  code.append('RETURN,'+changed_name)
  p[0] = TREE.Expression(code=code,datatype='continue',isArray=False,place=None)


def p_expression_function_call_with_arguments(p):
  'expression : expression PERIOD ID LPAREN argument_list RPAREN'
  rule.append(68)


  # if(p[3] == 'printdataSecure'):
  # exit()
  num = ClassTable[p[1].datatype].function_parameters[p[3]]
  if p[5].nargs + 1 <> num:
    sys.exit(p[3] + " takes %d"%(num) + " argument, Given %d"%p[5].nargs)
  if p[1].datatype not in ClassDict:
    sys.exit(p[1].datatype + " is not an class object ") 
  if( p[3] in ClassTable[p[1].datatype].privateFunctions and (currentClass[0] != p[1].datatype)):
    sys.exit("Call to private function......ERROR")

  t=newtemp()
  code = p[1].code
  code.extend(p[5].code)
  func_label = ClassTable[p[1].datatype].searchFunction(p[3])
  if(func_label == None):
    print("TYPE Check error, %s.%s function not defined"%(p[1].datatype, p[3]))
    exit()

  code.append('FUNC_PARAM,' + get_expression_place(p[1].place))
  code.append('FUNC_CALL,'+func_label)
  code.append('READ_STACK,' + get_expression_place(t))


  datatype = (ClassDict[current_symbol_table[0].getVariable(p[1].place).datatype].getMethod(p[3])).datatype
  p[0] = TREE.Expression(code=code,place=t,datatype=datatype,isArray=False)

def p_expression_function_call(p):
  'expression : expression PERIOD ID LPAREN RPAREN'
  rule.append(69)
  t=newtemp()
  num = ClassTable[p[1].datatype].function_parameters[p[3]]
  if 1 <> num:
    sys.exit(p[3] + " takes %d"%(num) + " argument, Given 1")
  
  if( p[3] in ClassTable[p[1].datatype].privateFunctions and (currentClass[0] != p[1].datatype)):
    sys.exit("Call to private function......ERROR")

  code = p[1].code


  func_label = ClassTable[p[1].datatype].searchFunction(p[3])
  if(func_label == None):
    print("TYPE Check error, %s.%s function not defined"%(p[1].datatype, p[3]))
    exit()

  code.append('FUNC_START')
  code.append('FUNC_PARAM,' + get_expression_place( p[1].place))
  code.append('FUNC_CALL,'+func_label)
  code.append('READ_STACK,' + get_expression_place( t))
  datatype = (ClassDict[current_symbol_table[0].getVariable(p[1].place).datatype].getMethod(p[3])).datatype
  p[0] = TREE.Expression(code=code,place=t, datatype=datatype,isArray=False)

def p_expression_new(p):
  'expression : NEW type'
  rule.append(70)


  t=newtemp(p[2].place)
  current_symbol_table[0].getVariable(t).datatype = p[2].place

  if(p[2].place not in ClassTable):
    print("CLASS %s not defined "%(p[2].place))
    exit()


  size = ClassTable[p[2].place].size
  code = ['ALLOCATE,' + get_expression_place(t) + ',' + str(size)]
  for name in ClassTable[p[2].place].variables:
    var = ClassDict[p[2].place].getVariable(name)
    if var.isArray:
      t2  = newtemp()
      code.append('ALLOCATE,%s,'%get_expression_place(t2) + str(var.size))
      code.append('INDEX_ASSIGN_L,%s,%d,%s'%(get_expression_place(t),ClassTable[p[2].place].variables[name],get_expression_place(t2)))

  p[0] = TREE.Expression(code=code,place=t, datatype=p[2].place)

def p_expression_isvoid(p):
  'expression : ISVOID expression'
  rule.append(71)
  # t=newtemp()
  # code = ['FUNC_CALL,isvoid']
  # code.append('READ_STACK,' + t)
  # p[0] = TREE.Expression(code=code,place=t, datatype='isvoid')
  code = p[2].code
  t = newtemp()
  code.append('EQUALS,'+get_expression_place(t)+',0,'+get_expression_place(p[2].place))
  p[0] = TREE.Expression(code=code,place=t, datatype='Bool')


def p_expression_let_expression(p):
  'expression : let_expression'
  rule.append(72)
  p[0] = TREE.Expression(code = p[1].code, datatype='let')


def p_let_to_let(p):
  'let : LET'

  let_id = newLet()

  code = ['LABEL,' + 'LET_BEGIN_' + current_symbol_table[0].scope_name + '.'+ str(let_id)]
  new_sym_tab = Symtab(parent=current_symbol_table[0], symtab_type='LET', scope_name=current_symbol_table[0].scope_name + '.' + str(let_id))
  current_symbol_table[0].lets.append(new_sym_tab)
  SymbolTables.append(new_sym_tab)
  current_symbol_table[0] = new_sym_tab

  p[0]=TREE.Let(code=code, datatype='',let_id=let_id)


def p_let_expression(p):
  'let_expression : let formaldehyde IN expression TEL'
  rule.append(73)

  code = p[1].code
  code.extend(p[2].code)

  code.extend(p[4].code)
  code.append('LABEL,LET_OVER_'+str(p[1].let_id))
  p[0] = TREE.Let(code = code, datatype=p[4].datatype)

  current_symbol_table[0] = current_symbol_table[0].parent




def p_expression_at_function_with_arguments(p):
  'expression : expression AT CLASS_TYPE PERIOD ID LPAREN argument_list RPAREN'
  rule.append(74)
  t=newtemp()
  code = p[1].code
  code.extend(p[7].code)
  func_label = ClassTable[p[3]].searchFunction(p[5])

  if( p[5] in ClassTable[p[3].datatype].privateFunctions):
    sys.exit("Call to private function......ERROR")

  if(func_label == None):
    print("TYPE Check error, %s.%s function not defined"%(p[1].datatype, p[3]))
    exit()

  code.append('FUNC_PARAM,' + get_expression_place(p[1].place))
  code.append('FUNC_CALL,'+func_label)
  code.append('READ_STACK,' + get_expression_place(t))

  datatype = (ClassDict[p[3]].getMethod(p[5])).datatype
  p[0] = TREE.Expression(code=code,place=t,datatype=datatype,isArray=False)

def p_expression_at_function(p):
  'expression : expression AT CLASS_TYPE PERIOD ID LPAREN RPAREN'
  rule.append(75)

  if( p[5] in ClassTable[p[3].datatype].privateFunctions):
    sys.exit("Call to private function......ERROR")


  t=newtemp()
  code = p[1].code
  # code.extend(p[7].code)
  func_label = ClassTable[p[3]].searchFunction(p[5])
  if(func_label == None):
    print("TYPE Check error, %s.%s function not defined"%(p[1].datatype, p[3]))
    exit()

  code.append('FUNC_PARAM,' + get_expression_place(p[1].place))
  code.append('FUNC_CALL,'+func_label)
  code.append('READ_STACK,' + get_expression_place(t))

  datatype = (ClassDict[p[3]].getMethod(p[5])).datatype
  p[0] = TREE.Expression(code=code,place=t,datatype=datatype,isArray=False)


def p_expression_if_then_else(p):
  'expression : if_then_else'
  rule.append(76)

  p[0] = TREE.Expression(code=p[1].code, datatype='if_then_else')

def p_if_then_else(p):
  'if_then_else : IF expression THEN expression ELSE expression FI'
  rule.append(77)

  _if = newjump()
  _fi = newjump()
  code=p[2].code
  code.append('IFGOTO,' + get_expression_place(p[2].place) + ',' +  _if)
  code.extend(p[6].code)
  code.append('GOTO,' + _fi)
  code.append('LABEL,' + _if)
  code.extend(p[4].code)
  code.append('LABEL,'+_fi)

  p[0] = TREE.If_Then_Else(code=code, datatype='if')

def p_expression_while(p):
  'expression : while'
  rule.append(78)

  p[0] = TREE.Expression(code=p[1].code, datatype='while')


def p_while(p):
  'while : WHILE expression LOOP expression POOL'
  rule.append(79)


  _loop = newjump()
  _pool = newjump()
  code = ['LABEL,' + _loop]
  code.extend(p[2].code)
  code.append('IFGOTO,EQUALS,' + get_expression_place(p[2].place) + ',0,' +  _pool)
  code.extend(p[4].code)
  code.append('GOTO,'+_loop)
  code.append('LABEL,'+_pool)
  for i in range(len(code)):
    if(code[i]=='BREAK'):
      code[i]='GOTO,'+_pool
    elif(code[i]=='CONTINUE'):
      code[i]='GOTO,'+_loop

  p[0] = TREE.While(code=code, datatype=p[4].datatype)


def p_expression_for(p):
  'expression : for'
  rule.append(80)

  p[0] = TREE.Expression(code=p[1].code, datatype='for')

def p_for(p):
  'for : FOR LPAREN expression SEMICOLON expression SEMICOLON expression RPAREN LOOP expression POOL'
  rule.append(81)

  _loop = newjump()
  _pool = newjump()
  _update = newjump()

  code = p[3].code
  code.append('LABEL,' + _loop)
  code.extend(p[5].code)
  code.append('IFGOTO,EQUALS,'+get_expression_place(p[5].place)+',0,' + _pool)
  code.extend(p[10].code)
  code.append('LABEL,' + _update)
  code.extend(p[7].code)
  code.append('GOTO,'+ _loop)
  code.append('LABEL,' + _pool)

  for i in range(len(code)):
    if(code[i]=='BREAK'):
      code[i]='GOTO,'+_pool
    elif(code[i]=='CONTINUE'):
      code[i]='GOTO,'+_update

  p[0] = TREE.For(code=code, datatype=p[10].datatype)


def p_formaldehyde_with_assign_many(p):
  'formaldehyde : formaldehyde COMMA ID COLON type GETS expression'
  # rule.append(31)
  current_symbol_table[0].enter(name=p[3],changed_name=current_symbol_table[0].scope_name +'.'+p[3], datatype=p[5].place,size=4, isArray =False)
  code = p[7].code
  code.append(p[1].code)
  code.append('ASSIGN,%s,%s'%(current_symbol_table[0].scope_name + '.' + p[3], get_expression_place(p[7].place)))

  if p[5].place in ClassDict or p[5].place in basicDataType:
    pass
  else:
    sys.exit('No object found named ' + p[3].place)

  p[0]=TREE.Formal(code=code, name = None)



def p_formaldehyde_many(p):
  'formaldehyde : formaldehyde COMMA ID COLON type'
  # rule.append(32)
  code = p[1].code
  p[0]=TREE.Formal(code=code,name = None)
  # quit()
  if p[5].place in ClassDict or p[5].place in basicDataType:
    pass
  else:
    sys.exit('No object found named ' + p[3].place)

  current_symbol_table[0].enter(name=p[3],changed_name=current_symbol_table[0].scope_name +'.' +p[3],datatype=p[5].place,size=4, isArray =False)


def p_formaldehyde_arr_many(p):
  'formaldehyde : formaldehyde COMMA ID COLON type LSQRBRACKET expression RSQRBRACKET'
  # rule.append(33)
  current_symbol_table[0].enter(name= p[3],changed_name=current_symbol_table[0].scope_name +'.' +p[3],datatype=p[5].place, size=4*int(p[7].place), isArray =True)

  code = p[1].code
  code.extend(p[7].code)
  code.append('ALLOCATE,' + current_symbol_table[0].scope_name + '.' + p[3] + ',' + get_expression_place(p[7].place))
  p[0]=TREE.Formal(code=code,name = None)
  if p[5].place in ClassDict or p[5].place in basicDataType:
    pass
  else:
    sys.exit('No object found named ' + p[3].place)



def p_formaldehyde_with_assign(p):
  'formaldehyde : ID COLON type GETS expression'
  # rule.append(31)
  current_symbol_table[0].enter(name=p[1],changed_name=current_symbol_table[0].scope_name +'.' +p[1],datatype=p[3].place,size=4, isArray =False)

  code = p[5].code
  code.append('ASSIGN,%s,%s'%(current_symbol_table[0].scope_name + '.'+p[1], get_expression_place(p[5].place)))
  # p[0] = TREE.SymTabEntry(id=p[1], datatype=p[3].datatype, code=code)
  p[0]=TREE.Formal(code=code,name = None)
  if p[3].place in ClassDict or p[3].place in basicDataType:
    pass
  else:
    sys.exit('No object found named ' + p[3].place)


def p_formaldehyde(p):
  'formaldehyde : ID COLON type'
  # rule.append(32)
  p[0]=TREE.Formal(code=[],name = None)
  current_symbol_table[0].enter(name=p[1], changed_name=current_symbol_table[0].scope_name +'.' +p[1] ,datatype=p[3].place, size=4, isArray =False)
  if p[3].place in ClassDict or p[3].place in basicDataType:
    pass
  else:
    sys.exit('No object found named ' + p[3].place)


def p_formaldehyde_arr(p):
  'formaldehyde : ID COLON type LSQRBRACKET expression RSQRBRACKET'
  # rule.append(33)
  code=p[5].code
  code.append('ALLOCATE,' + current_symbol_table[0].scope_name + '.' + p[1] + ',' + p[5].place)
  p[0]=TREE.Formal(code=code,name = None)


  if p[3].place in ClassDict or p[3].place in basicDataType:
    pass
  else:
    sys.exit('No object found named ' + p[3].place)


  current_symbol_table[0].enter(name=p[1],changed_name=current_symbol_table[0].scope_name +'.' +p[1],datatype=p[3].place,size=4, isArray =True)





def p_expression_objid(p):
  'expression : expression PERIOD ID'

  code=p[1].code

  if p[3] in ClassTable[p[1].datatype].private and currentClass[0] <> p[1].datatype:
    sys.exit("Accessing private variable" + p[3] + " of class "+p[1].datatype)

  if p[3] in ClassTable[p[1].datatype].parentprivatevariables:
    sys.exit("Accessing ancestor's private variable" + p[3] + " in class "+p[1].datatype)


  var = ClassDict[p[1].datatype].getVariable(p[3])

  if(var.name not in ClassTable[ p[1].datatype ].variables):
    sys.exit("Accessing Unknown variable " + p[3] + " of class "+p[1].datatype)


  datatype = var.datatype
  offset = ClassTable[ p[1].datatype ].variables[p[3]]


  t = newtemp(datatype)
  code.append('INDEX_ASSIGN_R,' + get_expression_place(t) + ',' + get_expression_place(p[1].place) + ',' + str(offset))

  p[0] = TREE.Expression(place = t, code = code, datatype=datatype,isArray=False)


def p_expression_objid_expression(p):
  'expression : expression PERIOD ID GETS expression'

  code = p[1].code
  code.extend(p[5].code)
  if p[3] in ClassTable[p[1].datatype].private and currentClass[0] <> p[1].datatype:
    sys.exit("Accessing private variable" + p[3] + " of class "+p[1].datatype)

  if p[3] in ClassTable[p[1].datatype].parentprivatevariables:
    sys.exit("Accessing ancestor's private variable" + p[3] + " in class "+p[1].datatype)


  var = ClassDict[p[1].datatype].getVariable(p[3])

  if(var.name not in ClassTable[ p[1].datatype ].variables):
    sys.exit("Accessing Unknown variable " + p[3] + " of class "+p[1].datatype)

  offset = ClassTable[ p[1].datatype ].variables[p[3]]
  code.append('INDEX_ASSIGN_L,'+ get_expression_place(p[1].place) +','+str(offset)+','+get_expression_place(p[5].place))
  
  p[0] = TREE.Expression(code=code,place=p[5].place, datatype=p[5].datatype)


def p_read_file(p):
  'expression : READ_FILE LPAREN ID COMMA expression RPAREN'

  if(p[5].datatype != 'String'):
    sys.exit('Invalid File name')


  code = p[5].code
  code.append('READ_FILE,' + get_expression_place(p[3]) + ',' + get_expression_place(p[5].place))
  p[0]=TREE.Expression(code=code, datatype=p[5].datatype)


def p_write_file(p):
  'expression : WRITE_FILE LPAREN expression COMMA expression RPAREN'

  if(p[5].datatype != 'String'):
    sys.exit('Invalid File name')

  if(p[3].datatype != 'String'):
    sys.exit('Can only write strings in file')

  code = p[5].code
  code.append('WRITE_FILE,' + get_expression_place(p[3].place) + ',' + get_expression_place(p[5].place))
  p[0]=TREE.Expression(code=code, datatype=p[5].datatype)



# def p_expression_self(p):
#   'expression : SELF'
#   rule.append(59)

#   p[0] = TREE.Expression(code=[], place='self', datatype=currentClass[0])


def p_error(p):
  """Error rule for Syntax Errors handling and reporting."""
  print("-------------------------- Error ---------------------------------")
  if p is None:
    print("Error! Unexpected end of input!")
  else:
    error = "Syntax error! Line: {}, position: {}, character: {}, type: {}".format(p.lineno, p.lexpos, p.value, p.type)
    print(error)
    print type(p.type)
  print("Exiting .....")
  exit()

parser  = yacc.yacc()




input_file = sys.argv[1]
with open(input_file) as file:
    data = file.read()
parser.parse(data)


for s in SymbolTables:
  print("===========")
  s.printsymtab()
print("===========")



print(len(SymbolTables))
for t in ClassTable:
  print ClassTable[t].printClass()

print(".... Parsing .... done ....")
main(SymbolTables, String_Dict)
print String_Dict