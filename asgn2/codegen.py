from enum import Enum
import csv
import sys
import numpy as np


# Global DS #
basic_block_list = []
LocalSymbolTable={}
RegisterDescriptor={'HI': 0, 'LO' : 0, 'r0' : 0, 'at' : 0, 'v0' : 0, 'v1' : 0, 'a0' : 0, 'a1' : 0, 'a2' : 0, 'a3' : 0, 't0' : 0, 't1' : 0, 't2' : 0, 't3' : 0, 't4' : 0, 't5' : 0, 't6' : 0, 't7' : 0, 's0' : 0, 's1' : 0, 's2' : 0, 's3' : 0, 's4' : 0, 's5' : 0, 's6' : 0, 's7' : 0, 't8' : 0, 't9' : 0, 'k0' : 0, 'k1' : 0, 's8' : 0, 'ra' : 0}
addressDescriptor={}
NextUse={}

UsableRegistersTemp = {'t0' : 0, 't1' : 0, 't2' : 0, 't3' : 0, 't4' : 0, 't5' : 0, 't6' : 0}
UsableRegistersGlobal = {'s0' : 0, 's1' : 0, 's2' : 0, 's3' : 0, 's4' : 0, 's5' : 0, 's6' : 0}

UsableRegisters = {'t0' : 0, 't1' : 0, 't2' : 0, 't3' : 0, 't4' : 0, 't5' : 0, 't6' : 0, 's0' : 0, 's1' : 0, 's2' : 0, 's3' : 0, 's4' : 0, 's5' : 0, 's6' : 0}

TempRegisters = {'t7' : 0, 't8' : 0, 't9' : 0}

VariableData = {}

memory_used = [0]

def is_int(row):
	try:
		temp = int(row)
		return True
	except Exception as e:
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

	def #print_stmt(self):
		'''Print an instruction'''
		#print(self.linenum,self.instr_typ,self.operator,self.in1,self.in1_type,self.in2,self.in2_type,self.out,self.jump_tagret,self.label)

def set_inputs(row, curr_statement):
	'''Reads input stores it in a list of classes'''
	curr_statement.linenum = row[0]
	#------------------------------------------------
	assign_list = ["LESS_THAN", "GREATER_THAN", "LESS_THAN_EQUALS", "GREATER_THAN_EQUALS", "EQUALS", "NOT_EQUALS", "ADD", "SUB", "MUL", "DIV", "MOD"]
	if(row[1] == "ASSIGN" or row[1] in assign_list):
		curr_statement.instr_typ = InstrType.ASSIGN
		if(row[1] in assign_list):
			exec("curr_statement.operator = Operator.%s" %(row[1]))
	else:
		exec("curr_statement.instr_typ = InstrType.%s" %(row[1]))

	#         --------------- For row 2 ----------------------

	if(curr_statement.instr_typ == InstrType.ASSIGN):
		if(curr_statement.operator <> None):					#for statements of type a = b + 2
			curr_statement.out = row[2]
			curr_statement.out_type = EntryType.VARIABLE

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
			curr_statement.out = row[2]
			curr_statement.out_type = EntryType.VARIABLE
			try:
				temp = int(row[3])
				curr_statement.in1 = temp
				curr_statement.in1_type = EntryType.INTEGER
			except Exception as e:
				temp = row[3]
				curr_statement.in1 = temp
				curr_statement.in1_type = EntryType.VARIABLE

	elif(curr_statement.instr_typ == InstrType.IFGOTO):
		exec("curr_statement.operator = Operator.%s" %(row[2]))
		curr_statement.jump_tagret = int(row[5])
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
			curr_statement.in1 = int(row[4])
			curr_statement.in1_type = EntryType.INTEGER
		else:
			curr_statement.in1 = row[4]
			curr_statement.in1_type = EntryType.VARIABLE

	elif(curr_statement.instr_typ == InstrType.INDEX_ASSIGN_R):			# OUT = IN1[IN2]
		curr_statement.out = row[2]
		curr_statement.out_type = EntryType.VARIABLE
		
		curr_statement.in1 = row[3]
		curr_statement.in1_type = EntryType.VARIABLE

		if(is_int(row[4])):
			curr_statement.in1 = int(row[4])
			curr_statement.in1_type = EntryType.INTEGER
		else:
			curr_statement.in1 = row[4]
			curr_statement.in1_type = EntryType.VARIABLE





	#-------------------row 2 end -------------------
	##print(curr_statement.linenum, curr_statement.instr_typ, curr_statement.operator,curr_statement.out,curr_statement.in1,curr_statement.in2)

class Scope(Enum):
	''' Scope of a variable'''
	GLOBAL = 1
	LOCAL = 2

def lookup_LocalSymbolTable(s):
	''' Search in symbol table'''
	if(s in LocalSymbolTable.keys() and s !=''):
		return LocalSymbolTable[s]
	else:
		return None

def insert_LocalSymbolTable(s, symbolTableEntry):
	'''Insert into symbol table'''
	if(s==""):
		#print("symbolName Cannot be empty.....Aborting !!")
		exit()
	else:
		LocalSymbolTable[s]=symbolTableEntry

class LocalSymTabEntry:
	'''One entry of symbol table'''
	def __init__(self, size=10, dataType="Int", scope=Scope.GLOBAL, isLive=False, nextUse=np.inf):
		self.isLive=isLive
		self.nextUse=nextUse
		self.dataType=dataType
		self.scope=scope
		self.size=size

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
	# #print(len(basic_block_list))
	for basic_block in basic_block_list:
		#Flush Symbol table's nextuse islive information
		for x in LocalSymbolTable:
			LocalSymbolTable[x].isLive = False
			LocalSymbolTable[x].nextUse = np.inf


		for stmt in reversed(basic_block):
			in1=""
			in2=""
			# stmt.#print_stmt()
			if(stmt.in1_type == EntryType.VARIABLE):
				in1=stmt.in1
			if(stmt.in2_type == EntryType.VARIABLE):
				in2=stmt.in2
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
					outnextuse=steo.nextUse
					outislive=steo.isLive
					steo.nextUse=np.inf
					steo.isLive=False
					LocalSymbolTable[out]=steo
				else:
					print("No entry for this variable in LocalSymbolTable")
					# s=LocalSymTabEntry()
					# insert_LocalSymbolTable(out,s)
			if(in1):
				if(ste1):
					in1nextuse=ste1.nextUse
					in1islive=ste1.isLive
					ste1.nextUse=stmt.linenum
					ste1.isLive=True
					LocalSymbolTable[in1]=ste1
				else:
					# s=LocalSymTabEntry(True, stmt.linenum)
					# insert_LocalSymbolTable(in1,s)
					print("No entry for this variable in LocalSymbolTable")
			if(in2):
				if(ste2):
					in2nextuse=ste2.nextUse
					in2islive=ste2.isLive
					ste2.nextUse=stmt.linenum
					ste2.isLive=True
					LocalSymbolTable[in2]=ste2
				else:
					# s=LocalSymTabEntry(True, stmt.linenum)
					# insert_LocalSymbolTable(in2,s)
					print("No entry for this variable in LocalSymbolTable")
			

			nue = NextUseEntry(in1, in2, out, in1nextuse, in2nextuse, outnextuse, in1islive, in2islive, outislive)
			NextUse[stmt.linenum]=nue

def constructEvictionCandidate(cur_line, basic_block):
	EvictionCandidates={}
	for stmt in reversed(basic_block):
		if(stmt == cur_line):
			return EvictionCandidates
		in1=""
		in2=""
		# stmt.#print_stmt()
		if(stmt.in1_type == EntryType.VARIABLE):
			in1=stmt.in1
			EvictionCandidates[stmt.in1] = stmt.linenum
		if(stmt.in2_type == EntryType.VARIABLE):
			in2=stmt.in2
			EvictionCandidates[stmt.in2] = stmt.linenum

def FindEmptyReg():
	for reg in UsableRegisters:
		if (UsableRegisters[reg] == 0):
			return reg

def GetReg():
	if 0 in UsableRegisters.values():
		return FindEmptyReg()

def UpdateVariableData(statement):
	if(statement.out_type == EntryType.VARIABLE):
		if(statement.out not in VariableData):
			register = GetReg()
			VariableData[statement.out] = [memory_used[0],register]
			memory_used[0] = memory_used[0] + 4
			UsableRegisters[register] = statement.out

def main():

	code = []
	leaders = [1]
	numberoflinesinfile=0

	machine_code = ""
	machine_code = machine_code + "lw $s7, $sp\n"

	with open(str(sys.argv[1]), 'rb') as symbolfile:
		line_reader = csv.reader(codefile, delimiter = ',')
		for row in line_reader:
			varname = row[0]
			size=row[1]
			datatype=row[2]
			if(row[3]=="GLOBAL"):
				scope=Scope.GLOBAL
			else:
				scope=Scope.LOCAL

			s=LocalSymTabEntry(size, datatype, scope)
			insert_LocalSymbolTable(varname, s)




	with open(str(sys.argv[1]), 'rb') as codefile:
		line_reader = csv.reader(codefile, delimiter = ',')
		
		for row in line_reader:
			curr_statement = statement()
			numberoflinesinfile = numberoflinesinfile + 1
			set_inputs(row, curr_statement)
			code.append(curr_statement)

			#------------------------------------------------
			if(curr_statement.instr_typ == InstrType.GOTO or curr_statement.instr_typ == InstrType.IFGOTO or curr_statement.instr_typ == InstrType.FUNC_RETURN or curr_statement.instr_typ == InstrType.FUNC_CALL):
				leaders.append(int(curr_statement.linenum)+1)
				if(curr_statement.instr_typ == InstrType.IFGOTO or curr_statement.instr_typ == InstrType.GOTO):
					leaders.append(int(curr_statement.jump_tagret))
			if(curr_statement.instr_typ == InstrType.LABEL):
				leaders.append(int(curr_statement.linenum))

			#------------------------------------------------
	# for x in code:
	# 	x.#print_stmt()
	leaders.append(numberoflinesinfile+1)
	leaders=set(leaders)
	leaders=list(leaders)
	leaders.sort()

	# #print(leaders)

	for i in range(len(leaders)-1):
		# #print(leaders[i]-1,leaders[i+1]-1)
		basic_block = code[leaders[i]-1:leaders[i+1]-1]
		basic_block_list.append(basic_block)

	# Basic block prepared----------------------------------------


	
	for x in basic_block_list:
		for st in x:
			UpdateVariableData(st)
			if(st.instr_typ == InstrType.ASSIGN and st.operator == None):
				if(st.in1_type == EntryType.VARIABLE):
					machine_code = machine_code + "move $%s, $%s\n"%(VariableData[st.out][1], VariableData[st.in1][1])
				elif(st.in1_type == EntryType.INTEGER):
					machine_code = machine_code + "li $%s, %d\n"%(VariableData[st.out][1], st.in1)

			elif(st.instr_typ == InstrType.ASSIGN):
				if(st.operator == Operator.ADD):
					if(st.in1_type == EntryType.VARIABLE and st.in2_type == EntryType.VARIABLE):
						machine_code = machine_code + "add $%s, $%s, $%s\n"%(VariableData[st.out][1], VariableData[st.in1][1], VariableData[st.in2][1])
					elif(st.in1_type == EntryType.VARIABLE and st.in2_type == EntryType.INTEGER):
						machine_code = machine_code + "addi $%s, $%s, %d\n"%(VariableData[st.out][1], VariableData[st.in1][1], st.in2)
					elif(st.in1_type == EntryType.INTEGER and st.in2_type == EntryType.VARIABLE):
						machine_code = machine_code + "addi $%s, $%s, %d\n"%(VariableData[st.out][1], VariableData[st.in2][1], st.in1)
					elif(st.in1_type == EntryType.INTEGER and st.in2_type == EntryType.INTEGER):
						machine_code = machine_code + "li $%s, %d\n"%(VariableData[st.out][1], st.in1 + st.in2)

				elif(st.operator == Operator.SUB):
					if(st.in1_type == EntryType.VARIABLE and st.in2_type == EntryType.VARIABLE):
						machine_code = machine_code + "sub $%s, $%s, $%s\n"%(VariableData[st.out][1], VariableData[st.in1][1], VariableData[st.in2][1])
					elif(st.in1_type == EntryType.VARIABLE and st.in2_type == EntryType.INTEGER):
						machine_code = machine_code + "addi $%s, $%s, -%d\n"%(VariableData[st.out][1], VariableData[st.in1][1], st.in2)
					elif(st.in1_type == EntryType.INTEGER and st.in2_type == EntryType.VARIABLE):
						machine_code = machine_code + "sub $t7, $zero, $%s\n"%(VariableData[st.in2][1])
						machine_code = machine_code + "addi $%s, $t7, %d\n"%(VariableData[st.out][1], st.in1)
					elif(st.in1_type == EntryType.INTEGER and st.in2_type == EntryType.INTEGER):
						machine_code = machine_code + "li $%s, %d\n"%(VariableData[st.out][1], st.in1 - st.in2)

				elif(st.operator == Operator.MUL):
					if(st.in1_type == EntryType.VARIABLE and st.in2_type == EntryType.VARIABLE):
						machine_code = machine_code + "mult $%s, $%s\n"%(VariableData[st.in1][1], VariableData[st.in2][1])
						machine_code = machine_code + "mflo $%s\n"%(VariableData[st.out][1])
					elif(st.in1_type == EntryType.VARIABLE and st.in2_type == EntryType.INTEGER):
						machine_code = machine_code + "li $t7, %d\n"%(st.in2)
						machine_code = machine_code + "mult $%s, $t7\n"%(VariableData[st.in1][1])
						machine_code = machine_code + "mflo $%s\n"%(VariableData[st.out][1])
					elif(st.in1_type == EntryType.INTEGER and st.in2_type == EntryType.VARIABLE):
						machine_code = machine_code + "li $t7, %d\n"%(st.in1)
						machine_code = machine_code + "mult $%s, $t7\n"%(VariableData[st.in2][1])
						machine_code = machine_code + "mflo $%s\n"%(VariableData[st.out][1])
					elif(st.in1_type == EntryType.INTEGER and st.in2_type == EntryType.INTEGER):
						machine_code = machine_code + "li $%s, %d\n"%(VariableData[st.out][1], st.in1 * st.in2)

				elif(st.operator == Operator.DIV):
					if(st.in1_type == EntryType.VARIABLE and st.in2_type == EntryType.VARIABLE):
						machine_code = machine_code + "div $%s, $%s\n"%(VariableData[st.in1][1], VariableData[st.in2][1])
						machine_code = machine_code + "mflo $%s\n"%(VariableData[st.out][1])
					elif(st.in1_type == EntryType.VARIABLE and st.in2_type == EntryType.INTEGER):
						machine_code = machine_code + "li $t7, %d\n"%(st.in2)
						machine_code = machine_code + "div $%s, $t7\n"%(VariableData[st.in1][1])
						machine_code = machine_code + "mflo $%s\n"%(VariableData[st.out][1])
					elif(st.in1_type == EntryType.INTEGER and st.in2_type == EntryType.VARIABLE):
						machine_code = machine_code + "li $t7, %d\n"%(st.in1)
						machine_code = machine_code + "div $%s, $t7\n"%(VariableData[st.in2][1])
						machine_code = machine_code + "mflo $%s\n"%(VariableData[st.out][1])
					elif(st.in1_type == EntryType.INTEGER and st.in2_type == EntryType.INTEGER):
						machine_code = machine_code + "li $%s, %d\n"%(VariableData[st.out][1], st.in1 / st.in2)

				elif(st.operator == Operator.MOD):
					if(st.in1_type == EntryType.VARIABLE and st.in2_type == EntryType.VARIABLE):
						machine_code = machine_code + "div $%s, $%s\n"%(VariableData[st.in1][1], VariableData[st.in2][1])
						machine_code = machine_code + "mfhi $%s\n"%(VariableData[st.out][1])
					elif(st.in1_type == EntryType.VARIABLE and st.in2_type == EntryType.INTEGER):
						machine_code = machine_code + "li $t7, %d\n"%(st.in2)
						machine_code = machine_code + "div $%s, $t7\n"%(VariableData[st.in1][1])
						machine_code = machine_code + "mfhi $%s\n"%(VariableData[st.out][1])
					elif(st.in1_type == EntryType.INTEGER and st.in2_type == EntryType.VARIABLE):
						machine_code = machine_code + "li $t7, %d\n"%(st.in1)
						machine_code = machine_code + "div $%s, $t7\n"%(VariableData[st.in2][1])
						machine_code = machine_code + "mfhi $%s"%(VariableData[st.out][1])
					elif(st.in1_type == EntryType.INTEGER and st.in2_type == EntryType.INTEGER):
						machine_code = machine_code + "li $%s, %d\n"%(VariableData[st.out][1], st.in1 % st.in2)




			#print(constructEvictionCandidate(st,x))
		#print("-------------------------------------------------------------------")
		#print(VariableData)
		#print(UsableRegisters)

		for var in VariableData:
			if(VariableData[var][1] <> 0):
				machine_code = machine_code + "sw %d($s7), $%s\n"%(VariableData[var][0], VariableData[var][1])
				UsableRegisters[VariableData[var][1]] = 0
				VariableData[var][1] = 0

		#print(VariableData)
		#print(UsableRegisters)
		#print("-------------------------------------------------------------------")

	for basic_block in basic_block_list:
		#print("-------")
		for stmt in basic_block:
			#print(stmt.linenum)

	construct_NextUse()
	#constructEvictionCandidate()
	# #print(NextUse.keys())
	#NextUse.sort()
	#print("HERE")
	##print(NextUse)
	#temp = sorted(NextUse.iteritems(), key = lambda (k,v): (v,k))
	#NextUse = temp
	
	for x in NextUse:
		#print x,NextUse[x].in1, NextUse[x].in2, NextUse[x].out, NextUse[x].in1nextuse, NextUse[x].in2nextuse, NextUse[x].outnextuse, NextUse[x].in1islive, NextUse[x].in2islive, NextUse[x].outislive

	
	temp = sorted(NextUse.iteritems(), key = lambda (k,v): (v,k))


if __name__ == '__main__':
	main()