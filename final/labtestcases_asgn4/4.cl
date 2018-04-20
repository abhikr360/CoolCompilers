class Main{
	a : Int;
	bar : Int;

	def foo : Int(){
		bar<-1
		(* do something with bar*)
	};
	
	def main : Int(){
		{
			foo();
			a<-bar;
		}
	};

};