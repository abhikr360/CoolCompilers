.data
space: .asciiz " "
.text
main:

j CLASS.Main

#-----------------------------------block id: 140457382234808

jal exit_func

#-----------------------------------block id: 140457382234880
CLASS.Fibonacci:


#-----------------------------------block id: 140457382234952
Fibonacci.fibonacci:

lw $t5, -8($fp)
lw $t7, 0($fp)
sw $t7, -4($fp)
move $t5, $t7

lw $s6, -4($fp)
lw $t7, 4($fp)
sw $t7, -8($fp)
move $s6, $t7

lw $s5, -12($fp)
slti $s5, $s6, 3

li $t7,0
sw $s5, -12($fp)
sw $t5, -8($fp)
sw $s6, -4($fp)

bgt $s5,$t7,label.1

#-----------------------------------block id: 140457382235024
lw $t5, -4($fp)
lw $s6, -16($fp)
addi $s6, $t5, -1

addiu $sp, $sp, -4
sw $ra, ($sp)
addiu $sp, $sp, -4
sw $fp, ($sp)

addiu $sp, $sp, -4
sw $s6, ($sp)

lw $s5, -8($fp)
addiu $sp, $sp, -4
sw $s5, ($sp)

sw $s6, -16($fp)
sw $s5, -8($fp)
sw $t5, -4($fp)

move $fp, $sp
addiu $sp, $sp, -32
jal Fibonacci.fibonacci

#-----------------------------------block id: 140457382235096
lw $t5, -20($fp)
lw $fp, ($sp)
addiu $sp, $sp, 4
lw $ra, ($sp)
addiu $sp, $sp, 4
move $t5, $v0

lw $s6, -4($fp)
lw $s5, -24($fp)
addi $s5, $s6, -2

addiu $sp, $sp, -4
sw $ra, ($sp)
addiu $sp, $sp, -4
sw $fp, ($sp)

addiu $sp, $sp, -4
sw $s5, ($sp)

lw $s4, -8($fp)
addiu $sp, $sp, -4
sw $s4, ($sp)

sw $t5, -20($fp)
sw $s5, -24($fp)
sw $s4, -8($fp)
sw $s6, -4($fp)

move $fp, $sp
addiu $sp, $sp, -32
jal Fibonacci.fibonacci

#-----------------------------------block id: 140457382235168
lw $t5, -28($fp)
lw $fp, ($sp)
addiu $sp, $sp, 4
lw $ra, ($sp)
addiu $sp, $sp, 4
move $t5, $v0

lw $s6, -20($fp)
lw $s5, -32($fp)
add $s5, $s6, $t5

sw $s6, -20($fp)
sw $t5, -28($fp)
sw $s5, -32($fp)

move $v0, $s5

#-----------------------------------block id: 140457382232360

j label.2

#-----------------------------------block id: 140457382232432
label.1:

lw $t5, -4($fp)
sw $t5, -4($fp)

move $v0, $t5

#-----------------------------------block id: 140457382235384
label.2:

addiu $sp, $sp, 4

addiu $sp, $sp, 4

addiu $sp, $sp, 32

jr $ra

#-----------------------------------block id: 140457382235456
CLASS.Main:

addiu $sp, $sp, -4
sw $ra, ($sp)
addiu $sp, $sp, -4
sw $fp, ($sp)


move $fp, $sp
addiu $sp, $sp, -16
jal Main.main

#-----------------------------------block id: 140457382235816

jal exit_func

#-----------------------------------block id: 140457382235888
Main.main:


#-----------------------------------block id: 140457382235672
LET_BEGIN_Main.main.LET_1:

lw $t5, -12($fp)
li $v0, 9
li $a0, 0
sll $a0, $a0, 2
syscall
move $t5, $v0

lw $s6, -4($fp)
move $s6, $t5

lw $s5, -8($fp)
li $s5, 3

addiu $sp, $sp, -4
sw $ra, ($sp)
addiu $sp, $sp, -4
sw $fp, ($sp)

addiu $sp, $sp, -4
sw $s5, ($sp)

addiu $sp, $sp, -4
sw $s6, ($sp)

sw $s6, -4($fp)
sw $t5, -12($fp)
sw $s5, -8($fp)

move $fp, $sp
addiu $sp, $sp, -32
jal Fibonacci.fibonacci

#-----------------------------------block id: 140457382235744
lw $t5, -16($fp)
lw $fp, ($sp)
addiu $sp, $sp, 4
lw $ra, ($sp)
addiu $sp, $sp, 4
move $t5, $v0

move $a0,$t5
jal print_int

sw $t5, -16($fp)

#-----------------------------------block id: 140457382235240
LET_OVER_LET_1:


jal exit_func

#-----------------------------------block id: 140457382235312
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
