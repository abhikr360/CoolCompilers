class Main inherits IO{
	i : Int;
	j : Int;
	k : Int;
	res : Int;

	main() : SELF_TYPE{
	{
		for({res <- 0; i <- 0 }; i < 10; i <- i+1)loop
			for(j <- 0; j < 10; j <- j+1)loop
				for(k <- 0; k < 10; k <- k+1)loop
					res <- res+1;
				pool;
			pool;
		pool;
		out_string("res = ");
		out_int(res);
		out_string("\n");
	}


	};


};
