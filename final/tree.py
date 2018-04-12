# f = open('symtab.txt', 'wb')
class Expression:
	"""docstring for Expression"""
	def __init__(self, code=[], place='', datatype='Int', isArray=False, relop=''):
		self.code = code
		self.place = place
		self.datatype = datatype
		self.isArray = isArray

class ArgumentList:
	"""docstring for ArgumentList"""
	def __init__(self, code):
		self.code = code

class FunctionCall:
	"""docstring for FunctionCall"""
	def __init__(self, code,datatype='Int'):
		self.code = code
		self.datatype = datatype

class Feature:
	"""docstring for Feature"""
	def __init__(self, code, datatype='Int'):
		self.code = code
		self.datatype = datatype

class FeatureHeader:
	"""docstring for FeatureHeader"""
	def __init__(self, code, datatype='Int'):
		self.code = code
		self.datatype = datatype


class FeatureBody:
	"""docstring for FeatureBody"""
	def __init__(self, code):
		self.code = code
		

class FeatureList:
	"""docstring for FeatureList"""
	def __init__(self, code):
		self.code = code

class Class:
	"""docstring for Class"""
	def __init__(self, code):
		self.code = code


class Classes:
	"""docstring for Class"""
	def __init__(self, code):
		self.code = code


class Program:
	"""docstring for Class"""
	def __init__(self, code):
		self.code = code

class ProgramImport:
	"""docstring for Class"""
	def __init__(self, code):
		self.code = code

class Start:
	"""docstring for Class"""
	def __init__(self, code):
		self.code = code


class If_Then_Else:
	"""docstring for Class"""
	def __init__(self, code,datatype='Int'):
		self.code = code
		self.datatype=datatype


class While:
	"""docstring for Class"""
	def __init__(self, code,datatype='Int'):
		self.code = code
		self.datatype=datatype

class For:
	"""docstring for Class"""
	def __init__(self, code,datatype='Int'):
		self.code = code
		self.datatype=datatype

class BlockExpression:
	"""docstring for BlockExpression"""
	def __init__(self, code,datatype='Int',place=''):
		self.code=code
		self.datatype=datatype
		self.place=place

class BlockList:
	"""docstring for BlockExpression"""
	def __init__(self, code,datatype='Int',place=''):
		self.code=code
		self.datatype=datatype
		self.place=place

class Formal:
	"""docstring for Formal"""
	def __init__(self, code, datatype='Int'):
		self.code = code
		self.datatype = datatype
		
class FormalParameterList(object):
	"""docstring for FormalParameterList"""
	def __init__(self, code,nargs=0):
		self.code = code
		self.nargs = nargs
		# self.symtab = symtab


class FormalParameter:
	"""docstring for FormalParameter"""
	def __init__(self, code, place, datatype='Int'):
		self.code = code
		self.place = place
		self.datatype = datatype



class Let(object):
		"""docstring for Let"""
		def __init__(self, code=[],datatype='Int',let_id = 0):
			self.code=code
			self.datatype=datatype
			self.let_id = let_id


class Type(object):
	"""docstring for Type"""
	def __init__(self,place):
		self.place = place
		
class ClassHeader(object):
	"""docstring for ClassHeader"""
	def __init__(self, code):
		self.code=code

class Id(object):
	"""docstring for Id"""
	def __init__(self,place = ''):
		self.place = place 
		