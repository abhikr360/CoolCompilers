class Test{
	i : Int;
	j : Int;


	def print2darray : Int (arr[][3]: Int , n :Int, self : Test){
	{	

		(*out_int(n);
		out_int(arr[0][0]);
		out_int(arr[0][1]);
		out_int(arr[0][2]);
		out_int(arr[1][0]);
		out_int(arr[1][1]);
		out_int(arr[1][2]);
		out_int(arr[2][0]);
		out_int(arr[2][1]);
		out_int(arr[2][2]); *)

		for (self.i<-0; self.i<3;self.i<-self.i+1 ) loop
		{	out_string("h ");
			for (self.j <-0 ; self.j<3 ;self.j <-self.j+1 ) loop{
				out_int(arr[self.i][self.j]);
			}
			pool;
		}
		pool;
	}
	};


};
(**)

class Main
{	n : Int<-3;
	arr : Int[n][3];
	obj : Test;
	i : Int;
	m : Int <- 0;
	j : Int <- 0;

	def main : Int ()
	{
		{
			(*arr[0][0] <- 1;
			arr[0][1] <- 2;
			arr[0][2] <- 3;
			arr[1][0] <- 4;
			arr[1][1] <- 5;
			arr[1][2] <- 6;
			arr[2][0] <- 7;
			arr[2][1] <- 8;
			arr[2][2] <- 9;


			let n:Int <- 20, arr : Int [3][3], m : Int <- 10 in {
			arr[0][0] <- ~1;
			arr[0][1] <- ~2;
			arr[0][2] <- ~3;
			arr[1][0] <- ~4;
			arr[1][1] <- ~5;
			arr[1][2] <- ~6;
			arr[2][0] <- ~7;
			arr[2][1] <- ~8;
			arr[2][2] <- ~9;

			out_int(arr[0][0]);
			out_int(arr[0][1]);
			out_int(arr[0][2]);
			out_int(arr[1][0]);
			out_int(arr[1][1]);
			out_int(arr[1][2]);
			out_int(arr[2][0]);
			out_int(arr[2][1]);

			out_int(n*m);
			}tel; *)

			for (i<-0; i<n;i<-i+1 ) loop
				for (j<-0;j<3 ;j<-j+1 ) loop{
					arr[i][j]<-m;
					m<-m+1;
					out_string("g ");
				}
				pool
			pool;
			obj <- new Test;
			obj.print2darray(arr, 3);
			(*out_int(arr[2][2]);*)
		}
	};
};