class Main
{
	a : Int;
	b : Int;

	def main : Int ()
	{
		{
			a <- 2;
			b <- 1+3*8/7-7+5;
			out_int(b);
			out_string(" \n");
			b <- 1+2+3+4+5+6+7+8+9+10+11+12+13+14+15+16+17+18+19+20;
			out_int(b);
			
		}
	};
};