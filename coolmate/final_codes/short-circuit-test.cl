class Main inherits IO {
	
	b_ : Int <-4;
	a : Int;
	def main : SELF_TYPE (){
	{
		if(((b_<1 and b_<=8) or b_<~1) and (not (b_ > 1) or (b_=9 or b_>=10))) then
		a<-1
		else
		a<-0
		fi;
	}
	};		
};