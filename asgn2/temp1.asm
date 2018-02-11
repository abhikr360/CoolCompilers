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
lw $t5,t1
li $t5, 1

lw $s6,t2
li $s6, 1

lw $s5,t3
li $t7, 2
mult $s6, $t7
mflo $s5

lw $s4,t4
add $s4, $t5, $s5

lw $s3,t5
li $s3, 4

lw $s2,t6
add $s2, $s4, $s3

lw $s1,X
move $s1, $s2

sw $s2, t6
sw $s4, t4
sw $s3, t5
sw $s6, t2
sw $s5, t3
sw $t5, t1
sw $s1, X

#-----------------------------------block id: 139661853219512
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
