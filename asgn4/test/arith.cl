
class A {

   var : Int <- 0;

   def value : Int () { var };

   def set_var : SELF_TYPE (num : Int)  {
      {
         var <- num;
         self;
      }
   };

   def method1 : SELF_TYPE (num : Int) {  
      self
   };

   def method2 : B (num1 : Int, num2 : Int) {  
      let x : Int in
	 {
            x <- num1 + num2;
	    (new B).set_var(x);
	 }
   tel
      
   };

   def method3 : C (num : Int) : C {  
      let x : Int in
	 {
            x <- ~num;
	    (new C).set_var(x);
	 }tel
      
   };

   def method4 : D (num1 : Int, num2 : Int){  
            if num2 < num1 then
               let x : Int in
		  {
                     x <- num1 - num2;
	             (new D).set_var(x);
	          }
               tel
            else
               let x : Int in
		  {
	             x <- num2 - num1;
	             (new D).set_var(x);
		  }
               tel
            fi
   };

   def method5 : E (num : Int){  
      let x : Int <- 1 in
	 {
	    let y : Int <- 1 in
	       while y <= num loop
	          {
                     x <- x * y;
	             y <- y + 1;
	          }
	       pool
	    tel;
	    (new E).set_var(x);
	 }
      tel
   };

};

class B inherits A { 

   def method5 : E (num : Int){ 
      let x : Int in
	 {
            x <- num * num;
	    (new E).set_var(x);
	 }
      tel
   };

};

class C inherits B {

   def method6 : A (num : Int){
      let x : Int in
         {
            x <- ~num;
	    (new A).set_var(x);
         }
      tel
   };

   def method5 : E (num : Int){ 
      let x : Int in
	 {
            x <- num * num * num;
	    (new E).set_var(x);
	 }
      
   };

};

class D inherits B {  
		
   def method7 : Bool (num : Int){  
      (let x : Int <- num in
            if x < 0 then method7(~x) else
            if 0 = x then TRUE else
            if 1 = x then FALSE else
	    if 2 = x then FALSE else
	       method7(x - 3)
	    fi fi fi fi
      )
   };

};

class E inherits D {

   def method6 : A (num : Int){  
      let x : Int in
         {
            x <- num / 8;
	    (new A).set_var(x);
         }
      tel
   };

};

class A2I {

     def c2i : Int (char : String){
	if char = "0" then 0 else
	if char = "1" then 1 else
	if char = "2" then 2 else
        if char = "3" then 3 else
        if char = "4" then 4 else
        if char = "5" then 5 else
        if char = "6" then 6 else
        if char = "7" then 7 else
        if char = "8" then 8 else
        if char = "9" then 9 else
        { abort(); 0; }  (* the 0 is needed to satisfy the
				  typchecker *)
        fi fi fi fi fi fi fi fi fi fi
     };

     def i2c : String (i : Int){
	if i = 0 then "0" else
	if i = 1 then "1" else
	if i = 2 then "2" else
	if i = 3 then "3" else
	if i = 4 then "4" else
	if i = 5 then "5" else
	if i = 6 then "6" else
	if i = 7 then "7" else
	if i = 8 then "8" else
	if i = 9 then "9" else
	{ abort(); ""; } 
        fi fi fi fi fi fi fi fi fi fi
     };

     def a2i : Int (s : String){
        if s.length() = 0 then 0 else
	if s.substr(0,1) = "-" then ~a2i_aux(s.substr(1,s.length()-1)) else
        if s.substr(0,1) = "+" then a2i_aux(s.substr(1,s.length()-1)) else
           a2i_aux(s)
        fi fi fi
     };


     def a2i_aux : Int (s : String){
	let int : Int <- 0 in	
           {	
               let j : Int <- s.length() in
	          let i : Int <- 0 in
		    while i < j loop
			{
			    int <- int * 10 + c2i(s.substr(i,1));
			    i <- i + 1;
			}
		    pool
		  tel
	       tel;
              int;
	    }
        tel
     };


    def i2a : String (i : Int){
	if i = 0 then "0" else 
        if 0 < i then i2a_aux(i) else
          "-".concat(i2a_aux(i * ~1)) 
        fi fi
    };
	

    def i2a_aux : String (i : Int){
        if i = 0 then "" else 
	    let next : Int <- i / 10 in
		i2a_aux(next).concat(i2c(i - next * 10))
	    tel
        fi
    };

};

class Main inherits IO {
   
   char : String;
   avar : A; 
   a_var : A;
   flag : Bool <- TRUE;


   def menu : String (){
      {
         out_string("\n\tTo add a number to ");
         print(avar);
         out_string("...enter a:\n");
         out_string("\tTo negate ");
         print(avar);
         out_string("...enter b:\n");
         out_string("\tTo find the difference between ");
         print(avar);
         out_string("and another number...enter c:\n");
         out_string("\tTo find the factorial of ");
         print(avar);
         out_string("...enter d:\n");
         out_string("\tTo square ");
         print(avar);
         out_string("...enter e:\n");
         out_string("\tTo cube ");
         print(avar);
         out_string("...enter f:\n");
         out_string("\tTo find out if ");
         print(avar);
         out_string("is a multiple of 3...enter g:\n");
         out_string("\tTo divide ");
         print(avar);
         out_string("by 8...enter h:\n");
	 out_string("\tTo get a new number...enter j:\n");
	 out_string("\tTo quit...enter q:\n\n");
         in_string();
      }
   };

   def prompt : String (){
      {
         out_string("\n");
         out_string("Please enter a number...  ");
         in_string();
      }
   };

   def get_int : Int (){
      {
	 let z : A2I <- new A2I in
	    let s : String <- prompt() in
	       z.a2i(s)
	    tel
         tel;
      }
   };

   def is_even : Bool (num : Int){
      let x : Int <- num in
            if x < 0 then is_even(~x) else
            if 0 = x then TRUE else
	    if 1 = x then FALSE else
	          is_even(x - 2)
	    fi fi fi
      tel
   };

   def class_type : SELF_TYPE (var : A){
      
 
   def print : SELF_TYPE (var : A){
     let z : A2I <- new A2I in
	{
	   out_string(z.i2a(var.value()));
	   out_string(" ");
	}
     tel
   };

   def main : Object (){
      {
         avar <- (new A);
         while flag loop
            {
	       out_string("number ");
	       print(avar);
	       if is_even(avar.value()) then
	          out_string("is even!\n")
	       else
	          out_string("is odd!\n")
	       fi;
	       class_type(avar);
	       char <- menu();
                  if char = "a" then 
                     {
                        a_var <- (new A).set_var(get_int());
	                avar <- (new B).method2(avar.value(), a_var.value());
	             } else
                  if char = "b" then 
                     
		                  out_string("Oooops\n");
		                  else
                  if char = "c" then 
                     {
                        a_var <- (new A).set_var(get_int());
	                avar <- (new D).method4(avar.value(), a_var.value());
	             } else
                  if char = "d" then avar <- (new C)@A.method5(avar.value()) else
                  if char = "e" then avar <- (new C)@B.method5(avar.value()) else
                  if char = "f" then avar <- (new C)@C.method5(avar.value()) else
                  if char = "g" then 
		      if ((new D).method7(avar.value()))
		                       then 
			 {
	                    out_string("number ");
	                    print(avar);
	                    out_string("is divisible by 3.\n");
			 }
			 else  
			 {
	                    out_string("number ");
	                    print(avar);
	                    out_string("is not divisible by 3.\n");
			 }
		      fi else
                  if char = "h" then 
		      let x : A in
			 {
		            x <- (new E).method6(avar.value());
			    let r : Int <- (avar.value() - (x.value() * 8)) in
			       {
			          out_string("number ");
			          print(avar);
			          out_string("is equal to ");
			          print(x);
			          out_string("times 8 with a remainder of ");
				  let a : A2I <- new A2I in
				     {
			                out_string(a.i2a(r));
			                out_string("\n");
				     }
				  tel; 
			       }
                            tel; 
			    avar <- x;
		         } 
		      tel 
		      else
                  if char = "j" then avar <- (new A)
		      else
                  if char = "q" then flag <- FALSE
		      else
                      avar <- (new A).method1(avar.value())
                  fi fi fi fi fi fi fi fi fi fi;
            }
         pool;
       }
   };

};

