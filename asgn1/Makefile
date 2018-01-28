all:
	@rm -f bin/table.py
	@rm -f bin/table.pyc
	@cp src/table.py bin/
	@rm -f bin/lexer
	@cp src/lexer.py bin/
	@chmod u+x bin/lexer.py
	@mv bin/lexer.py bin/lexer
	
clean:
	@rm -f bin/lexer bin/table.py bin/table.pyc
