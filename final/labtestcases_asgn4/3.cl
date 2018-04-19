class Main{
	i : Int;
	a : Int;
	t : Int;
	def main : Int(){
		{
			for (i<-0;{t<-(i<100);i<-i+1;t;};1)loop
			{
				a<-a+1;
				out_int(i);
			}
			pool;
			
		}
	};
};