class Chinese inherits IO {
	i : Int[2];
   def  main : SELF_TYPE () {
   	   		
   	   	for(i<-0;i<10;i<-i+1)loop
			i<-i+i
		pool    

   	};
   	def out_string : String () {
   		"asasasasa"
   	};
			

};


class Main inherits IO {
	
		i : Int[2];
		b : String <- "hello word";
		a : Chinese;
		def main2 : SELF_TYPE () {
			{
				a.main();
				let b : Int , c : Int[5] in 
				{

					let c : Int in 
						c[0] <- b[1]*c
					tel;
					b <- b+c;
				}
				tel;
			}
		};

};
