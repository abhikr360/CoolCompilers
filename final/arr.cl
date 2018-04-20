class Main
{
	arr : Int[7][7];

	def sort : Int (arr[] : Int,l :Int)
	{
		{
			out_int(arr[0]);
			out_int(arr[1]);
			out_int(l);
		}
	};

	def main : Int ()
	{
		{
			arr[0] <- 3;
			arr[1] <- 1;
			arr[2] <- 2;
			arr[3] <- 10;
			arr[4] <- 0;
			arr[5] <- 12;
			arr[6] <- 14;

			sort(arr,2);

			(*let i : Int in
				for (i <- 0; i < 7; i <- i+1) loop
				{
					out_int(arr[i]);
					out_string(" ");
				}	
				pool
			tel;*)
		}
	};
};