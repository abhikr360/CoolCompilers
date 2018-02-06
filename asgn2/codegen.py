from enum import Enum
import csv
import sys


# Global DS #
basic_block_list = []
SymbolTable={}
RegisterDescriptor={'HI': 0, 'LO' : 0, 'r0' : 0, 'at' : 0, 'v0' : 0, 'v1' : 0, 'a0' : 0, 'a1' : 0, 'a2' : 0, 'a3' : 0, 't0' : 0, 't1' : 0, 't2' : 0, 't3' : 0, 't4' : 0, 't5' : 0, 't6' : 0, 't7' : 0, 's0' : 0, 's1' : 0, 's2' : 0, 's3' : 0, 's4' : 0, 's5' : 0, 's6' : 0, 's7' : 0, 't8' : 0, 't9' : 0, 'k0' : 0, 'k1' : 0, 's8' : 0, 'ra' : 0}
addressDescriptor={}
NextUse={}

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
		self.jump_tagret = None
		self.label = None

	def print_stmt(self):
		'''Print an instruction'''
		print(self.linenum,self.instr_typ,self.operator,self.in1,self.in1_type,self.in2,self.in2_type,self.out,self.jump_tagret,self.label)



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

	#-------------------row 2 end -------------------
	#print(curr_statement.linenum, curr_statement.instr_typ, curr_statement.operator,curr_statement.out,curr_statement.in1,curr_statement.in2)

class Scope(Enum):
	''' Scope of a variable'''
	GLOBAL = 1
	LOCAL = 2


def lookup_SymbolTable(s):
	''' Search in symbol table'''
	if(s in SymbolTable.keys() and s !=''):
		return SymbolTable[s]
	else:
		return None

def insert_SymbolTable(s, symbolTableEntry):
	'''Insert into symbol table'''
	if(s==""):
		print("symbolName Cannot be empty.....Aborting !!")
		exit()
	else:
		SymbolTable[s]=symbolTableEntry


class SymTabEntry:
	'''One entry of symbol table'''
	def __init__(self, isLive=False, nextUse=0, dataType=EntryType.INTEGER, scope=Scope.GLOBAL):
		self.isLive=isLive
		self.nextUse=nextUse
		self.dataType=dataType
		self.scope=scope



class NextUseEntry:
	"""for each line : for all three variables involved their next use and is lib=ve information"""
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
	# print(len(basic_block_list))
	i=-1
	for basic_block in basic_block_list:
		#Flush Symbol table's nextuse islive information
		i=i+1
		for x in SymbolTable:
			SymbolTable[x].isLive = False
			SymbolTable[x].nextUse = 0

		# if i==1:
		# 	print(SymbolTable['a'].isLive)
		# 	print(SymbolTable['a'].nextUse)
		# 	break
		for stmt in reversed(basic_block):
			in1=""
			in2=""
			# stmt.print_stmt()
			if(stmt.in1_type == EntryType.VARIABLE):
				in1=stmt.in1
			if(stmt.in2_type == EntryType.VARIABLE):
				in2=stmt.in2
			out = stmt.out
			in1nextuse=0
			in2nextuse=0
			outnextuse=0
			in1islive=False
			in2islive=False
			outislive=False



			ste1 = lookup_SymbolTable(in1)
			ste2 = lookup_SymbolTable(in2)
			steo = lookup_SymbolTable(out)
			print(in1, in2, out)
			if(out):
				if(steo):
					outnextuse=steo.nextUse
					outislive=steo.isLive
					steo.nextUse=0
					steo.isLive=False
					SymbolTable[out]=steo
				else:
					s=SymTabEntry()
					insert_SymbolTable(out,s)
			if(in1):
				if(ste1):
					in1nextuse=ste1.nextUse
					in1islive=ste1.isLive
					ste1.nextUse=stmt.linenum
					ste1.isLive=True
					SymbolTable[in1]=ste1
				else:
					s=SymTabEntry(True, stmt.linenum)
					insert_SymbolTable(in1,s)
			if(in2):
				if(ste2):
					in2nextuse=ste2.nextUse
					in2islive=ste2.isLive
					ste2.nextUse=stmt.linenum
					ste2.isLive=True
					SymbolTable[in2]=ste2
				else:
					s=SymTabEntry(True, stmt.linenum)
					insert_SymbolTable(in2,s)
			

			nue = NextUseEntry(in1, in2, out, in1nextuse, in2nextuse, outnextuse, in1islive, in2islive, outislive)
			NextUse[stmt.linenum]=nue



def main():
	code = []
	leaders = [1]
	numberoflinesinfile=0
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
	# 	x.print_stmt()
	leaders.append(numberoflinesinfile+1)
	leaders=set(leaders)
	leaders=list(leaders)
	leaders.sort()

	# print(leaders)

	for i in range(len(leaders)-1):
		# print(leaders[i]-1,leaders[i+1]-1)
		basic_block = code[leaders[i]-1:leaders[i+1]-1]
		basic_block_list.append(basic_block)
	# Basic block prepared----------------------------------------

	for basic_block in basic_block_list:
		print("-------")
		for stmt in basic_block:
			print(stmt.linenum)

	construct_NextUse()

	# print(NextUse.keys())
	for x in NextUse:
		print x,NextUse[x].in1, NextUse[x].in2, NextUse[x].out, NextUse[x].in1nextuse, NextUse[x].in2nextuse, NextUse[x].outnextuse, NextUse[x].in1islive, NextUse[x].in2islive, NextUse[x].outislive

if __name__ == '__main__':
	main()