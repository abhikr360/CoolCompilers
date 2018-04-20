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
			out_string(name);
		}
	};
};
class Lo {
	def hello : Int (a : String, self : Do){
		out_string(a)
	};
	def neet : String (name : String, self : Do)
	{
		{
			out_string("Hello ");
			out_string(name);
			self.hello(name);
			return "\ndude\n";;
		}
	};
};*)
class Main
{
	(*a : String <- "Hello W\n";
	b : String;
	n : Int <- 6;
	c : Do <- new Do;
	l : Lo <- new Lo;
	d : Int[6]*)
	i : Int;
	def main : Int ()
	{
		{
			(*for (i<- 0; i<10;i<-i+1)loop
			{
				
				if (i<3) then
				{
					continue;
				}
				else{
					4;
				}
				fi;
				out_string(" ");
				out_int(i);
			}	



			pool;
			*)
			i<- 0;

			while(i<10)loop{
				if (i<3) then
				{
					i<-i+1;
					continue;
				}
				else{
					4;
				}
				fi;
				out_int(i);
				out_string(" ");
				i<-i+1;
			}pool;
 		}
	};
};