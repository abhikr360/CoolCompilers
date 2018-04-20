class Node{
	data : Int;
	next : Node; 

	def set_data : Int(n : Int, self : Node){
		{
			self.data <- n;
			return 1;;
		}
	};

	def set_next : Int(next_node : Node, self : Node){
		{
			self.next <- new Node;
			self.next <- next_node;
			return 1;;
		}
	};
	def print_data : Int(self : Node){
		{
		out_int(self.data);
		return 1;;
		}
	};
};

class Main{

	n : Int;
	i : Int;
	head : Node;
	temp : Node;
	fast : Node;
	slow : Node;

	def main : Int (){
		{
			
			n <- 20;
			i<-1;

			for (i <- 0;i<n;i<-i+1) loop
			{
				temp <- new Node;
				temp.set_data(i+5);
				temp.next <- head;
				head <- temp;				
			}
			pool;

			out_string("121");

			fast <- head;
			slow <- head;

			((fast.next).next).print_data();

			while ( (not isvoid(fast)) and (not isvoid(fast.next)) )(*and (not isvoid((fast.next).next)) )  *)
			loop

			{
				
				fast<- (((fast).next).next);
				slow <- slow.next;
			}
			pool;

			slow.print_data();

		}
	};

};