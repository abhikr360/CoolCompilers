class Main inherits IO {
	arr : Int[10];
	i : Int ;
   def  main : SELF_TYPE () {

      {
         (*for (i<-0 ; i<10 ; i<- i+1)loop
            out_int(i)*)
            {
               arr[i] <- 2*i;
               (*let var1 : Int <-10, var2 : Int<-9 in
                  let var3 : Int <- 6 in
                     var1 <- var3 < 10
                  tel
               tel;
               let var1 : Int in 
                  var1 <- i
               tel;

            }

         pool;*)
         fib(3)
      }

   };

   def fib : Int (n: Int){
      if(n<3){
         3
      }
   };
};