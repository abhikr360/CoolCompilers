#*******************givenrehister for ans t5 
#*******************givenrehister for factorial.n t5 
#*******************givenrehister for factorial.n t5 
.data
space: .asciiz " "
n : .word 0
ans : .word 0
factorial.temp : .word 0
factorial.n : .word 0
factorial.res : .word 0
.text
main:
move $fp, $sp
lw $t5,n
li $t5, 3

addiu $sp, $sp, -4
sw $ra, ($sp)
addiu $sp, $sp, -4
sw $fp, ($sp)

addiu $sp, $sp, -4
lw $t5, ($sp)

jal factorial

lw $ra, ($sp)
addiu $sp, $sp, 4
lw $fp, ($sp)
sw $t5, 0($fp)

addiu $sp, $sp, 4

#-----------------------------------block id: 140290846585200
lw $t5, ans
move $a0,$t5
jal print_int

sw $t5, 4($fp)

jal exit_func

#-----------------------------------block id: 140290846585416
factorial:

lw $t5,factorial.n
lw $t5, ($sp)
addiu $sp, $sp, 4

li $t7,1
sw $t5, 0($fp)

ble $t5,$t7,base

#-----------------------------------block id: 140290846585488
lw $t5, factorial.n
lw $s6,factorial.temp
addi $s6, $t5, -1

addiu $sp, $sp, -4
sw $ra, ($sp)
addiu $sp, $sp, -4
sw $fp, ($sp)

addiu $sp, $sp, -4
lw $s6, ($sp)

jal factorial
lw $ra, ($sp)
addiu $sp, $sp, 4
lw $fp, ($sp)
sw $t5, 0($fp)
sw $s6, 4($fp)

addiu $sp, $sp, 4

#-----------------------------------block id: 140290846585632
lw $t5, factorial.n
lw $s6, factorial.temp
lw $s5,factorial.res
mult $t5, $s6
mflo $s5

move $v0, $s6
lw $ra, ($sp)
add $sp, $sp, 4
sw $s5, 8($fp)
sw $t5, 0($fp)
sw $s6, 4($fp)

jr $ra

#-----------------------------------block id: 140290846585560
base:

li $v0, 0
lw $ra, ($sp)
add $sp, $sp, 4

jr $ra

#-----------------------------------block id: 140290846585704
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
space_func:
la $a0, space
li $v0, 4
syscall
jr $ra

