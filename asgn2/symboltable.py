from enum import Enum
import codegen

SymbolTable={}
RegisterDescriptor={'HI': 0, 'LO' : 0, 'r0' : 0, 'at' : 0, 'v0' : 0, 'v1' : 0, 'a0' : 0, 'a1' : 0, 'a2' : 0, 'a3' : 0, 't0' : 0, 't1' : 0, 't2' : 0, 't3' : 0, 't4' : 0, 't5' : 0, 't6' : 0, 't7' : 0, 's0' : 0, 's1' : 0, 's2' : 0, 's3' : 0, 's4' : 0, 's5' : 0, 's6' : 0, 's7' : 0, 't8' : 0, 't9' : 0, 'k0' : 0, 'k1' : 0, 's8' : 0, 'ra' : 0}
addressDescriptor={}

class SymtabEntryType(Enum):
	INTEGER = 1
	VARIABLE = 2
	STRING = 3

class Scope(Enum):
	GLOBAL = 1
	LOCAL = 2


def lookup_SymbolTable(s):
	if(s in SymbolTable.keys()):
		return SymbolTable[s]
	else:
		return None

def insert_SymbolTable(s, symbolTableEntry):
	if(s==""):
		print("symbolName Cannot be empty.....Aborting !!")
		exit()
	else:
		SymbolTable[s]=symbolTableEntry


class SymTabEntry:
	def __init__(self, isLive=False, nextUse=0, dataType=SymtabEntryType.INTEGER, scope=Scope.GLOBAL):
		self.isLive=isLive
		self.nextUse=nextUse
		self.dataType=dataType
		self.scope=scope

NextUse={}

class NextUseEntry:
	"""docstring for NextUseEntry"""
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
	s=1
	
def main():

	# s1 = SymTabEntry()
	# insert_SymbolTable('a1', s1)
	# print(SymbolTable)
	# s2 = SymTabEntry()
	# insert_SymbolTable('a_b', s2)

	# print(lookup_SymbolTable('s'))
	# print(lookup_SymbolTable('a1').isLive)
	print(codegen.basic_block_list)


if __name__ == '__main__':
	main()