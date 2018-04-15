class Kotha{
	houseno : Int;
	manager : Int; 
};
class Randi{
	price : Int;
	numfucks : Int;
	diameter : Int;
	customers : Int[5];
	address : Kotha[4];
};

class Main{
	khetan : Randi <- new Randi;
	arjun : Randi;
	a : Int <- 4;

	hall12 : Kotha;

	def printrandis : SELF_TYPE (){
		{
			out_int(a);
			out_int(arjun.diameter);
			out_int(khetan.numfucks);
			out_int(khetan.price);
		}
	};

	def main : Int (){
		{
		out_int(a);

		(khetan.customers)[0] <- 1;
		(*(khetan.customers)[1] <- khetan.customers[0] + 1;
		(khetan.customers)[2] <- khetan.customers[1] + 1;
		(khetan.customers)[3] <- khetan.customers[2] + 1;
		(khetan.customers)[4] <- khetan.customers[3] + 1;
		khetan.price <- 11;*)


		out_int(khetan.customers[0]);
		khetan.numfucks <- 999;
		arjun <- new Randi;
		hall12 <- new Kotha;
		hall12.manager <- 69;
		arjun.address[1] <- hall12;
		khetan.address[2] <- arjun.address[1];
		out_int(khetan.address[2].manager);
		out_int(arjun.address[1].manager);
		arjun.diameter<-4;
		arjun.customers[0] <- 555;
		out_int(arjun.customers[0]);
		printrandis();
		}
	};

};