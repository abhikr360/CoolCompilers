
class Main{

	n : Int;
	i : Int;
	def ack : Int (m : Int, n : Int){
		let i : Int <- ~1,j : Int <- ~1 in 
		{
			if(m>=0 and n >=0) then
			{
				if(m=0) then 
					i <- n+1
				else
					{
						if (n=0) then 
							i <- ack(m-1,1)
						else
						{
							j<- ack(m,n-1);
							i <- ack(m-1,j);
						}fi;
					}	
				fi;			
			}
			else
				 1
			fi;
			return i;;
		}
		tel
	};

	def main : Int (){
		{
			n <- ack(1,4);
			out_int(n);
		}
			
};

};