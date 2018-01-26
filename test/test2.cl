class A {

   -- Let's assume that we don't want A to not inherit from IO.

   io : IO <- new IO;

   out_a() : Object { io.out_string("A: Hello world\n") };

};


class B inherits A {

   -- B does not have to an extra attribute, since it inherits io from A.

   out_b() : Object { io.out_string("B: Hello world\n") };

};


class C inherits IO {

   -- Now the IO methods are part of C.

   out_c() : Object { out_string("C: Hello world\n") };

   -- Note that out_string(...) is just a shorthand for self.out_string(...)

};


class D inherits C {

   -- Inherits IO methods from C.

   out_d() : Object { out_string("D: Hello world\n") };

};


class Main inherits IO {

   -- Same case as class C.

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
