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

	def main : Int (){
		{
			
			n <- 5;
			i<-1;
			(*list[1] <- new Node;
			list[1].data <- 4;
			(*if(i>0) then
				list[i].set_next(list[i-1])
			else
				1
			fi;*)
			for (i <- 0;i<n;i<-i+1) loop
			{
				temp <- new Node;
				temp.set_data(i+5);
				temp.next <- head;
				head <- temp;
				(*if(i>0) then
					list[i].set_next(list[i-1])
				else
					1
				fi;
				out_int(i);
				list[i].print_data();*)
				
			}
			pool;

			out_string("\n");
			while (not isvoid(head)) loop

			{
				head.print_data();
				out_string(" ");

				head <- head.next;
			}
			pool;

		}
	};

};