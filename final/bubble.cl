class Main
{
	arr : Int[7];

	def sort : Int (arr[] : Int, n : Int)
	{
		{
			let i : Int, j : Int, temp : Int in 
				for (i<-0;i<n ; i<-i+1 )loop
					for (j <- 1 ;j<(n-i);j<-j+1)loop
						if((arr[j-1]) > (arr[j])) then 
						{
		                    temp <- (arr[j-1]);
		                    arr[j-1] <- (arr[j]);
		                    arr[j] <- temp;
						}
						else 
							4
						fi
					pool
				pool	
			tel;
		}
	};

	def main : Int ()
	{
		{
			arr[0] <- 30;
			arr[1] <- 10;
			arr[2] <- 2;
			arr[3] <- 15;
			arr[4] <- 0;
			arr[5] <- ~12;
			arr[6] <- 14;

			sort(arr, 7);

			let i : Int in
				for (i <- 0; i < 7; i <- i+1) loop
				{
					out_int(arr[i]);
					out_string(" ");
				}	
				pool
			tel;
			out_string("\n");
		}
	};
};