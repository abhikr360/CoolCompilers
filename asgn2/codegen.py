from enum import Enum
import csv
import sys

class InstrType(Enum):
	assign = 1
	goto = 2
	ifgoto = 3
	index_assign_l = 4
	index_assign_r = 5
	func_param = 6
	func_call = 7
	func_return = 8
	label = 9
	scanf = 10
	printf = 11

class SymtabEntryType(Enum):
	integer = 1
	variable = 2
	string = 3

class Operator(Enum):
	less_than = 1
	greater_than = 2
	less_than = 3
	greater_than = 4
	equals = 5
	not_equals = 6
	add = 7
	sub = 8
	mul = 9
	div = 10

class statement:
	def __init__(self, linenum = None, instr_typ = None, in1 = None, in1_type = None, in2 = None, in2_type = None, out = None, out_type = None, jump_tagret = None, label = None):
		self.linenum = linenum
		self.instr_typ = instr_typ
		self.in1 = in1
		self.in1_type = in1_type
		self.in2 = in2
		self.in2_type = in2_type
		self.out = out
		self.out_type = out_type
		self.jump_tagret = jump_tagret
		self.label = label


def main():
	code = []
	leaders = []
	with open(str(sys.argv[1]), 'rb') as codefile:
		line_reader = csv.reader(codefile, delimiter = ',')
		for row in line_reader:
			print(row)

	#code = []
	s1 = statement(0,InstrType.assign, 1, SymtabEntryType.integer, 2, SymtabEntryType.integer, 3, SymtabEntryType.variable, 4)
	s2 = statement(0,InstrType.assign, 1, SymtabEntryType.integer, 2, SymtabEntryType.integer, 3, SymtabEntryType.variable, 4)
	
	code.append(s1)
	code.append(s2)

	print (code)

if __name__ == '__main__':
	main()


