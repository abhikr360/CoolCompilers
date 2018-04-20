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