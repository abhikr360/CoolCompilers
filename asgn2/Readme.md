### To run ###
bin/codegen test/test-3ac.csv test/test-sym.csv

Above command will make temp.asm assembly file

To run the above assembly file on spim

spim -file temp.asm

### Other Instructions ###
Variable name in TAC cannot be a keyword in MIPS. For eg. j,jal,b

Main function should not have FUNC_RETURN
For arrays, dataType in TAC should be Array but the EntryType in our code will be Variable
We also support recursive function calls

### Library Functions ###
PRINT_INT can print an integer variable, array[i], a number
SCAN_INT can scan into an integer variable, array[i]
EXIT for exiting
SPACE for printing space

### EFFORT SHEET ###

All of us consent to the following effort distribution for our group for asgn2:

Abhishek Kumar 150035 34%
Madhukant      150368 33%
Tushar Gupta   150771 33%

+ ASSIGN,var,12 ```var = 12```
+ ADD|SUB|MUL|DIV a,b,c ```a = b +|-|*|/ c```  b,c can be variable as well as integer
+ GOTO L ```goto label L```
+ IFGOTO,LESS_THAN_EQUALS | LESS_THAN | EQUALS | NOT_EQUALS | GREATER_THAN | GREATER_THAN_EQUALS ,a,10,L ```goto label L if a cond_op 10```
+ INDEX_ASSIGN_L,arr,index,val  ```arr[index] = value```
+ INDEX_ASSIGN_R,dest,arr,index   ```dest = arr[index]```
+ FUNC_CALL,foo ```call function foo```
+ FUNC_RETURN ```return from current function```
+ LABEL,L ```mark this line as label L```
+ FUNC_LABEL,foo ```label for function foo()```

### Library Functions ###

+ SCAN_INT,dest ```scanf("%d",dest)```
+ PRINT_INT,src ```printf("%d",src)```
+ EXIT ```exit()```
+ SPACE ```printf(" ")```
