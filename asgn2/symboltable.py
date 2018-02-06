from enum import Enum
symbolTable={}
class SymtabEntryType(Enum):
	INTEGER = 1
	VARIABLE = 2
	STRING = 3


class symTabEntry:
	count=0;
	@staticmethod
	def lookup(s):
		for e in symbolTable.values():
			if(e.symbolName==s):
				return e.symTabIdx

	def __init__(self, symbolName="", isLive=False, nextUse=0, dataType=SymtabEntryType.INTEGER, scope=None):
		self.symTabIdx=symTabEntry.count;
		symTabEntry.count = symTabEntry.count + 1
		self.symbolName = symbolName
		self.isLive=isLive
		self.nextUse=nextUse
		self.dataType=dataType
		self.scope=scope


	def insert(self):
		if(self.symbolName==""):
			print("symbolName Cannot be empty.....Aborting !!")
			exit()
		else:
			symbolTable[self.symTabIdx]=self

	
def main():
	

	registerDescriptor={'HI': 0, 'LO' : 0, 'r0' : 0, 'at' : 0, 'v0' : 0, 'v1' : 0, 'a0' : 0, 'a1' : 0, 'a2' : 0, 'a3' : 0, 't0' : 0, 't1' : 0, 't2' : 0, 't3' : 0, 't4' : 0, 't5' : 0, 't6' : 0, 't7' : 0, 's0' : 0, 's1' : 0, 's2' : 0, 's3' : 0, 's4' : 0, 's5' : 0, 's6' : 0, 's7' : 0, 't8' : 0, 't9' : 0, 'k0' : 0, 'k1' : 0, 's8' : 0, 'ra' : 0}
	addressDescriptor={} # Key for this dictionary will be the index in symbol table

	s1 = symTabEntry('abf', True, 0)
	s1.insert()
	print(symbolTable)
	s2 = symTabEntry('kl')

	s2.insert()
	s3 = symTabEntry('hj')
			
	s3.insert()

	print(symTabEntry.lookup('kl'))

if __name__ == '__main__':
	main()