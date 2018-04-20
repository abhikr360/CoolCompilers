
class Main
{
	a : String <- "Hello W\n";
	b : String;
	c : Do <- new Do;
	d_size : Int <- 10;
	d : Int[10];

	def main : Int ()
	{
		{
			a <- "Goodbye\n";
			b <- "popo\n";
			out_string(a);
			out_string(b);


			let i : Int <- 0 in 
			{
				for (i <- 0; i < d_size; i<-i+1)loop
				{
					d[i] <- i*i*i + 1;				
				}pool;
				
			}  tel;

			c.hello(d, b, d_size);
			a <- c.greet("Tushar");
			out_string(a);

		}
	};
};