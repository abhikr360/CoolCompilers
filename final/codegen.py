#!/usr/bin/env python

from enum import Enum
import csv
import sys
import numpy as np
import os
import re


# Global DS #
MethodSize={}
basic_block_list = []
LocalSymbolTable={}
RegisterDescriptor={'HI': 0, 'LO' : 0, 'r0' : 0, 'at' : 0, 'v0' : 0, 'v1' : 0, 'a0' : 0, 'a1' : 0, 'a2' : 0, 'a3' : 0, 't0' : 0, 't1' : 0, 't2' : 0, 't3' : 0, 't4' : 0, 't5' : 0, 't6' : 0, 't7' : 0, 's0' : 0, 's1' : 0, 's2' : 0, 's3' : 0, 's4' : 0, 's5' : 0, 's6' : 0, 's7' : 0, 't8' : 0, 't9' : 0, 'k0' : 0, 'k1' : 0, 's8' : 0, 'ra' : 0}
addressDescriptor={}
NextUse={}

UsableRegistersTemp = {'t0' : 0, 't1' : 0, 't2' : 0, 't3' : 0, 't4' : 0, 't5' : 0, 't6' : 0}
UsableRegistersGlobal = {'s0' : 0, 's1' : 0, 's2' : 0, 's3' : 0, 's4' : 0, 's5' : 0, 's6' : 0}
UsableRegisters = {'t0' : 0, 't1' : 0, 't2' : 0, 't3' : 0, 't4' : 0, 't5' : 0, 's0' : 0, 's1' : 0, 's2' : 0, 's3' : 0, 's4' : 0, 's5' : 0, 's6' : 0}

TempRegisters = {'$t6' : 0,'t7' : 0, 't8' : 0, 't9' : 0}
VariableData = {}
block_codes = {}

current_symbol_table = [None]
previousSymbolTables = []

readingfromstack=[0]

def is_int(row):
	try:
		temp = int(row)
		return True
	except Exception as e:
		return False

def is_string(row):
	if is_int(row):
		return False
	elif (row[0] == '"' and row[len(row)-1] == '"') or (row[0] == "'" and row[len(row)-1] == "'"):
		return True
	return False

class InstrType(Enum):
	'''Any Instruction in three Address code can be of one of these types'''
	ASSIGN = 1
	GOTO = 2
	IFGOTO = 3
	INDEX_ASSIGN_L = 4
	INDEX_ASSIGN_R = 5
	FUNC_PARAM = 6
	FUNC_CALL = 7
	FUNC_RETURN = 8
	LABEL = 9
	SCAN_INT = 10
	SCAN_STRING = 11
	PRINT_INT = 12
	PRINT_STRING = 13
	EXIT=14
	SPACE=15
	FUNC_LABEL=16
	IFFALSE=17
	FUNC_START=18
	POP_STACK=19
	RETURN=20
	ALLOCATE=21
	READ_FILE=22
	WRITE_FILE=23


class EntryType(Enum):
	'''Data Type of variable in three address code'''
	INTEGER = 1
	VARIABLE = 2
	STRING = 3

class Operator(Enum):
	''' Operators available in our three address code'''
	LESS_THAN = 1
	GREATER_THAN = 2
	LESS_THAN_EQUALS = 3
	GREATER_THAN_EQUALS = 4
	EQUALS = 5
	NOT_EQUALS = 6
	ADD = 7
	SUB = 8
	MUL = 9
	DIV = 10
	MOD = 11
	READ_STACK=12

class statement:
	''' A instruction in three address code'''
	def __init__(self):
		self.linenum =  None
		self.instr_typ = None
		self.operator = None
		self.in1 = None
		self.in1_type = None
		self.in2 = None
		self.in2_type = None
		self.out = None
		self.out_type = None
		self.jump_tagret = None
		self.label = None
		self.code_statement = ""

	def print_stmt(self):
		'''Print an instruction'''
		print(self.linenum,self.instr_typ,self.operator,self.in1,self.in1_type,self.in2,self.in2_type,self.out,self.jump_tagret,self.label)

def set_inputs(row, curr_statement):
	'''Reads input stores it in a list of classes'''
	curr_statement.linenum = int(row[0])
	#------------------------------------------------
	assign_list = ["LESS_THAN", "GREATER_THAN", "LESS_THAN_EQUALS", "GREATER_THAN_EQUALS", "EQUALS", "NOT_EQUALS", "ADD", "SUB", "MUL", "DIV", "MOD", "READ_STACK"]
	if(row[1] == "ASSIGN" or row[1] in assign_list):
		curr_statement.instr_typ = InstrType.ASSIGN
		if(row[1] in assign_list):
			exec("curr_statement.operator = Operator.%s" %(row[1]))
	else:
		exec("curr_statement.instr_typ = InstrType.%s" %(row[1]))


	#         --------------- For row 2 ----------------------

	if(curr_statement.instr_typ == InstrType.ASSIGN):
		if(curr_statement.operator == Operator.READ_STACK):
			curr_statement.out=row[2]
			curr_statement.out_type = EntryType.VARIABLE
		if(curr_statement.operator <> None and curr_statement.operator <> Operator.READ_STACK ):					#for statements of type a = b + 2
			curr_statement.out = row[2]
			curr_statement.out_type = EntryType.VARIABLE

			if(is_int(row[3])):
				curr_statement.in1 = int(row[3])
				curr_statement.in1_type = EntryType.INTEGER
			elif(is_string(row[3])):
				curr_statement.in1 = (row[3])
				curr_statement.in1_type = EntryType.STRING
				# print "-------11111111111-------------111111111----------1111"
			else:
				curr_statement.in1 = (row[3])
				curr_statement.in1_type = EntryType.VARIABLE
			try:
				temp = int(row[4])
				curr_statement.in2 = temp
				curr_statement.in2_type = EntryType.INTEGER
			except Exception as e:
				temp = row[4]
				curr_statement.in2 = temp
				curr_statement.in2_type = EntryType.VARIABLE
		elif(curr_statement.operator <> Operator.READ_STACK):
			curr_statement.out = row[2]
			curr_statement.out_type = EntryType.VARIABLE
			if(is_int(row[3])):
				curr_statement.in1 = int(row[3])
				curr_statement.in1_type = EntryType.INTEGER
			elif(is_string(row[3])):
				curr_statement.in1 = (row[3])
				curr_statement.in1_type = EntryType.STRING
				# print "-------11111111111-------------111111111----------1111"
			else:
				curr_statement.in1 = (row[3])
				curr_statement.in1_type = EntryType.VARIABLE

	elif(curr_statement.instr_typ == InstrType.IFGOTO):
		if(len(row)>4):
			exec("curr_statement.operator = Operator.%s" %(row[2]))
			curr_statement.jump_tagret = row[5]
			try:
				temp = int(row[3])
				curr_statement.in1 = temp
				curr_statement.in1_type = EntryType.INTEGER
			except Exception as e:
				temp = row[3]
				curr_statement.in1 = temp
				curr_statement.in1_type = EntryType.VARIABLE

			try:
				temp = int(row[4])
				curr_statement.in2 = temp
				curr_statement.in2_type = EntryType.INTEGER
			except Exception as e:
				temp = row[4]
				curr_statement.in2 = temp
				curr_statement.in2_type = EntryType.VARIABLE
		else:
			curr_statement.jump_tagret = row[3]
			curr_statement.operator = ''
			try:
				temp = int(row[4])
				curr_statement.in1 = temp
				curr_statement.in1_type = EntryType.INTEGER
			except Exception as e:
				temp = row[2]
				curr_statement.in1 = temp
				curr_statement.in1_type = EntryType.VARIABLE
			curr_statement.in2 = 0
			curr_statement.in2_type = EntryType.INTEGER


	elif(curr_statement.instr_typ == InstrType.IFFALSE):
		curr_statement.jump_tagret = row[3]
		curr_statement.operator = ''
		try:
			temp = int(row[2])
			curr_statement.in1 = temp
			curr_statement.in1_type = EntryType.INTEGER
		except Exception as e:
			temp = row[2]
			curr_statement.in1 = temp
			curr_statement.in1_type = EntryType.VARIABLE
		curr_statement.in2 = 0
		curr_statement.in2_type = EntryType.INTEGER


	elif(curr_statement.instr_typ == InstrType.INDEX_ASSIGN_L):			# OUT[IN1] = IN2
		curr_statement.out = row[2]
		curr_statement.out_type = EntryType.VARIABLE
		
		if(is_int(row[3])):
			curr_statement.in1 = int(row[3])
			curr_statement.in1_type = EntryType.INTEGER
		else:
			curr_statement.in1 = row[3]
			curr_statement.in1_type = EntryType.VARIABLE

		if(is_int(row[4])):
			curr_statement.in2 = int(row[4])
			curr_statement.in2_type = EntryType.INTEGER
		else:
			curr_statement.in2 = row[4]
			curr_statement.in2_type = EntryType.VARIABLE

	elif(curr_statement.instr_typ == InstrType.INDEX_ASSIGN_R):			# OUT = IN1[IN2]
		curr_statement.out = row[2]
		curr_statement.out_type = EntryType.VARIABLE
		
		curr_statement.in1 = row[3]
		curr_statement.in1_type = EntryType.VARIABLE

		if(is_int(row[4])):
			curr_statement.in2 = int(row[4])
			curr_statement.in2_type = EntryType.INTEGER
		else:
			curr_statement.in2 = row[4]
			curr_statement.in2_type = EntryType.VARIABLE

	elif(curr_statement.instr_typ == InstrType.LABEL):
		curr_statement.label = row[2]
	elif(curr_statement.instr_typ == InstrType.FUNC_LABEL):
		curr_statement.label = row[2]

	elif(curr_statement.instr_typ == InstrType.FUNC_CALL):
		curr_statement.jump_tagret = row[2]

	elif(curr_statement.instr_typ == InstrType.GOTO):
		curr_statement.jump_tagret = row[2]


	elif(curr_statement.instr_typ == InstrType.FUNC_PARAM):
		if(is_int(row[2])):
				curr_statement.in1 = int(row[2])
				curr_statement.in1_type = EntryType.INTEGER
		elif(is_string(row[2])):
			curr_statement.in1 = (row[2])
			curr_statement.in1_type = EntryType.STRING
		else:
			curr_statement.in1 = (row[2])
			curr_statement.in1_type = EntryType.VARIABLE

	elif(curr_statement.instr_typ == InstrType.RETURN):
		if(is_int(row[2])):
				curr_statement.out = int(row[2])
				curr_statement.out_type = EntryType.INTEGER
		elif(is_string(row[2])):
			curr_statement.out = (row[2])
			curr_statement.out_type = EntryType.STRING
		else:
			curr_statement.out = (row[2])
			curr_statement.out_type = EntryType.VARIABLE

	elif(curr_statement.instr_typ == InstrType.SCAN_INT or curr_statement.instr_typ == InstrType.PRINT_INT):
		try:
			temp = int(row[2])
			curr_statement.in1 = temp
			curr_statement.in1_type = EntryType.INTEGER
		except Exception as e:
			temp = row[2]
			curr_statement.in1 = temp
			curr_statement.in1_type = EntryType.VARIABLE
		if(len(row)==4):
			try:
				temp = int(row[3])
				curr_statement.in2 = temp
				curr_statement.in2_type = EntryType.INTEGER
			except Exception as e:
				temp = row[3]
				curr_statement.in2 = temp
				curr_statement.in2_type = EntryType.VARIABLE

	elif(curr_statement.instr_typ == InstrType.SCAN_STRING or curr_statement.instr_typ == InstrType.PRINT_STRING):
		if is_string(row[2]):
			curr_statement.in1 = row[2]
			curr_statement.in1_type = EntryType.STRING
		else:
			curr_statement.in1 = row[2]
			curr_statement.in1_type = EntryType.VARIABLE

	elif(curr_statement.instr_typ == InstrType.ALLOCATE):
		curr_statement.out = row[2]
		curr_statement.out_type = EntryType.VARIABLE
		if(is_int(row[3])):
			curr_statement.in1 = int(row[3])
			curr_statement.in1_type = EntryType.INTEGER
		else:
			curr_statement.in1 = row[3]
			curr_statement.in1_type = EntryType.VARIABLE

	elif(curr_statement.instr_typ == InstrType.READ_FILE):
		curr_statement.out = row[2]
		curr_statement.out_type = EntryType.VARIABLE

		if(is_string(row[3])):
			curr_statement.in1 = row[3]
			curr_statement.in1_type = EntryType.STRING
		else:
			curr_statement.in1 = row[3]
			curr_statement.in1_type = EntryType.VARIABLE


	elif(curr_statement.instr_typ == InstrType.WRITE_FILE):

		if(is_string(row[2])):
			curr_statement.in1 = row[2]
			curr_statement.in1_type = EntryType.STRING
		else:
			curr_statement.in1 = row[2]
			curr_statement.in1_type = EntryType.VARIABLE

		if(is_string(row[3])):
			curr_statement.in2 = row[3]
			curr_statement.in2_type = EntryType.STRING
		else:
			curr_statement.in2 = row[3]
			curr_statement.in2_type = EntryType.VARIABLE


	#-------------------row 2 end -------------------
	##print(curr_statement.linenum, curr_statement.instr_typ, curr_statement.operator,curr_statement.out,curr_statement.in1,curr_statement.in2)

class Scope(Enum):
	''' Scope of a variable'''
	GLOBAL = 1
	LOCAL = 2

def lookup_LocalSymbolTable(s):
	''' Search in symbol table'''
	# return current_symbol_table[0].getVariable(s)
	if s <> None and s <> '':
		# print "searhcing for variable : " + s
		# if 't.' in s:
		# 	sym_entry = LocalSymTabEntry(size=int(s[2:]),dataType='Temp',isArray=False)
		# 	# insert_LocalSymbolTable(s,sym_entry)
		# 	return sym_entry
		if(s in LocalSymbolTable.keys() and s !=''):
			return LocalSymbolTable[s]
		else:
			return None

def insert_LocalSymbolTable(s, symbolTableEntry):
	'''Insert into symbol table'''
	if(s==""):
		print("symbolName Cannot be empty.....Aborting !!")
		exit()
	else:
		LocalSymbolTable[s]=symbolTableEntry

class LocalSymTabEntry:
	'''One entry of symbol table'''
	def __init__(self, size=4, dataType="Int", scope=Scope.GLOBAL, isLive=False, nextUse=np.inf, isArray = False):
		self.isLive=isLive
		self.nextUse=nextUse
		self.dataType=dataType
		self.scope=scope
		self.size=size
		self.isArray = isArray

class NextUseEntry:
	"""for each line : for all three variables involved their next use and is live information"""
	def __init__(self, in1, in2, out, in1nextuse, in2nextuse, outnextuse, in1islive, in2islive, outislive):
		self.in1 = in1
		self.in2 = in2
		self.out = out
		self.in1nextuse = in1nextuse
		self.in2nextuse = in2nextuse
		self.outnextuse = outnextuse
		self.in1islive = in1islive
		self.in2islive = in2islive
		self.outislive = outislive

def construct_NextUse():
	# print("here")
	# print(len(basic_block_list))
	for basic_block in basic_block_list:
		#Flush Symbol table's nextuse islive information
		for x in LocalSymbolTable:
			LocalSymbolTable[x].isLive = False
			LocalSymbolTable[x].nextUse = np.inf


		for stmt in reversed(basic_block):
			in1=""
			in2=""
			out=""
			# stmt.#print_stmt()
			if(stmt.in1_type == EntryType.VARIABLE):
				in1=stmt.in1
			if(stmt.in2_type == EntryType.VARIABLE):
				in2=stmt.in2
			if(stmt.out_type == EntryType.VARIABLE):
				out = stmt.out
			in1nextuse=np.inf
			in2nextuse=np.inf
			outnextuse=np.inf
			in1islive=False
			in2islive=False
			outislive=False


			ste1 = lookup_LocalSymbolTable(in1)
			ste2 = lookup_LocalSymbolTable(in2)
			steo = lookup_LocalSymbolTable(out)
			if(out):
				if(steo):
					# if(steo.dataType <> 'Temp'):
					outnextuse=steo.nextUse
					outislive=steo.isLive
					steo.nextUse=np.inf
					steo.isLive=False
					LocalSymbolTable[out]=steo
				else:
					print LocalSymbolTable
					print("No entry for this variable in out LocalSymbolTable" + str(out))
					stmt.print_stmt()
					# s=LocalSymTabEntry()
					# insert_LocalSymbolTable(out,s)
			if(in1):
				if(ste1):
					# if(ste1.dataType <> 'Temp'):
					in1nextuse=ste1.nextUse
					in1islive=ste1.isLive
					ste1.nextUse=stmt.linenum
					ste1.isLive=True
					LocalSymbolTable[in1]=ste1
				else:
					# s=LocalSymTabEntry(True, stmt.linenum)
					# insert_LocalSymbolTable(in1,s)
					print("No entry for this variable in in1 LocalSymbolTable" + str(in1))
			if(in2):
				if(ste2):
					# if(ste2.dataType <> 'Temp'):
					in2nextuse=ste2.nextUse
					in2islive=ste2.isLive
					ste2.nextUse=stmt.linenum
					ste2.isLive=True
					LocalSymbolTable[in2]=ste2
				else:
					# s=LocalSymTabEntry(True, stmt.linenum)
					# insert_LocalSymbolTable(in2,s)
					print("No entry for this variable in in2 LocalSymbolTable" + str(in2))
			

			nue = NextUseEntry(in1, in2, out, in1nextuse, in2nextuse, outnextuse, in1islive, in2islive, outislive)
			NextUse[stmt.linenum]=nue



# farthest and in variable data and usableregister   what about equality
def constructEvictionCandidate(cur_line, basic_block):
	EvictionCandidates={}



	for stmt in reversed(basic_block):
		# print(int(stmt.linenum), int(cur_line.linenum), int(stmt.linenum) > int(cur_line.linenum))
		if(stmt.linenum > cur_line.linenum):
			if(stmt.in1_type == EntryType.VARIABLE and VariableData[stmt.in1][1] != 0 and (stmt.in1 != cur_line.in1 and stmt.in1 !=cur_line.in2 and stmt.in1 != cur_line.out)) :
				EvictionCandidates[stmt.in1] = stmt.linenum
			if(stmt.in2_type == EntryType.VARIABLE and VariableData[stmt.in2][1] != 0 and (stmt.in2 != cur_line.in1 and stmt.in2 !=cur_line.in2 and stmt.in2 != cur_line.out)) :
				EvictionCandidates[stmt.in2] = stmt.linenum
			# if(VariableData[stmt.out][1] != 0 and (stmt.out != cur_line.in1 and stmt.out != cur_line.in2 and stmt.out != cur_line.out)) :
			# 	EvictionCandidates[stmt.out] = np.inf

		elif(stmt.linenum < cur_line.linenum):
			# print(stmt.linenum)
			if(stmt.in1 <> None and stmt.in1_type == EntryType.VARIABLE and stmt.in1 not in EvictionCandidates and stmt.in1 in VariableData and  VariableData[stmt.in1][1] <> 0 and (stmt.in1 != cur_line.in1 and stmt.in1 !=cur_line.in2 and stmt.in1 != cur_line.out)):
				return stmt.in1
			elif(stmt.in2 <> None and stmt.in2_type == EntryType.VARIABLE and stmt.in2 not in EvictionCandidates and stmt.in2 in VariableData and VariableData[stmt.in2][1] <> 0 and (stmt.in2 != cur_line.in1 and stmt.in2 !=cur_line.in2 and stmt.in2 != cur_line.out)):
				return stmt.in2
			elif(stmt.out <> None and stmt.out_type == EntryType.VARIABLE and stmt.out not in EvictionCandidates and stmt.out in VariableData and VariableData[stmt.out][1] <> 0 and (stmt.out != cur_line.in1 and stmt.out !=cur_line.in2 and stmt.out != cur_line.out)):
				return stmt.out


	# print("HERE")
	return max (EvictionCandidates, key=EvictionCandidates.get)

def FindEmptyReg():
	for reg in UsableRegisters:
		if (UsableRegisters[reg] == 0):
			return reg

def searchString(StringDict, string):
	for strs in StringDict:
		if StringDict[strs] == string:
			return strs

def GetReg(stmt, block):
	
	nue = NextUse[stmt.linenum]
	useless_var = None
	empty_reg = None
	# if(nue.in1 != "" and nue.in1nextuse == np.inf and nue.in1 != nue.out):
	# 	useless_var = nue.in1
	# 	empty_reg = VariableData[useless_var][1]
	# 	stmt.code_statement = stmt.code_statement +  "sw $%s, %s\n"%(VariableData[useless_var][1], useless_var)
	# 	UsableRegisters[empty_reg] = 0
	# elif(nue.in2 != "" and nue.in2nextuse == np.inf and nue.in2 != nue.out):
	# 	useless_var = nue.in2
	# 	empty_reg = VariableData[useless_var][1]
	# 	stmt.code_statement = stmt.code_statement +  "sw $%s, %s\n"%(VariableData[useless_var][1], useless_var)
	# 	UsableRegisters[empty_reg] = 0
	# print(UsableRegisters.values())
	if 0 in UsableRegisters.values():
		empty_reg = FindEmptyReg()
	else: 		# to handle for temporaries
		useless_var = constructEvictionCandidate(stmt,block)

		empty_reg = VariableData[useless_var][1]
		l = lookup_LocalSymbolTable(useless_var)

		if(l.dataType != 'Array'):
			if l.scope == Scope.LOCAL:
				stmt.code_statement = stmt.code_statement +  "sw $%s, -%d($fp)\n"%(VariableData[useless_var][1], VariableData[useless_var][0])
			else:
				stmt.code_statement = stmt.code_statement +  "sw $%s, %s\n"%(VariableData[useless_var][1], useless_var)

		UsableRegisters[empty_reg] = 0
		VariableData[useless_var][1] = 0
	
	# print("------------------------1234--%s"%empty_reg)
	# print(UsableRegisters.keys())
	if(not (empty_reg in UsableRegisters.keys())):
		print("Invalid register" + str(empty_reg))
		exit()
	return empty_reg


def UpdateVariableData(statement,block):
	if(statement.in1_type == EntryType.VARIABLE):

		if(statement.in1 not in VariableData or VariableData[statement.in1][1] == 0):
			register = GetReg(statement,block)
			VariableData[statement.in1][1] = register
			UsableRegisters[register] = statement.in1
			l = lookup_LocalSymbolTable(statement.in1)
			# if(statement.instr_typ==InstrType.INDEX_ASSIGN_R or (l.dataType=="Array" and (statement.instr_typ==InstrType.SCAN_INT or statement.instr_typ==InstrType.PRINT_INT))):

			if(l.scope == Scope.LOCAL):
				# if(l.isArray==True):
				# 	statement.code_statement = statement.code_statement + "lw $%s, -%d($fp)\n"%(VariableData[statement.in1][1], VariableData[statement.in1][0])
				# else:
				statement.code_statement = statement.code_statement + "lw $%s, -%d($fp)\n"%(VariableData[statement.in1][1], VariableData[statement.in1][0])
			else:
				# if(l.dataType=="Array"):
				# 	statement.code_statement = statement.code_statement + "lw $%s, %s\n"%(VariableData[statement.in1][1], statement.in1)
				# else:
				statement.code_statement = statement.code_statement + "lw $%s, %s\n"%(VariableData[statement.in1][1], statement.in1)



	if(statement.in2_type == EntryType.VARIABLE):
		if(statement.in2 not in VariableData or VariableData[statement.in2][1] == 0):
			register = GetReg(statement,block)
			VariableData[statement.in2][1] = register
			UsableRegisters[register] = statement.in2
			l = lookup_LocalSymbolTable(statement.in2)
			# statement.code_statement = statement.code_statement + "lw $%s,%s\n" % (register, UsableRegisters[register])
			if(l.scope == Scope.LOCAL):
				statement.code_statement = statement.code_statement + "lw $%s, -%d($fp)\n"%(VariableData[statement.in2][1], VariableData[statement.in2][0])
			else:
				statement.code_statement = statement.code_statement + "lw $%s, %s\n"%(VariableData[statement.in2][1], statement.in2)

	if(statement.out_type == EntryType.VARIABLE):
		if(statement.out not in VariableData or VariableData[statement.out][1] == 0):
			# print statement.out,"PPPPPPPPPPPOOOOOOOOOOOOOOOPPPPPPPPPPPPOOOOOOOOOOOOOOOO"
			# print(statement.out)
			register = GetReg(statement,block)
			VariableData[statement.out][1] = register
			print statement.out,register
			UsableRegisters[register] = statement.out
			l=lookup_LocalSymbolTable(statement.out)


			# if( statement.in1 != statement.out and statement.in2 != statement.out ):
			# 	pass
			# else:
			if(l.scope == Scope.LOCAL):
				if(l.isArray==True):
					statement.code_statement = statement.code_statement + "lw $%s, -%d($fp)\n"%(VariableData[statement.out][1], VariableData[statement.out][0])
				else:
					statement.code_statement = statement.code_statement + "lw $%s, -%d($fp)\n" % (register, VariableData[statement.out][0])
			else:
				if(l.isArray ==True):
					statement.code_statement = statement.code_statement + "lw $%s, %s\n"%(VariableData[statement.out][1], statement.out)
				else:
					statement.code_statement = statement.code_statement + "lw $%s,%s\n" % (register, UsableRegisters[register])

def main(SymbolTables, StringDict):
	# print StringDict
	# quit()

	code = []
	leaders = [1]
	numberoflinesinfile=0

	data_code = ".data\n"
	machine_code = ".text\n"
	data_code = data_code + 'space: .asciiz " "\n'
	for string in StringDict:
		print (StringDict[string].replace("'", "\"")).replace("\n","\\%c"%("n")),"@@@@"
		data_code += "%s: .asciiz %s\n"%(string, (StringDict[string].replace("'", "\"")).replace("\n","\\%c"%("n")))









#------------------------------------- Reading Code----------------------------------------
	i=0
	for  x in SymbolTables:
		if(x.symtab_type != 'LET'):
			i = 4
			name=x.scope_name
		if(x.scope_name != 'Main'):
			for var in x.variables:
				var.name = x.scope_name + '.' + var.name
				VariableData[var.name] = [i,0]
				i = i + var.size
				s=LocalSymTabEntry(size = var.size, dataType = var.datatype, scope = Scope.LOCAL, isArray=var.isArray)
				insert_LocalSymbolTable(var.name, s)
				# data_code = data_code + "%s : .word 0\n"%var.name
			MethodSize[name]=i-4
		else:
			for var in x.variables:
				var.name = x.scope_name + '.' + var.name
				VariableData[var.name] = [0,0]
				s=LocalSymTabEntry(size=var.size, dataType=var.datatype,scope=Scope.GLOBAL, isArray=var.isArray)
				insert_LocalSymbolTable(var.name, s)
				# if(not var.isArray):
				data_code = data_code + "%s : .word 0\n"%(var.name)
				# else:
				# 	data_code = data_code + "%s : .word 0%d\n"%(var.name, 4*int(var.size))
				i = i + var.size
			MethodSize[name]=i-4




#----------------------------------------Local Symbol Table Loaded----------------------------------
	print("----------LOCAL SYMBOL TABLE START----------")
	for s in LocalSymbolTable:
		print (s, LocalSymbolTable[s].size, LocalSymbolTable[s].dataType, LocalSymbolTable[s].scope)
	print("----------LOCAL SYMBOL TABLE END----------")

	print("---------- VariableData START--------")
	for k in VariableData.keys():
		print(k, VariableData[k][0], VariableData[k][1])
	print("---------- VariableData END--------")

	print("--------- MethodSize START------")
	for k in MethodSize.keys():
		print(k , MethodSize[k])
	print("--------- MethodSize END ------")


	os.system('rm -f temp.asm')
	assemblyfile=open('temp.asm','w')
	assemblyfile.write(data_code)
	assemblyfile.write(machine_code)
	assemblyfile.write("main:\n")
	# assemblyfile.write("addiu $sp, $sp, -%d\n\n"%(MethodSize['Main']))

	with open(sys.argv[2], 'rb') as codefile:
		line_reader = csv.reader(codefile, delimiter = ',')
		
		for row in line_reader:
			curr_statement = statement()
			numberoflinesinfile = numberoflinesinfile + 1
			set_inputs(row, curr_statement)
			code.append(curr_statement)

			#------------------------------------------------
			if(curr_statement.instr_typ == InstrType.GOTO or curr_statement.instr_typ == InstrType.IFGOTO or curr_statement.instr_typ == InstrType.FUNC_RETURN or curr_statement.instr_typ == InstrType.FUNC_CALL or curr_statement.instr_typ==InstrType.RETURN):
				leaders.append(int(curr_statement.linenum)+1)
				# if(curr_statement.instr_typ == InstrType.IFGOTO or curr_statement.instr_typ == InstrType.GOTO):
				# 	leaders.append(int(curr_statement.jump_tagret))
			if(curr_statement.instr_typ == InstrType.LABEL or curr_statement.instr_typ == InstrType.FUNC_LABEL):
				leaders.append(int(curr_statement.linenum))

			#------------------------------------------------
	# for x in code:
	# 	x.print_stmt()
#---------------------------------------Code Read--------------------------------




#---------------------------------------------Basic block------------------------------
	leaders.append(numberoflinesinfile+1)
	leaders=set(leaders)
	leaders=list(leaders)
	leaders.sort()

	# print(leaders)

	for i in range(len(leaders)-1):
		# #print(leaders[i]-1,leaders[i+1]-1)
		basic_block = code[leaders[i]-1:leaders[i+1]-1]
		basic_block_list.append(basic_block)

	# for x in basic_block_list:
	# 	for st in x:
	# 		st.print_stmt()
	# 	print("----------------------")

# ----------------------------------------Basic block prepared----------------------------------------


	construct_NextUse()
	


	print_int_func = "print_int:\nli $v0,1\nsyscall\njr $ra\n"
	scan_int_func = "scan_int:\nli $v0,5\nsyscall\njr $ra\n"

	print_string_func = "print_string:\nli $v0,4\nsyscall\njr $ra\n"
	scan_string_func = "scan_string:\nli $v0,8\nsyscall\njr $ra\n"

	exit_func="exit_func:\nli $v0,10\nsyscall\n"
	space_func="space_func:\nla $a0, space\nli $v0, 4\nsyscall\njr $ra\n"

	file_open_func="file_open:\nli $v0, 13\nli $a2, 0\nsyscall\nmove $t8, $v0\njr $ra\n"
	file_read_func="file_read:\nli $v0, 14\nmove $a0, $t8\nli $a2, 100\nsyscall\njr $ra\n"
	file_close_func="file_close:\nli $v0, 16\nmove $a0, $t8\nsyscall\njr $ra\n"

	file_write_func="file_write:\nli $v0, 15\nmove $a0, $t8\nmove $t6, $ra\njal strlen\nmove $ra, $t6\nsyscall\njr $ra\n"

	strlen_func="strlen:\nmove $a3, $a1\nli $a2, 0\nj strlen.test\nstrlen.loop:\naddi $a3, $a3, 1\naddi $a2, $a2, 1\nstrlen.test:\nlb $t7, 0($a3)\nbnez $t7, strlen.loop\njr $ra\n"

# ---------------------------------------------------------------Translation -----------------------------
	prevst = None
	curMethod = None
	for x in basic_block_list:
		for st in x:
			# infunction=['main']
			UpdateVariableData(st,x)


			# print("variable data updated :  %s" % st.linenum)
			# print (VariableData)
			# print UsableRegisters

			if(st.instr_typ == InstrType.ASSIGN and st.operator == None):
				if(st.in1_type == EntryType.VARIABLE):
					st.code_statement = st.code_statement + "move $%s, $%s\n"%(VariableData[st.out][1], VariableData[st.in1][1])
				elif(st.in1_type == EntryType.INTEGER):
					st.code_statement = st.code_statement + "li $%s, %d\n"%(VariableData[st.out][1], st.in1)
				elif(st.in1_type == EntryType.STRING):
					print "#######",st.in1
					for k in StringDict:
						print StringDict[k]
				 	st.code_statement += "la $%s, %s\n"%(VariableData[st.out][1], searchString(StringDict,st.in1))
				 	# print VariableData[st.out][1],"@@@@@@@@@@@@"
			elif(st.instr_typ == InstrType.ASSIGN):
				if(st.operator == Operator.ADD):
					if(st.in1_type == EntryType.VARIABLE and st.in2_type == EntryType.VARIABLE):
						st.code_statement = st.code_statement + "add $%s, $%s, $%s\n"%(VariableData[st.out][1], VariableData[st.in1][1], VariableData[st.in2][1])
					elif(st.in1_type == EntryType.VARIABLE and st.in2_type == EntryType.INTEGER):
						st.code_statement = st.code_statement + "addi $%s, $%s, %d\n"%(VariableData[st.out][1], VariableData[st.in1][1], st.in2)
					elif(st.in1_type == EntryType.INTEGER and st.in2_type == EntryType.VARIABLE):
						st.code_statement = st.code_statement + "addi $%s, $%s, %d\n"%(VariableData[st.out][1], VariableData[st.in2][1], st.in1)
					elif(st.in1_type == EntryType.INTEGER and st.in2_type == EntryType.INTEGER):
						st.code_statement = st.code_statement + "li $%s, %d\n"%(VariableData[st.out][1], st.in1 + st.in2)

				elif(st.operator == Operator.SUB):
					if(st.in1_type == EntryType.VARIABLE and st.in2_type == EntryType.VARIABLE):
						st.code_statement = st.code_statement + "sub $%s, $%s, $%s\n"%(VariableData[st.out][1], VariableData[st.in1][1], VariableData[st.in2][1])
					elif(st.in1_type == EntryType.VARIABLE and st.in2_type == EntryType.INTEGER):
						st.code_statement = st.code_statement + "addi $%s, $%s, -%d\n"%(VariableData[st.out][1], VariableData[st.in1][1], st.in2)
					elif(st.in1_type == EntryType.INTEGER and st.in2_type == EntryType.VARIABLE):
						st.code_statement = st.code_statement + "sub $t7, $zero, $%s\n"%(VariableData[st.in2][1])
						st.code_statement = st.code_statement + "addi $%s, $t7, %d\n"%(VariableData[st.out][1], st.in1)
					elif(st.in1_type == EntryType.INTEGER and st.in2_type == EntryType.INTEGER):
						st.code_statement = st.code_statement + "li $%s, %d\n"%(VariableData[st.out][1], st.in1 - st.in2)

				elif(st.operator == Operator.MUL):
					if(st.in1_type == EntryType.VARIABLE and st.in2_type == EntryType.VARIABLE):
						st.code_statement = st.code_statement + "mult $%s, $%s\n"%(VariableData[st.in1][1], VariableData[st.in2][1])
						st.code_statement = st.code_statement + "mflo $%s\n"%(VariableData[st.out][1])
					elif(st.in1_type == EntryType.VARIABLE and st.in2_type == EntryType.INTEGER):
						st.code_statement = st.code_statement + "li $t7, %d\n"%(st.in2)
						st.code_statement = st.code_statement + "mult $%s, $t7\n"%(VariableData[st.in1][1])
						st.code_statement = st.code_statement + "mflo $%s\n"%(VariableData[st.out][1])
					elif(st.in1_type == EntryType.INTEGER and st.in2_type == EntryType.VARIABLE):
						st.code_statement = st.code_statement + "li $t7, %d\n"%(st.in1)
						st.code_statement = st.code_statement + "mult $%s, $t7\n"%(VariableData[st.in2][1])
						st.code_statement = st.code_statement + "mflo $%s\n"%(VariableData[st.out][1])
					elif(st.in1_type == EntryType.INTEGER and st.in2_type == EntryType.INTEGER):
						st.code_statement = st.code_statement + "li $%s, %d\n"%(VariableData[st.out][1], st.in1 * st.in2)

				elif(st.operator == Operator.DIV):
					if(st.in1_type == EntryType.VARIABLE and st.in2_type == EntryType.VARIABLE):
						st.code_statement = st.code_statement + "div $%s, $%s\n"%(VariableData[st.in1][1], VariableData[st.in2][1])
						st.code_statement = st.code_statement + "mflo $%s\n"%(VariableData[st.out][1])
					elif(st.in1_type == EntryType.VARIABLE and st.in2_type == EntryType.INTEGER):
						st.code_statement = st.code_statement + "li $t7, %d\n"%(st.in2)
						st.code_statement = st.code_statement + "div $%s, $t7\n"%(VariableData[st.in1][1])
						st.code_statement = st.code_statement + "mflo $%s\n"%(VariableData[st.out][1])
					elif(st.in1_type == EntryType.INTEGER and st.in2_type == EntryType.VARIABLE):
						st.code_statement = st.code_statement + "li $t7, %d\n"%(st.in1)
						st.code_statement = st.code_statement + "div $%s, $t7\n"%(VariableData[st.in2][1])
						st.code_statement = st.code_statement + "mflo $%s\n"%(VariableData[st.out][1])
					elif(st.in1_type == EntryType.INTEGER and st.in2_type == EntryType.INTEGER):
						st.code_statement = st.code_statement + "li $%s, %d\n"%(VariableData[st.out][1], st.in1 / st.in2)

				elif(st.operator == Operator.MOD):
					if(st.in1_type == EntryType.VARIABLE and st.in2_type == EntryType.VARIABLE):
						st.code_statement = st.code_statement + "div $%s, $%s\n"%(VariableData[st.in1][1], VariableData[st.in2][1])
						st.code_statement = st.code_statement + "mfhi $%s\n"%(VariableData[st.out][1])
					elif(st.in1_type == EntryType.VARIABLE and st.in2_type == EntryType.INTEGER):
						st.code_statement = st.code_statement + "li $t7, %d\n"%(st.in2)
						st.code_statement = st.code_statement + "div $%s, $t7\n"%(VariableData[st.in1][1])
						st.code_statement = st.code_statement + "mfhi $%s\n"%(VariableData[st.out][1])
					elif(st.in1_type == EntryType.INTEGER and st.in2_type == EntryType.VARIABLE):
						st.code_statement = st.code_statement + "li $t7, %d\n"%(st.in1)
						st.code_statement = st.code_statement + "div $%s, $t7\n"%(VariableData[st.in2][1])
						st.code_statement = st.code_statement + "mfhi $%s"%(VariableData[st.out][1])
					elif(st.in1_type == EntryType.INTEGER and st.in2_type == EntryType.INTEGER):
						st.code_statement = st.code_statement + "li $%s, %d\n"%(VariableData[st.out][1], st.in1 % st.in2)
				elif(st.operator == Operator.READ_STACK):
					# print("@@@@ The Abhishek at work")
					# print(prevst)
					if(prevst <> None and  prevst.instr_typ == InstrType.FUNC_CALL):
						st.code_statement += "lw $fp, ($sp)\naddiu $sp, $sp, 4\n"
						st.code_statement += "lw $ra, ($sp)\naddiu $sp, $sp, 4\n"
						st.code_statement += "move $%s, $v0\n"%(VariableData[st.out][1])
					else:
						st.code_statement += "lw $t7, %d($fp)\n"%(readingfromstack[0])
						st.code_statement += "sw $t7, -%d($fp)\n"%(readingfromstack[0]+4)
						st.code_statement += "move $%s, $t7\n"%(VariableData[st.out][1])
						readingfromstack[0] += 4
						VariableData[st.out][0] = readingfromstack[0]
					# st.code_statement = st.code_statement + "lw $%s, ($sp)\n"%(VariableData[st.out][1])



				## Use Set Registers
				elif(st.operator == Operator.LESS_THAN):
					if(st.in2_type == EntryType.VARIABLE and st.in1_type == EntryType.VARIABLE):
						st.code_statement = st.code_statement + "slt $%s, $%s, $%s\n"%(VariableData[st.out][1], VariableData[st.in1][1], VariableData[st.in2][1])
					elif(st.in2_type == EntryType.VARIABLE and st.in1_type == EntryType.INTEGER):
						st.code_statement = st.code_statement + "sgei $%s, $%s, %d\n"%(VariableData[st.out][1],VariableData[st.in2][1],st.in1)
					elif(st.in2_type == EntryType.INTEGER and st.in1_type == EntryType.VARIABLE):
						st.code_statement = st.code_statement + "slti $%s, $%s, %d\n"%(VariableData[st.out][1], VariableData[st.in1][1], st.in2)
					elif(st.in2_type == EntryType.INTEGER and st.in1_type == EntryType.INTEGER):
						st.code_statement = st.code_statement + "li $%s, %d\n"%(VariableData[st.out][1], 1 if st.in1 < st.in2 else 0)

				elif(st.operator == Operator.LESS_THAN_EQUALS):
					if(st.in2_type == EntryType.VARIABLE and st.in1_type == EntryType.VARIABLE):
						st.code_statement = st.code_statement + "sle $%s, $%s, $%s\n"%(VariableData[st.out][1], VariableData[st.in1][1], VariableData[st.in2][1])
					elif(st.in2_type == EntryType.VARIABLE and st.in1_type == EntryType.INTEGER):
						st.code_statement = st.code_statement + "li $t7,%d\n"%st.in1
						st.code_statement = st.code_statement + "sle $%s, $t7, %d\n"%(VariableData[st.out][1],VariableData[st.in2][1])
					elif(st.in2_type == EntryType.INTEGER and st.in1_type == EntryType.VARIABLE):
						st.code_statement = st.code_statement + "slei $%s, $%s, %d\n"%(VariableData[st.out][1],VariableData[st.in1][1],st.in2)
					elif(st.in2_type == EntryType.INTEGER and st.in1_type == EntryType.INTEGER):
						st.code_statement = st.code_statement + "li $%s, %d\n"%(VariableData[st.out][1], 1 if st.in1 <= st.in2 else 0)
					# st.code_statement += "addi, $%s, $%s, 1\n"%(VariableData[st.out][1])


				elif(st.operator == Operator.GREATER_THAN):
					if(st.in2_type == EntryType.VARIABLE and st.in1_type == EntryType.VARIABLE):
						st.code_statement = st.code_statement + "sgt $%s, $%s, $%s\n"%(VariableData[st.out][1], VariableData[st.in1][1], VariableData[st.in2][1])
					elif(st.in2_type == EntryType.VARIABLE and st.in1_type == EntryType.INTEGER):
						st.code_statement = st.code_statement + "slei $%s, $%s, %d\n"%(VariableData[st.out][1], VariableData[st.in2][1], st.in1)
					elif(st.in2_type == EntryType.INTEGER and st.in1_type == EntryType.VARIABLE):
						st.code_statement = st.code_statement + "li $t7,%d\n"%st.in2
						st.code_statement = st.code_statement + "sgt $%s, $%s, $t7\n"%(VariableData[st.out][1],VariableData[st.in1][1])
					elif(st.in2_type == EntryType.INTEGER and st.in1_type == EntryType.INTEGER):
						st.code_statement = st.code_statement + "li $%s, %d\n"%(VariableData[st.out][1], 1 if st.in1 > st.in2 else 0)
					
				elif(st.operator == Operator.GREATER_THAN_EQUALS):
					if(st.in2_type == EntryType.VARIABLE and st.in1_type == EntryType.VARIABLE):
						st.code_statement = st.code_statement + "sge $%s, $%s, $%s\n"%(VariableData[st.out][1], VariableData[st.in1][1], VariableData[st.in2][1])
					elif(st.in2_type == EntryType.VARIABLE and st.in1_type == EntryType.INTEGER):
						st.code_statement = st.code_statement + "slti $%s, $%s, %d\n"%(VariableData[st.out][1], VariableData[st.in2][1], st.in1)
					elif(st.in2_type == EntryType.INTEGER and st.in1_type == EntryType.VARIABLE):
						st.code_statement = st.code_statement + "sgei $%s, $%s, %d\n"%(VariableData[st.out][1],VariableData[st.in1][1],st.in2)
					elif(st.in2_type == EntryType.INTEGER and st.in1_type == EntryType.INTEGER):
						st.code_statement = st.code_statement + "li $%s, %d\n"%(VariableData[st.out][1], 1 if st.in1 >= st.in2 else 0)
					
				elif(st.operator == Operator.EQUALS):
					if(st.in2_type == EntryType.VARIABLE and st.in1_type == EntryType.VARIABLE):
						st.code_statement = st.code_statement + "seq $%s, $%s, $%s\n"%(VariableData[st.out][1], VariableData[st.in1][1], VariableData[st.in2][1])
					elif(st.in2_type == EntryType.VARIABLE and st.in1_type == EntryType.INTEGER):
						st.code_statement += "li $t9, %d\n"%(st.in1)
						st.code_statement = st.code_statement + "seq $%s, $%s, $t9\n"%(VariableData[st.out][1], VariableData[st.in2][1])
					elif(st.in2_type == EntryType.INTEGER and st.in1_type == EntryType.VARIABLE):
						st.code_statement += "li $t9, %d\n"%(st.in2)
						st.code_statement = st.code_statement + "seq $%s, $%s, $t9\n"%(VariableData[st.out][1],VariableData[st.in1][1])
					elif(st.in2_type == EntryType.INTEGER and st.in1_type == EntryType.INTEGER):
						st.code_statement = st.code_statement + "li $%s, %d\n"%(VariableData[st.out][1], 1 if st.in1 == st.in2 else 0)
					

			elif(st.instr_typ == InstrType.POP_STACK):
				st.code_statement = st.code_statement + "addiu $sp, $sp, 4\n"

			elif(st.instr_typ == InstrType.FUNC_LABEL):
				st.code_statement = st.code_statement + "%s:\n"%(st.label)
				readingfromstack[0]=0
				curMethod = st.label

			elif(st.instr_typ == InstrType.LABEL):
				st.code_statement = st.code_statement + "%s:\n"%(st.label)


		
			elif(st.instr_typ == InstrType.FUNC_CALL):
				st.code_statement += "move $fp, $sp\n"
				st.code_statement += "addiu $sp, $sp, -%d\n"%(MethodSize[st.jump_tagret])
				st.code_statement = st.code_statement + "jal %s\n"%(st.jump_tagret) # handle return register
				

			
			elif(st.instr_typ == InstrType.FUNC_PARAM):
				if(st.in1_type == EntryType.INTEGER):
					st.code_statement = st.code_statement + "addiu $sp, $sp, -4\n"
					st.code_statement += "li $t7, %d\n"%(st.in1)
					st.code_statement += "sw $t7, ($sp)\n"
				elif(st.in1_type == EntryType.STRING):
					st.code_statement = st.code_statement + "addiu $sp, $sp, -4\n"
					st.code_statement += "la $t7, %s\n"%(searchString(StringDict, st.in1))
					st.code_statement += "sw $t7, ($sp)\n"
				else:
					st.code_statement = st.code_statement + "addiu $sp, $sp, -4\n"
					st.code_statement += "sw $%s, ($sp)\n"%(VariableData[st.in1][1])

			elif(st.instr_typ == InstrType.FUNC_START):
				st.code_statement += "addiu $sp, $sp, -4\n"
				st.code_statement += "sw $ra, ($sp)\n"

				st.code_statement += "addiu $sp, $sp, -4\n"
				st.code_statement += "sw $fp, ($sp)\n"



				# st.code_statement += "addiu $sp, $sp, -4\n" # Space for returning


			elif(st.instr_typ == InstrType.RETURN):
				if(st.out_type == EntryType.INTEGER):
					st.code_statement += "li $v0, %d\n"%(st.out)
				elif(st.out_type == EntryType.STRING):
					st.code_statement += "la $v0, %s\n"%(searchString(StringDict, st.out))
				else:
					st.code_statement += "move $v0, $%s\n"%(VariableData[st.out][1])


			elif(st.instr_typ == InstrType.FUNC_RETURN):
				# st.code_statement = st.code_statement + "lw $ra, ($sp)\nadd $sp, $sp, 4\n"
				st.code_statement += "addiu $sp, $sp, %d\n"%(MethodSize[curMethod])
				st.code_statement = st.code_statement + "jr $ra\n"

			elif(st.instr_typ == InstrType.INDEX_ASSIGN_L):
				if(st.in1_type==EntryType.VARIABLE):
					st.code_statement = st.code_statement+ "sll $t7, $%s, 2\n"%(VariableData[st.in1][1])
					st.code_statement = st.code_statement + "add $t8, $%s, $t7\n"%(VariableData[st.out][1])
					if(st.in2_type==EntryType.VARIABLE):
						st.code_statement = st.code_statement + "sw $%s, 0($t8)\n"%(VariableData[st.in2][1])
					else:
						st.code_statement = st.code_statement + "li $t9, %d\n"%(st.in2)
						st.code_statement = st.code_statement + "sw $t9, 0($t8)\n"
				else:
					st.code_statement = st.code_statement + "li $t7, %d\n"%(st.in1)
					st.code_statement = st.code_statement + "sll $t7, $t7, 2\n"
					st.code_statement = st.code_statement + "add $t8, $%s,$t7\n"%(VariableData[st.out][1])
					if(st.in2_type==EntryType.VARIABLE):
						st.code_statement = st.code_statement + "sw $%s, 0($t8)\n"%(VariableData[st.in2][1])
					else:
						st.code_statement = st.code_statement + "li $t9, %d\n"%(st.in2)
						st.code_statement = st.code_statement + "sw $t9, 0($t8)\n"


			elif(st.instr_typ == InstrType.INDEX_ASSIGN_R):
				if(st.in2_type==EntryType.VARIABLE):
					st.code_statement = st.code_statement+ "sll $t7, $%s, 2\n"%(VariableData[st.in2][1])
					st.code_statement = st.code_statement + "add $t8, $%s, $t7\n"%(VariableData[st.in1][1])
					st.code_statement = st.code_statement + "lw $%s, 0($t8)\n"%(VariableData[st.out][1])
				else:
					st.code_statement = st.code_statement + "li $t7, %d\n"%(st.in2)
					st.code_statement = st.code_statement + "sll $t8, $t7, 2\n"
					st.code_statement = st.code_statement + "add $t8, $%s,$t8\n"%(VariableData[st.in1][1])
					st.code_statement = st.code_statement + "lw $%s, 0($t8)\n"%(VariableData[st.out][1])



				if(st.out_type == EntryType.VARIABLE and st.in1_type == EntryType.VARIABLE and VariableData[st.out][1] == VariableData[st.in1][1] and st.out <> st.in1):
					VariableData[st.in1][1] = 0
				if(st.out_type == EntryType.VARIABLE and st.in2_type == EntryType.VARIABLE and VariableData[st.out][1] == VariableData[st.in2][1] and st.in2 <> st.out):
					VariableData[st.in2][1] = 0

			elif(st.instr_typ==InstrType.IFGOTO):

				branch_instr = ""
				if(st.operator == Operator.GREATER_THAN or st.operator == ''):
					branch_instr = "bgt"
				elif(st.operator == Operator.GREATER_THAN_EQUALS):
					branch_instr = "bge"
				elif(st.operator == Operator.LESS_THAN):
					branch_instr = "blt"
				elif(st.operator == Operator.LESS_THAN_EQUALS):
					branch_instr = "ble"
				elif(st.operator == Operator.EQUALS):
					branch_instr = "beq"
				elif(st.operator == Operator.NOT_EQUALS):
					branch_instr = "bne"

				if(st.in1_type == EntryType.VARIABLE and st.in2_type == EntryType.VARIABLE):
					branch_instr = branch_instr + " $%s,$%s,%s\n" % (VariableData[st.in1][1],VariableData[st.in2][1],st.jump_tagret)
				if(st.in1_type == EntryType.INTEGER and st.in2_type == EntryType.VARIABLE):
					temp_instr = "li $t7,%d\n"% st.in1
					branch_instr = temp_instr + branch_instr + " $t7,$%s,%s\n" % (VariableData[st.in2][1],st.jump_tagret)
				if(st.in1_type == EntryType.VARIABLE and st.in2_type == EntryType.INTEGER):
					temp_instr = "li $t7,%d\n" % st.in2
					branch_instr = temp_instr + branch_instr + " $%s,$t7,%s\n" % (VariableData[st.in1][1],st.jump_tagret)
				if(st.in1_type == EntryType.INTEGER and st.in2_type == EntryType.INTEGER):
					temp_instr = "li $t7,%d\n" % st.in1
					temp_instr = temp_instr + "li $t8,%d\n" % st.in2
					branch_instr = temp_instr + branch_instr + " $t7,$t8,%s\n" % (st.jump_tagret)


				st.code_statement = st.code_statement + branch_instr


			elif(st.instr_typ == InstrType.IFFALSE ):
				branch_instr = "ble"

				if(st.in1_type == EntryType.VARIABLE and st.in2_type == EntryType.INTEGER):
					temp_instr = "li $t7,%d\n" % st.in2
					branch_instr = temp_instr + branch_instr + " $%s,$t7,%s\n" % (VariableData[st.in1][1],st.jump_tagret)
				if(st.in1_type == EntryType.INTEGER and st.in2_type == EntryType.INTEGER):
					temp_instr = "li $t7,%d\n" % st.in1
					temp_instr = temp_instr + "li $t8,%d\n" % st.in2
					branch_instr = temp_instr + branch_instr + " $t7,$t8,%s\n" % (st.jump_tagret)

				st.code_statement = st.code_statement + branch_instr



			elif(st.instr_typ == InstrType.GOTO):
				st.code_statement = st.code_statement + "j %s\n" % (st.jump_tagret)


			elif(st.instr_typ == InstrType.READ_FILE):
				st.code_statement += "move $t9, $ra\n"
				st.code_statement += "li $a1, 0\n"


				if(st.in1_type == EntryType.VARIABLE):
					st.code_statement += "move $a0,$%s\n" % (VariableData[st.in1][1])
					st.code_statement += "jal file_open\n"
					st.code_statement += "move $a0, $t8\n"
					st.code_statement += "move $a1, $%s\n"%(VariableData[st.out][1])
					st.code_statement += "jal file_read\n"
					st.code_statement += "jal file_close\n"

				elif(st.in1_type == EntryType.STRING):
					st.code_statement += "la $a0,%s\n" % searchString(StringDict, st.in1)
					st.code_statement += "jal file_open\n"
					st.code_statement += "move $a0, $t8\n"
					st.code_statement += "move $a1, $%s\n"%(VariableData[st.out][1])
					st.code_statement += "jal file_read\n"
					st.code_statement += "jal file_close\n"


				st.code_statement += "move $ra, $t9\n"

			elif(st.instr_typ == InstrType.WRITE_FILE):
				st.code_statement += "move $t9, $ra\n"
				st.code_statement += "li $a1, 1\n"

				if(st.in1_type == EntryType.VARIABLE):
					st.code_statement += "move $a0,$%s\n" % (VariableData[st.in1][1])
					st.code_statement += "jal file_open\n"
					st.code_statement += "move $a0, $t8\n"
					

				elif(st.in1_type == EntryType.STRING):
					st.code_statement += "la $a0,%s\n" % searchString(StringDict, st.in1)
					st.code_statement += "jal file_open\n"
					st.code_statement += "move $a0, $t8\n"

				if(st.in2_type == EntryType.VARIABLE):
					st.code_statement += "move $a1, $%s\n"%(VariableData[st.in2][1])
					st.code_statement += "jal file_write\n"
					st.code_statement += "jal file_close\n"

				if(st.in2_type == EntryType.STRING):
					st.code_statement += "la $a1, %s\n"%searchString(StringDict,st.in2)
					st.code_statement += "jal file_write\n"
					st.code_statement += "jal file_close\n"

				st.code_statement += "move $ra, $t9\n"

			elif(st.instr_typ == InstrType.PRINT_INT):
				st.code_statement += "move $t9, $ra\n"
				if(st.in2 == None):
					if(st.in1_type ==EntryType.VARIABLE):
						st.code_statement = st.code_statement + "move $a0,$%s\n" % (VariableData[st.in1][1])
						st.code_statement = st.code_statement + "jal print_int\n"
					else:
						st.code_statement = st.code_statement + "li $a0,%d\n" % (st.in1)
						st.code_statement = st.code_statement + "jal print_int\n"
				else:
					if(st.in1_type == EntryType.INTEGER):
						print("Array address is an INTEGER \n")
						quit()
					else:
						if(st.in2_type == EntryType.VARIABLE):
							st.code_statement = st.code_statement + "sll $t7, $%s, 2\n"%(VariableData[st.in2][1])
							st.code_statement = st.code_statement + "add $t8, $%s, $t7\n"%(VariableData[st.in1][1])
							# st.code_statement = st.code_statement + "lw "
							st.code_statement = st.code_statement + "lw $a0,0($t8)\n"
							st.code_statement = st.code_statement + "jal print_int\n"
						else:
							st.code_statement = st.code_statement + "li $t7, %d\n"%(st.in2)
							st.code_statement = st.code_statement + "sll $t7, $t7, 2\n"
							st.code_statement = st.code_statement + "add $t8, $%s, $t7\n"%(VariableData[st.in1][1])
							# st.code_statement = st.code_statement + "lw "
							st.code_statement = st.code_statement + "lw $a0,0($t8)\n" 
							st.code_statement = st.code_statement + "jal print_int\n"
				st.code_statement += "move $ra, $t9\n"

			elif(st.instr_typ == InstrType.PRINT_STRING):
				st.code_statement += "move $t9, $ra\n"


				if(st.in1_type == EntryType.VARIABLE):
					st.code_statement = st.code_statement + "move $a0,$%s\n" % (VariableData[st.in1][1])
					st.code_statement = st.code_statement + "jal print_string\n"

				elif(st.in1_type == EntryType.STRING):
					st.code_statement = st.code_statement + "la $a0,%s\n" % searchString(StringDict, st.in1)
					st.code_statement = st.code_statement + "jal print_string\n"


				st.code_statement += "move $ra, $t9\n"


			elif(st.instr_typ == InstrType.SCAN_INT):
				st.code_statement += "move $t9, $ra\n"
				if(st.in2 == None):	
					if(st.in1_type ==EntryType.VARIABLE):
						st.code_statement = st.code_statement + "jal scan_int\n"
						st.code_statement = st.code_statement + "move $%s,$v0\n" % (VariableData[st.in1][1])
				else:
					if(st.in1_type == EntryType.INTEGER):
						print("Array address is an INTEGER \n")
						quit()
					else:
						if(st.in2_type == EntryType.VARIABLE):
							st.code_statement = st.code_statement + "jal scan_int\n"
							st.code_statement = st.code_statement + "sll $t7, $%s, 2\n"%(VariableData[st.in2][1])
							st.code_statement = st.code_statement + "add $t8, $%s, $t7\n"%(VariableData[st.in1][1])
							# st.code_statement = st.code_statement + "lw "
							st.code_statement = st.code_statement + "sw $v0,0($t8)\n"
						else:
							st.code_statement = st.code_statement + "jal scan_int\n"
							st.code_statement = st.code_statement + "li $t7, %d\n"%(st.in2)
							st.code_statement = st.code_statement + "sll $t7, $t7, 2\n"
							st.code_statement = st.code_statement + "add $t8, $%s, $t7\n"%(VariableData[st.in1][1])
							# st.code_statement = st.code_statement + "lw "
							st.code_statement = st.code_statement + "sw $v0,0($t8)\n"
				st.code_statement += "move $ra, $t9\n"
	
			elif(st.instr_typ == InstrType.EXIT):
				st.code_statement = st.code_statement + "jal exit_func\n"
			elif(st.instr_typ == InstrType.SPACE):
				st.code_statement = st.code_statement + "move $t9,$ra\njal space_func\nmove $ra,$t9\n"

			elif(st.instr_typ == InstrType.ALLOCATE):
				st.code_statement += "li $v0, 9\n"
				if(st.in1_type == EntryType.VARIABLE):
					st.code_statement += "move $a0, $%s\n"%(VariableData[st.in1][1])
				else:
					st.code_statement += "li $a0, %d\n"%(st.in1)
				st.code_statement += "sll $a0, $a0, 2\n"
				st.code_statement += 'syscall\n'
				st.code_statement += 'move $%s, $v0\n'%(VariableData[st.out][1])



			prevst = st
			
			

		
		block_code = ""
		for var in VariableData:
			if(VariableData[var][1] <> 0 and LocalSymbolTable[var].dataType <> "Array" ) :
				if(lookup_LocalSymbolTable(var).scope == Scope.LOCAL):
					block_code = block_code + "sw $%s, -%d($fp)\n"%(VariableData[var][1], VariableData[var][0])
				else:
					block_code = block_code + "sw $%s, %s\n"%(VariableData[var][1], var)
			if(VariableData[var][1] <> 0):
				UsableRegisters[VariableData[var][1]] = 0
				VariableData[var][1] = 0

		
		block_codes[id(x)] = block_code

		

	for basic_block in basic_block_list:

		for stmt in basic_block:
			if(stmt <> basic_block[len(basic_block) - 1]):
				assemblyfile.write(stmt.code_statement)
				assemblyfile.write('\n')
			else:
				if(stmt.instr_typ in [InstrType.GOTO, InstrType.IFGOTO, InstrType.FUNC_CALL, InstrType.FUNC_RETURN, InstrType.EXIT, InstrType.RETURN]):
					temp = stmt.code_statement.split('\n')
					if(stmt.instr_typ == InstrType.FUNC_CALL):
						ne = temp[:len(temp)-4] + [block_codes[id(basic_block)]] + temp[len(temp)-4:]
					else:
						ne = temp[:len(temp)-2] + [block_codes[id(basic_block)]] + temp[len(temp)-2:]
					res = ""
					for line in ne:
						res = res+line+'\n'
					stmt.code_statement = res[:len(res)-1]
					assemblyfile.write(stmt.code_statement)
					assemblyfile.write('\n')
					assemblyfile.write("#-----------------------------------block id: %d\n"%(id(basic_block)))
				else:
					assemblyfile.write(stmt.code_statement)
					assemblyfile.write('\n')
					assemblyfile.write(block_codes[id(basic_block)])
					assemblyfile.write('\n')
					assemblyfile.write("#-----------------------------------block id: %d\n"%(id(basic_block)))

	assemblyfile.write(exit_func)
	assemblyfile.write(print_int_func)
	assemblyfile.write(scan_int_func)
	assemblyfile.write(space_func)
	assemblyfile.write(print_string_func)
	assemblyfile.write(scan_string_func)
	assemblyfile.write(file_open_func)
	assemblyfile.write(file_read_func)
	assemblyfile.write(file_close_func)
	assemblyfile.write(file_write_func)
	assemblyfile.write(strlen_func)

	

	assemblyfile.close()

if __name__ == '__main__':
	main()