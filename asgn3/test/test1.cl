import me;
import mu;
class Main {
   main(): SELF_TYPE {
   	out_string("Hello World!\n")
   };
};

class BookList inherits IO { 
    isNil() : Bool { { abort(); true; } };
    
    cons(hd : Book) : Cons {
        (let new_cell : Cons <- new Cons in
            new_cell.init(hd,self)
        tel)
    };

    car() : Book { { abort(); new Book; } };

    cdr() : BookList { { abort(); new BookList; } };
    
    print_list() : Object { abort() };
};

class Main inherits IO{

	a : Int <- 5 + 9 % 5;
	b : Bool <- TRUE;
	c : Int <- new Int;



   main(): SELF_TYPE {
   	{
   		out_string("Hello World!\n");
   		a <-  5+ 5 + 5 +a;
   		b <- ar[5];
   		(*cp[2] <- 12*)
   		c <- foo(a, b,c);
   		d <- main.f();
   		e.fun(c,d,s);

   		if (a < 0) then 
   			{
   				a <- 0;
   				b <- 0;
   			} 
   		else 
   		{
   			if (kumar = "brilliant") then
   				all <- TRUE
   			else
   			{
   				all <- FALSE;
   				kumar <- "randi";
   			}
   			fi;
   			c <- b;
   		}
   		fi;

   		while(not(kumar = "brilliant")) loop
   		{
   			confirm();
   			while(TRUE) loop
   				str <- "YOU LIAR!!!"
   			pool;
   		}
   		pool;


   		for(i <- 0; i < np; i<- i+1) loop
   			for(j; j<-0; j+1) loop
   				echo("WOW WOW")
   			pool
   		pool;

   		self@Book.print(a,b);
   	}
   };


   (*method2(num1 : Int, num2 : Int) : B {
	  		(let x : Int in
	  		{
		        x <- num1 + num2;
			    d.set_var(x);
			 }
			 )
	   };*)


   public main1(): SELF_TYPE {
   	out_string("Hello World!\n")
   };
   public main2(a : Int, b : String): SELF_TYPE {
   	out_string("Hello World!\n")
   };
   main3(xyz[] : Int): Int {
   	out_string("Hello World!\n")
   };

};
class Main inherits IO{
};
class Main {

    books : BookList;

    main() : Object {
        (let a_book : Book <-
            (new Book).initBook("Compilers, Principles, Techniques, and Tools",
                                "Aho, Sethi, and Ullman")
        in
            (let an_article : Article <-
                (new Article).initArticle("The Top 100 CD_ROMs",
                                          "Ulanoff",
                                          "PC Magazine")
            in
                {
                    books <- (new Nil).cons(a_book).cons(an_article);
                    books.print_list();
                }
            tel
            )
        tel
        )
    };
};