import sys

class Variable:
	"""docstring for Variable"""
	def __init__(self,name, datatype='Int', size=4):
		self.name = name
		self.datatype = datatype
		self.size = size


class Method:
	def __init__(self, name, datatype='Int'):
		self.name = name
		self.datatype = datatype

		
class Symtab:
	"""docstring for Symtab"""
	def __init__(self,parent,symtab_type, scope_name):
		self.variables = []
		self.parent = parent
		self.methods = []
		self.symtab_type = symtab_type    # symbol table type class or method or let type
		self.scope_name = scope_name 	# name of class or method or let id
		self.lets = []

	def enter(self,name,datatype='Int',size=4):
		if(self.search(name)):
			sys.exit("Variable %s already present in symbol table"%name)
		else:
			newvar = Variable(name,datatype,size)
			self.variables.append(newvar)

	def enter_method(self, name,datatype='Int'):
		if(self.search_method(name)):
			sys.exit("Method %s already present in symbol table"%name)
		else:
			newmethod = Method(name,datatype)
			self.methods.append(newmethod)

	def getVariable(self,name):
		current_sym_tab = self

		while current_sym_tab <> None:
			for variable_entry in current_sym_tab.variables:
				if(variable_entry.name == name):
					return variable_entry

			current_sym_tab = current_sym_tab.parent

		sys.exit('Error no entry in Symbol table for : '+name)
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

	def search(self,name):
		for variable_entry in self.variables:
			if(variable_entry.name == name):
				return True
		return False

	def search_method(self, name):
		for method_entry in self.methods:
			if(method_entry.name == name):
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
