class A
{
	a : Int;
	b : Int ;

	def sum : Int(a : Int, b : Int, self : A)
	{
		return a+b + self.a;
	};
};

class B inherits A
{
	c : Int;

	def sum : Int(a : Int, b : Int, self : B)
	{
		return a + b + self.a + self.c;
	};

	def setsum : Int(a : Int, b : Int, self : B)
	{
		
		{
			self.c <- (self.sum(a,b));
			return 0;;
		}
	};
};

class C inherits B
{
	d : Int;

	def me : Int(self : C)
	{
		{
			self.setsum(99,101);
			out_int(self.c);
			out_int(self.d);
			return 0;;
		}
	};
};

class Main
{
	a : A <- new A;
	k : B <- new B;
	man : C <- new C;
	def main : Int()
	{
		{

			k.a <- 100;
			k.b <- 200;
			k.c <- 300;

			a.a <- 1000;
			a.b <- 2000;

			man.a <- 10000;
			man.b <- 20000;
			man.c <- 30000;

			out_int	(k.sum(2,3));
			out_string("a");
			out_int (k@A.sum(2,3));
			out_string("a");
			
			k.setsum(5,7);
			out_int(k.c);

			out_string("1");

			out_int (a.sum(99,1));

			man.d <- ~9;
			man.me();
			
		}
	};
};