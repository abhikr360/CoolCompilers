class WHATSUP{
   w1 : Int;
   w2 : Int;
   def printme : Int ( n: Int, m:Int, self : WHATSUP){
      {
         self.w1 <- n;
         out_int(self.w2 + m);
         out_int(self.w1);
      }

   };
};

class Fibonacci{
   def fibonacci : Int (n : Int, self : Fibonacci){
      {
         if(n < 3) then
            return n;
         else
            return self.fibonacci(n-1) + self.fibonacci(n-2);
         fi;
      }
   };
};

class Main inherits IO {
   def  main : SELF_TYPE () {

      {
         (*let a : WHATSUP  in
         {
            a<- new WHATSUP;
            a.w2 <- 4;
            a.printme(8, 12);
         }
         tel;*)


         let f : Fibonacci, n : Int in 
         {
            f <- new Fibonacci;
            n <- 3;
            out_int(f.fibonacci(n));
         }
         tel;



      }

   };

   
};

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