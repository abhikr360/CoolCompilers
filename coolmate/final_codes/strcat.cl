
class Main
{
	a : String;
	b : String;

	def main : Int ()
	{
		{
			a <- "Goodbye";
			b <- "popo";
			(*copy_string(a,b);
			out_string(a);
			out_string(b);*)
			out_string("Before concatnaing : \n");
			out_string(" a : ");
			out_string(a);
			out_string("\n b : ");
			out_string(b);

			concat_string(a,b);
			out_string("\nAfter concatinating a : \n");
			out_string(a);

		}
	};
};