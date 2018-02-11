### To run ###
bin/codegen test/test-3ac.csv test/test-sym.csv

Above command will make temp.asm assembly file

To run the above assembly file on spim

spim -file temp.asm

### Other Instructions ###
Variable name in TAC cannot be a keyword in MIPS. For eg. j,jal,b

Main function should not have FUNC_RETURN
For arrays, dataType in TAC should be Array but the EntryType in our code will be Variable

### Library Functions ###
PRINT_INT can print an integer variable, array[i], a number
SCAN_INT can scan into an integer variable, array[i]
EXIT for exiting
SPACE for printing space


