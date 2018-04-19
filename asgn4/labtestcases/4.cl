class Main{
	a : Int;
	bar : Int;

	
	def main : Int(){
		{
			foo();
			a<-bar;
		}
	};

	def foo : Int(){
		bar<-1
		(* do something with bar*)
	};
};