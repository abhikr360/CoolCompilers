class Chinese inherits IO {
	i : Int[2];
   def  main : SELF_TYPE () {
   	   		
   	   	for(i<-0;i<10;i<-i+1)loop
			i<-i+i
		pool    
   	};
		

};

class Main inherits IO {
	
		i : Int[2];
		a : Chinese;
		def main2 : SELF_TYPE () {
			a.main()
		};




		

};
