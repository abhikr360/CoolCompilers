class Secure {
   private aa : Int;
   public bb : Int;
   private cc : Int;
   dd : Int;

   def set : Int(n : Int, m: Int, self : Secure){
      {
      self.aa <- n;
      self.bb <- m;
      }
   };

   def get_aa : Int(self : Secure){
      return self.aa;
   };

   def get_bb : Int(self : Secure){
      return self.bb;
   };

   def  printdata : Int (self : Secure){
      {
      out_int(self.aa);
      out_string(" ");
       out_int(self.bb);
      out_string(" ");
       out_int(self.cc);
      out_string(" ");
       out_int(self.dd);
      out_string(" ");
      }
   };
};

class Shukla inherits Secure {
   ee : Int;
   private ff : Int;

   def private printdata : Int(self : Shukla){
      {
      out_string(" ");
       out_int(self.bb);
      out_string(" ");
      out_string(" ");
       out_int(self.dd);
      out_string(" ");
      out_int(self.ee + 1);
      out_string(" ");
      out_int(self.ff + 2);
      out_string(" ");

      }
   };
};

class Sec_course inherits Shukla{
   private gg : Int;
   hh : Int;

};

class Main {
   n : Int <- 4;
   m : Int <- 2 ;

   def  main : SELF_TYPE () {

      {
         let obj : Sec_course , nv : Shukla, obj1 : Shukla in 
         {
            obj1 <- new Shukla;
            obj <- new Sec_course;
            nv <- new Shukla;
            obj.set(4,5);
            obj.printdata();


         }tel;
      }

   };

   
};