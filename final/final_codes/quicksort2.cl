class Main
{
	arr : Int[10];

	def quicksort : Int (arr[] : Int,first : Int, last : Int){
		let pivot : Int, i : Int, j : Int, temp : Int, f : Int, e : Int , a : Int in 
		{
			if(first<last) then 
			{
				pivot <- (arr[last]);
				i <- first-1;

				(*while(i<j) loop
				{
					while(arr[i] <= (arr[pivot]) and i<last)loop
						i <- i+1
					pool;
					while(arr[j] > (arr[pivot]))loop
						j <- j-1
					pool;
					if (i<j) then 
					{
						temp <- (arr[i]);
						arr[j] <- (arr[i]);
						arr[i] <- temp;
					}
					else
						1
					fi;

				}
				pool;*)

				for (j <- first;j<last;j<-j+1)loop
					if(arr[j]<= pivot) then 
					{
						i<- i+1;
						temp <- (arr[i]);
						arr[i] <- (arr[j]);
						arr[j] <- temp;
					}
					else
						1
					fi
				pool;

				temp <- (arr[i+1]);
				arr[i+1] <- (arr[last]);
				arr[last] <- temp;

				quicksort(arr,first,i);
				quicksort(arr,i+2,last);


			}	
			else
				1
			fi;
		}tel
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
			arr[7] <- ~14;
			arr[8] <- ~100;
			arr[9] <- 1000;


			quicksort(arr, 0, 9);

			let i : Int in
				for (i <- 0; i < 10; i <- i+1) loop
				{
					out_int(arr[i]);
					out_string(" ");
				}	
				pool
			tel;
		}
	};
};