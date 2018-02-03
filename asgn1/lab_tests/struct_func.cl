class T{
	a : String;
	b : Int;
	c : String;
	d : Int;
	e : Int;
	name : String;
	f : String;
	
	init() : SELF_TYPE {
	{
		a <- "a";
		b <- 47114711;
		c <- "c";
		d <- 1234;
		e <- 3;
		f <- "*";
		name <- "abc";
	}
	};

};

class Main{
	k : T;
	main(): SELF_TYPE{
		k <- new T;
		k.init();
	};
};




