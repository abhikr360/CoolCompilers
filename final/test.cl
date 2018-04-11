class Chinese inherits IO {
	i : Int[3];
	b : Int <- 5;
	c : String;
	d : Bool;
   def  main : SELF_TYPE () {
   	   		

   	   	{
   	   		b <- ~5%b;
   	   		
   	   	(*for(i<-0;i<10;i<-i+1)loop
   	   	    			i<-i[1]+i[0]
   	   	    		pool;*)

   	   		d <- d <- ~b=0 and TRUE ;
   	   		b <- ~b;
   	   		i[1] <- b+b;
   	   		i[0] <- b;
   	   		b <- 55;
   	   		b <- b/3;
   	   		i[2] <- b+b;
   	   	} 

   	};
   	def out_string : String () {
   		c<-"asasasasa"
   	};
   	def out_string_second : String () {
   		c<-"asasasasa"
   	};
			

};


(*
class Main inherits IO {
	
		i : Int[2];
		b : String <- "hello word";
		a : Chinese;
		def public main2 : Object (f[] : Int, b : String) {
			{
				a.main(b,f);
				let b : Int , c : Int[5] , d : String in 
				{
					let c : Int in 
					{
						c[0] <- b[~2*2+123]+1/10- c%12;
						c <- 5;
					}
					tel;
						b <- b+c;
						for (i<-0;i>18 and i>20 ; i<- i+1 ) loop
							FALSE
						pool;

				}
				tel;
			}
		};

};*)
