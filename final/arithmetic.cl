class Arith
{
   def mul : Int( n : Int, m : Int, self : Arith)
   {
      let i : Int, ans : Int <- 0 in
      {
         for(i<-0; i<m; i<-i+1) loop
         {
            ans <- ans + n;
         }pool;
         return ans;;

      }
      tel
   };

   def add : Int( n : Int, m : Int, self : Arith)
   {
      let i : Int, ans : Int <- n in
      {
         for(i<-0; i<m; i<-i+1) loop
         {
            ans <- ans + 1;
         }pool;
         return ans;;

      }
      tel
   };

   def power : Int( n : Int, m : Int, self : Arith)
   {
      let i : Int, ans : Int <- 1 in
      {
         for(i<-0; i<m; i<-i+1) loop
         {
            ans <- ans*n;
         }pool;
         return ans;;

      }
      tel
   };

   def log : Int( n : Int, m : Int, self : Arith)
   {
      let i : Int, ans : Int <- 0 in
      {
         for(i<-0; ans/m = 1; i<-i+1) loop
         {
            ans <- ans/m;
         }pool;
         return ans;;

      }
      tel
   };



};

class Main inherits IO {
   n : Int <- 10000;
   m : Int <- 10;
   arith : Arith <- new Arith;

   def  main : SELF_TYPE () {
         {
            out_int(arith.add(n, m));
            let k : Int in 
            {
               scan_int(k);
               out_int(k);
            }tel;

         }
      };

   

   
};