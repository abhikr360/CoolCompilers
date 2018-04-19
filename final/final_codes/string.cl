class Do {
	def hello : Int (a : String, self : Do){
		out_string(a)
	};
	def greet : String (name : String, self : Do)
	{
		{
			out_string("Hello ");
			out_string(name);
			return "\ndude\n";;
		}
	};
};
class Main
{
	a : String <- "Hello W\n";
	b : String;
	c : Do <- new Do;

	def main : Int ()
	{
		{
			a <- "Goodbye\n";
			b <- "popo";
			out_string(a);
			out_string(b);


			c.hello(b);
			a <- c.greet("Tushar");
			out_string(a);

		}
	};
};