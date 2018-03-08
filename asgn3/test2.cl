class A {


   io : IO <- new IO;

   out_a() : Object { io.out_string("A: Hello world\n") };

};


class B inherits A {


   out_b() : Object { io.out_string("B: Hello world\n") };

};


class C inherits IO {


   out_c() : Object { out_string("C: Hello world\n") };


};


class D inherits C {


   out_d() : Object { out_string("D: Hello world\n") };

};


class Main inherits IO {


   main() : Object {
      {
	 (new A).out_a();
	 (new B).out_b();
	 (new C).out_c();
	 (new D).out_d();
	 out_string("Done.\n");
      }
   };

};
