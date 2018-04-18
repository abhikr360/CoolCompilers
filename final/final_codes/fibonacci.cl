
class Main {
   n : Int <- 4;
   m : Int <- ;
   def fact : Int (n: Int, m: Int){
      if n+m<3 then
         return n+m;
      else
         return (n+m)*fact(n-1, m) ;
      
      fi
   };

   def  main : SELF_TYPE () {

      {
         let prev : Int <-fact(n, m) in
            out_int(prev)
         tel;
      }

   };

   
};