from enum import Enum

class InstrType(Enum):
	assign = 1
	goto = 2
	ifgoto = 3
	index_assign_l = 4
	index_assign_r = 5
	func_param = 6
	func_call = 7
	func_return = 8

class SymtabEntryType(Enum):
	integer = 1
	variable = 2
	string = 3

class Operator(Enum):
	less_than = 1
	greater_than = 2
	equals = 3
	not_equals = 4
	add = 5
	sub = 6
	mul = 7
	div = 8

class statement:
	def __init__(self, instr_typ, in1, in1_type, in2, in2_type, out, out_type, jump_tagret):
		self.instr_typ = instr_typ
		self.in1 = in1
		self.in1_type = in1_type
		self.in2 = in2
		self.in2_type = in2_type
		self.out = out
		self.out_type = out_type
		self.jump_tagret = jump_tagret


def main():
	code = []
	s1 = statement(InstrType.assign, 1, SymtabEntryType.integer, 2, SymtabEntryType.integer, 3, SymtabEntryType.variable, 4)
	
	code.append(s1)

	print (code)

if __name__ == '__main__':
	main()


