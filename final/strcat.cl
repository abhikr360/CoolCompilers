
class Main
{
	a : String;
	b : String;

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