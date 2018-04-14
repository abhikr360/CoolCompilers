class Main inherits IO {
   n : Int;
   m : Int;
   def fib : Int (n: Int){
      if n<3 then
         return 1;
      else
         return fib(n-1)+fib(n-2) ;
      
      fi

   };

   def  main : SELF_TYPE () {

      {
         (*for (i<-0 ; i<10 ; i<- i+1)loop
            out_int(i)
            {
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
         n <- 3;
         let prev : Int <-fib(n) in
            out_int(prev)
         tel;
      }

   };

   
};

