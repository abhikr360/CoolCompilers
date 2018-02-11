.data

t1 : .word 0
t2 : .word 0
t3 : .word 0
t4 : .word 0
t5 : .word 0
t6 : .word 0
X : .word 0
.text
main:
lw $t2,t1
li $t2, 1

lw $t0,t2
li $t0, 1

lw $t1,t3
li $t7, 2
mult $t0, $t7
mflo $t1

sw $t0, t2
lw $t0,t4
add $t0, $t2, $t1

sw $t2, t1
lw $t2,t5
li $t2, 4

sw $t1, t3
lw $t1,t6
add $t1, $t0, $t2

sw $t0, t4
lw $t0,X
move $t0, $t1

sw $t1, t6
sw $t2, t5
sw $t0, X

#-----------------------------------block id: 140701288864440
exit_func:
li $v0,10
syscall
print_int:
li $v0,1
syscall
jr $ra
scan_int:
li $v0,5
syscall
jr $ra
