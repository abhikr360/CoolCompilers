class Do {
	def hello : Int (b[] : Int, a : String, b_size : Int, self : Do){
		{
			out_string(a);
			out_string("\n");
			let i : Int <- 0 in 
			{
				for (i <- 0; i < b_size; i<-i+1)loop
				{
					out_string(a);
					out_int((b)[i]);
					out_string("\n");				
				}pool;

			}  tel;		
		}

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