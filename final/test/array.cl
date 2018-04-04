class Main
{
	arr : Int[5];
	def merge : Int (arr[] : Int, l : Int, m : Int, r : Int)
	{
		let n1 : Int, n2 : Int in
		{
			n1 <- m - l + 1;
			n2 <- r - m;

			let l : Int[5], r : Int[5], i : Int in 
			{

				for (i<-0; i<n1; i<-i+1) loop
					l[i] <- arr[l+i]
				pool;
			}
			tel;
		}
		tel
	};
};