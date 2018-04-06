class Main inherits IO {
	
	i : Int[2];
	b : Int <-4;
	(*c : Int<-6;*)
	(*a : Int <- 9;*)

	def main : SELF_TYPE (){
	{
		if( ((b<1 and b<8) or b>~1) and (b >1 or (b<9 or b<10)) ) then
		i[0] <- 10
		else
		b <- i[1]
		fi;
	}
	};		
};
(*if(b<c+1 and (b>c-1 or (a >1 and a<10)))*)