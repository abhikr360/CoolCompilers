class A
{
	a : Int;
	b : Int;

	def sum : Int(a : Int, b : Int, self : A)
	{
		return a+b;
	};
};

class B inherits A
{
	c : Int;

	def setsum : Int(a : Int, b : Int, self : B)
	{
		
		{
			self.c = self.sum(a,b);
			return 0;;
		}
	};
};

class Main
{
	k : A;
	def main : Int()
	{
		{
			k <- new A;
			out_int(k.sum(2,3));
		}
	};
};