class Main{
	e : Int;
	bar : Int;
	c : Int;
	d : Int;
	
	def main : Int(){
		{
			if ((c>0) and (d>0)) then 
				d<-d+1
			else
				if ((d>0) and (e>0)) then
				e<-e+1
				else
					d<-d-1
				fi
			fi;
		}
	};
};