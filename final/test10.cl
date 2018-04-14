class Main inherits IO {
   n : Int [3];
   m : Int [6];
   (*def fib : Int (n: Int){
      if n<3 then
         return 1;
      else
         return fib(n-1)+fib(n-2) ;
      
      fi

   }; *)

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
         m[0] <- 5;
        m[1] <- 1;
         m[2] <- 2;
         m[3] <- 3;
         m[4] <- 4;
         m[5] <- 3;
         let a : Int [4] in
         {
            a[m[m[5]]] <- m[1];
            out_int(a[3]);
         }
         tel;

         out_int(m[m[m[5]]]);





      }

   };

   
};

