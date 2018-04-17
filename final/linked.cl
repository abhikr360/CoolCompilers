class Node{
	data : Int;
	next : Node; 

	def set_data : SELF_TYPE(n : Int, self : Node){
		self.data <- n
	};

	def set_next : SELF_TYPE(next_node : Node, self : Node){
		self.next <- next_node
	};
};

class Main{

	n : Int;
	i : Int;
	list : Node[6];
	no : Node;

	def main : Int (){
		{
			out_int(7);
			n <- 6;
			no <- new Node;
			list[0] <- new Node;
			(*for (i <- 0;i<n;i<-i+1) loop
			{
				list[i] <- new Node;
				list[i].set_data(i);
				if(i>0) then
					list[i].set_next(list[i-1])
				else
					list[i].set_next(list[i-1])
				fi;
				out_int(i);
			}
			pool;*)

		}
	};

};