class Node{
	data : Int;
	next : Node; 

	def set_data : SELF_TYPE(n : Int, self : Node){
		{
			self.data <- n;
		}
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
			
			n <- 1;
			i<-1;
			list[1] <- new Node;
			list[1].data <- 4;
			(*if(i>0) then
				list[i].set_next(list[i-1])
			else
				1
			fi;*)
			out_int(i);
			list[1].print_data();
			(*for (i <- 0;i<n;i<-i+1) loop
			{
				list[i] <- new Node;
				list[i].set_data(i);
				if(i>0) then
					list[i].set_next(list[i-1])
				else
					1
				fi;
				out_int(i);
				list[i].print_data();
				
			}
			pool;*)

		}
	};

};