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

class SymtabEntry(Enum):
	integer = 1
	address = 2

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
	def __init__(self, instr_typ, in1, in2, out, jump_tagret):
		self.instr_typ = instr_typ
		self.in1 = in1
		self.in2 = in2
		self.out = out
		self.jump_tagret = jump_tagret


def main():
	for i in Operator:
		print(i)

if __name__ == '__main__':
	main()


