class Randi{
	price : Int;
	numfucks : Int;
	diameter : Int;
};

class Main{
	khetan : Randi <- new Randi;
	arjun : Randi;
	a : Int <- 4;


	def printrandis : SELF_TYPE (){
		{
			out_int(a);
			out_int(arjun.diameter);
			out_int(khetan.numfucks);
			out_int(khetan.price);
		}
	};

	def main : Int (){{
		out_int(a);
		khetan.price <- 11;
		khetan.numfucks <- 999;
		arjun <- new Randi;
		arjun.diameter<-4;
		printrandis();
		}
	};

};