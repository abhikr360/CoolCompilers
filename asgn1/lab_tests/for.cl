class Main inherits IO{
   	i : Int
   main(): Int {
	{
   	i <- 6;
   	for(;i<= 8 and i>= 6 and not(i== 7); i<-i+1)
   	loop{
   		if(i>=0) 
   		then out_string("yes\n")
   		else out_string("no\n")
   		fi;
   	}
   	pool;
   	0;
	}
   };
};
