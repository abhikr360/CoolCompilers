class Node{
	data : Int;
	next : Node; 

	def set_data : SELF_TYPE(n : Int, self : Node){
		self.data <- n
	};

	def set_next : SELF_TYPE(next_node : Node, self : Node){
		{
			self.next <- new Node;
			self.next <- next_node;
		}
	};
	def print_data : SELF_TYPE(self : Node){
		out_int(self.data)
	};
};

class Main{

	n : Int;
	i : Int;
	list : Node[6];
	no : Node;

	def main : Int (){
		{
			
			n <- 6;
			no <- new Node;
			for (i <- 0;i<n;i<-i+1) loop
			{
				out_int(i);
				list[i] <- new Node;
				list[i].set_data(i);
				if(i>0) then
					list[i].set_next(list[i-1])
				else
					1
				fi;
				list[i].print_data();
				out_int(i);
				
			}
			pool;

		}
	};

};