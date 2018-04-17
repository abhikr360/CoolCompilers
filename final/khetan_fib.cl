class Main inherits IO {
   i:Int <- 5;
   def fib : Int (n: Int, m : Int){
      {
         out_int(m);
      if n<3 then
         return n;
      else
         return fib(n-1, m-1) + fib(n-2, m-2) ;

      fi;

   }
   };

   def  main : SELF_TYPE () {

      let a : Int, b : Int in{
            a <- 5;
            b<-3;
            out_int(fib(a+b, a));
            out_int(fib(a-b, 5));
         }
         tel
   };

   
};
