class Japanese inherits IO {
	i : Int[2];
   def  main2 : SELF_TYPE (b : Int) {
   	   	
   	   	for(i<-0;i<10;i<-i+1)loop
			i<-i+i
		pool
   	};

};

class Main inherits IO {
	
		i : Int[2];
		b : String;
		c : Japanese;
		
		def main : SELF_TYPE (a : Int, b : Int) {
			{
				c.main2(i,c,b);
				b <- 2;
				let c : Int <- 0 in 
				b <- 4
				tel;
				let s : String,c : Int in
					let p : Int in
						s <- p
					tel
				tel;
			}
		};		

};
