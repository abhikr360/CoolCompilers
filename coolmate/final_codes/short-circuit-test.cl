class Main {
	
	b_ : Int <-4;
	a : Int;
	def main : SELF_TYPE (){
	{
		if(((b_<1 and b_<=8) or b_<~1) and (not (b_ > 1) or (b_=9 or b_>=10))) then
		{
		a<-1;
		out_int(a);
		}
		else
		{
		a<-0;
		out_int(a);
		}
		fi;
	}
	};		
};