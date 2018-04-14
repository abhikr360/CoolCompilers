class Randi{
	price : Int;
	numfucks : Int;
	diameter : Int;
};

class Main{
	khetan : Randi <- new Randi;
	arjun : Randi;

	def main : Int (){{
		khetan.price <- 11;
		khetan.numfucks <- 999;
		arjun <- new Randi;
		arjun.diameter<-4;
		}
	};

};