(*class Japanese inherits IO {
	i : Int[2];
   def  main2 : SELF_TYPE (b : Int) {
   	   	
   	   	for(i<-0;i<10;i<-i+1)loop
			i<-i+i
		pool
   	};

};*)

class Main inherits IO {
	
		i : Int[2];
		b : Int;
		
		def main : SELF_TYPE (a : Int) {
			{
				b <- 2;
				let c : Int <- 0 in 
				b <- 4
				tel;
				let s : Int,c : Int in
					let p : Int in
						s <- p
					tel
				tel;
			}
		};
		def do : Int (a : Int,b :Int) {
			let s : Int,c : Int in
					let p : Int in
						main(a,b) 
					tel
				tel

		};		

};
