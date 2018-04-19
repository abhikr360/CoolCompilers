class Main{
	a : Int;
	bar : Int;

	def foo : Int(a:Int){
		bar<-1
		(* do something with bar*)
	};
	
	def main : Int(){
		{
			foo(a);
			a<-bar;
		}
	};

};