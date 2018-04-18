import sys

def is_int(row):
	try:
		temp = int(row)
		return True
	except Exception as e:
		return False

class ClassObject:
	"""docstring for ClassObject"""
	def __init__(self,name):
		self.name = name
		self.variables = {}
		self.private = []
		self.parentprivatevariables=[]
		self.functions = {}
		self.privateFunctions=[]
		self.parent = None
		self.size = 0
	def printClass(self):
		print self.name
		print self.variables
		print self.private
		print self.functions
		print self.privateFunctions
		print self.parent
		print "size = " ,self.size

	def searchFunction(self, func_name):
		if(func_name in self.functions ):
			return self.functions[func_name]
		else:
			if(self.parent == None or self.parent == -1):
				return None
			else:
				return self.parent.searchFunction(func_name)


class Variable:
	"""docstring for Variable"""
	def __init__(self,name,changed_name ,datatype='Int', size=4,isArray=False,parent_scope_name = None):
		self.name = name
		self.changed_name = changed_name
		self.datatype = datatype
		self.isArray = isArray
		self.size = size
		self.parent_scope_name = parent_scope_name


class Method:
	def __init__(self, name, datatype='Int',parent_class = None):
		self.name = name
		self.datatype = datatype
		self.parent_class = parent_class

		
class Symtab:
	"""docstring for Symtab"""
	def __init__(self,parent,symtab_type, scope_name):
		self.variables = []
		self.parent = parent
		self.methods = []
		self.symtab_type = symtab_type    # symbol table type class or method or let type
		self.scope_name = scope_name 	# name of class or method or let id
		self.lets = []

	def enter(self, name, changed_name, datatype='Int',size=4,isArray=False):
		# name = self.scope_name + '.' + name 
		if(self.local_search(name)):
			sys.exit("Variable %s already present in symbol table"%name)
		else:
			newvar = Variable(name,changed_name,datatype,size,isArray,self.scope_name)
			self.variables.append(newvar)

	def enter_method(self, name,datatype='Int',parent_class=None):
		if(self.search_method(name)):
			sys.exit("Method %s already present in symbol table"%name)
		else:
			newmethod = Method(name,datatype,parent_class)
			self.methods.append(newmethod)

	def getVariable(self,name):
		# name = self.scope_name + '.' + name
		current_sym_tab = self



		while current_sym_tab <> None:
			for variable_entry in current_sym_tab.variables:
				if(variable_entry.name == name):
					return variable_entry
			# current_sym_tab.printsymtab()
			current_sym_tab = current_sym_tab.parent
		if(is_int(name)):
			return None
		sys.exit('Error no entry in Symbol table for : '+str(name))
		return None

	def getMethod(self,name):
		current_sym_tab = self

		while current_sym_tab <> None:
			for method_entry in current_sym_tab.methods:
				if(method_entry.name == name):
					return method_entry

			current_sym_tab = current_sym_tab.parent

		sys.exit('Error no entry in Symbol table for : '+name)
		return None	

	def local_search(self,name):
		for variable_entry in self.variables:
			if(variable_entry.name == name):
				return True
		return False
	def search(self,name):
		current_sym_tab = self

		while current_sym_tab <> None:
			for variable_entry in current_sym_tab.variables:
				if(variable_entry.name == name):
					return True
			current_sym_tab  =current_sym_tab.parent
		return False

	def search_method(self, name):
		for method_entry in self.methods:
			if(method_entry.name == str(name)):
				return True
		return False

	def getScope(self,name):
		current_sym_tab = self
		while current_sym_tab <> None:
			for variable_entry in current_sym_tab.variables:
				if(variable_entry.name == name):
					return current_sym_tab
			current_sym_tab = current_sym_tab.parent
		# sys.exit('Error no scope found for %s',name)
		return None

	def printsymtab(self):
		print "Symbol Table : ", self.scope_name
		if self.parent <> None:
			print "Parent : ", self.parent.scope_name
		for v in self.variables:
			print(v.name, v.datatype, v.size)
