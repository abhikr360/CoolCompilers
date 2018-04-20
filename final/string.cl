(*class Do {
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
};*)
class Main
{
	a : String;
	b : String;
	c : Int <- 5;
	(*c : Do <- new Do;*)

	def main : Int ()
	{
		{
			a <- "Goodbye\n";
			b <- "popo";
			(*copy_string(a,b);
			out_string(a);
			out_string(b);*)

			concat_string(a,b);
			out_string(a);
			out_string(b);

		}
	};
};