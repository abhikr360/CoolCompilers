from enum import Enum
import csv
import sys

def is_int(row):
	try:
		temp = int(row)
		return True
	except Exception as e:
		return False

class InstrType(Enum):
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
	INTEGER = 1
	VARIABLE = 2
	STRING = 3

class Operator(Enum):
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

	def print_stmt(self):
		print(self.linenum,self.instr_typ,self.operator,self.in1,self.in1_type,self.in2,self.in2_type,self.out,self.jump_tagret,self.label)

def set_inputs(row, curr_statement):
	curr_statement.linenum = row[0]
	#------------------------------------------------
	assign_list = ["LESS_THAN", "GREATER_THAN", "LESS_THAN_EQUALS", "GREATER_THAN_EQUALS", "EQUALS", "NOT_EQUALS", "ADD", "SUB", "MUL", "DIV", "MOD"]
	if(row[1] == "ASSIGN" or row[1] in assign_list):
		curr_statement.instr_typ = InstrType.ASSIGN
		if(row[1] in assign_list):
			exec("curr_statement.operator = Operator.%s" %(row[1]))
	else:
		exec("curr_statement.instr_typ = InstrType.%s" %(row[1]))

	#--------------- For row 2 ----------------------

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
	#print(curr_statement.linenum, curr_statement.instr_typ, curr_statement.operator,curr_statement.out,curr_statement.in1,curr_statement.in2)


def main():
	code = []
	leaders = [1]
	with open(str(sys.argv[1]), 'rb') as codefile:
		line_reader = csv.reader(codefile, delimiter = ',')
		for row in line_reader:
			curr_statement = statement()
			#print(row[1])
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

	#code = []
	# s1 = statement(0,InstrType.assign, 1, SymtabEntryType.integer, 2, SymtabEntryType.integer, 3, SymtabEntryType.variable, 4)
	# s2 = statement(0,InstrType.assign, 1, SymtabEntryType.integer, 2, SymtabEntryType.integer, 3, SymtabEntryType.variable, 4)

	for x in code:
		x.print_stmt()
	leaders=set(leaders)
	leaders=list(leaders)
	leaders.sort()

	basic_block_list = []

	for i in range(len(leaders)-1):
		print(leaders[i]-1,leaders[i+1]-1)
		basic_block = code[leaders[i]-1:leaders[i+1]-1]
		basic_block_list.append(basic_block)


	
	for x in basic_block_list:
		print(x[0].instr_typ)

if __name__ == '__main__':
	main()


