class Node{
	data : Int;
	left : Node; 
	right : Node; 

	def set_data : Int(n : Int, self : Node){
		{
			self.data <- n;
			return 1;;
		}
	};

	def set_left : Int(next_node : Node, self : Node){
		{
			self.left <- next_node;
			return 1;;
		}
	};
	def set_right : Int(next_node : Node, self : Node){
		{
			self.right <- next_node;
			return 1;;
		}
	};
	def print_data : Int(self : Node){
		{
		out_int(self.data);
		out_string("\n");
		}
	};
};

class Main{

	n : Int;
	i : Int;
	head : Node;
	temp : Node;
	arr : Node[2];

	def printTree : Int (head : Node){
		if (not isvoid(head)) then
		{
			4;
			printTree(head.left);
			head.print_data();
			printTree(head.right);
		}
		else
			1
		fi
	};

	def main : Int (){
		{
			
			n <- 10;
			i<-1;

			arr[0] <- new Node;
			(arr[0]).set_data(5);

			arr[1] <- new Node;
			(arr[1]).set_data(12);

			temp <- new Node;
			temp.set_data(13);

			temp.set_left(arr[0]);
			temp.set_right(arr[1]);

			head <- temp;

			temp <- new Node;
			temp.set_data(21);
			head.left.set_left(temp);

			temp <- new Node;
			temp.set_data(33);
			head.left.left.set_right(temp);

			temp <- new Node;
			temp.set_data(11);
			head.right.set_left(temp);



			printTree(head);
			(*for (i <- 0;i<n;i<-i+1) loop
			{
				temp <- new Node;
				temp.set_data(i+5);
				temp.next <- head;
				head <- temp;
				
			}
			pool;

			out_string("121");
			while (not isvoid(head)) loop

			{
				head.print_data();
				out_string("121");

				head <- head.next;
			}
			pool;*)

		}
	};

};