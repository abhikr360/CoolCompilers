all:
	rm -f bin/irgen 2>/dev/null
	rm -rf bin 2>/dev/null
	mkdir bin/
	cp src/irgen.py bin/
	cp src/lexer.py bin/
	cp src/parsetab.py bin/
	cp src/symtab.py bin/
	cp src/tree.py bin/
	chmod u+x bin/irgen.py
	mv bin/irgen.py bin/irgen
	
clean:
	rm -f bin/*.py
	rm -f bin/irgen
	rm -f bin/*.pyc
	rm -f bin/parser.out
