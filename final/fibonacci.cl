(*class Main inherits IO {
   n : Int <- 6;
   def fib : Int (n: Int){
      if n<3 then
         return 1;
      else
         return fib(n-1)+fib(n-2) ;
      
      fi

   };

   def  main : SELF_TYPE () {

      {
         for (i<-0 ; i<10 ; i<- i+1)loop
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

         pool;
         let prev : Int <-fib(n) in
            out_int(prev)
         tel;
      }

   };

   
};
*)

(*class Main inherits IO {
   n : Int <- 6;
   def fact : Int (n: Int){
      if n<3 then
         return n;
      else
         return fact(n-1)*n ;
      
      fi

   };

   def  main : SELF_TYPE () {

      {
         for (i<-0 ; i<10 ; i<- i+1)loop
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

         pool;
         let prev : Int <-fact(n) in
            out_int(prev)
         tel;
      }

   };

   
};*)

class Main inherits IO {
   n : Int <- 4;
   m : Int <- 1;
   def fact : Int (n: Int, m: Int){
      if n+m<3 then
         return n+m;
      else
         return (n+m)*fact(n-1, m) ;
      
      fi
   };

   def  main : SELF_TYPE () {

      {
         (*for (i<-0 ; i<10 ; i<- i+1)loop
            out_int(i)
            {
               let var1 : Int <-10, var2 : Int<-9 in
                  let var3 : Int <- 6 in
                     var1 <- var3 < 10
                  tel
               tel;
               let var1 : Int in 
                  var1 <- i
               tel;

            }

         pool;*)
         let prev : Int <-fact(n, m) in
            out_int(prev)
         tel;
      }

   };

   
};