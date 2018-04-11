class Main
{
	arr : Int[5];
	def merge : Int (arr[] : Int, l : Int, m : Int, r : Int)
	{
		let n1 : Int, n2 : Int in
		{
			n1 <- m - l + 1;
			n2 <- r - m;

			let l : Int[5], r : Int[5], i : Int, j : Int, k : Int in 
			{

				for (i<-0; i<n1; i<-i+1) loop
					l[i] <- arr[l+i]
				pool;

				for (j<-0; j<n2; j<-j+1) loop
					r[j] <- arr[m+1+j]
				pool;

				i<-0;
				j<-0;
				k<-l;

				while (i < n1 and j < n2) loop
				{
					if (l[i] <= r[j]) then
					{
						arr[k] <- l[i];
						i <- i+1;
					}
					else
					{
						arr[k] <- r[j];
						j <- j+1;
					}
					fi;
					k <- k+1;
				}
				pool;

				while (i < n1) loop
				{
					arr[k] <- l[i];
					i <- i+1;
					k <- k+1;
				}
				pool;

				while (j < n2) loop
				{
					arr[k] <- r[j];
					j <- j+1;
					k <- k+1;
				}
				pool;
			}
			tel;
		}
		tel
	};

	def sort : Int (arr[] : Int, l : Int, r : Int)
	{
		if (l < r) then
			let m : Int in
			{
				m <- (l+r)/2;
				sort(arr, l, m);
				sort(arr, m+1, r);

				merge(arr, l, m, r);
			}
			tel
		else 1
		fi
	};

	def out_int : Int (a : Int)
	{
		1
	};

	def out_string : Int (a : Int)
	{
		1
	};

	def main : Int ()
	{
		{
			arr[0] <- 3;
			arr[1] <- 1;
			arr[2] <- 2;
			arr[3] <- ~1;
			arr[4] <- 0;

			sort(arr, 0, 5);

			let i : Int in
				for (i <- 0; i < 5; i <- i+1) loop
				{
					out_int(arr[i]);
					out_string("\n");
				}	
				pool
			tel;
		}
	};
};