.data
space: .asciiz " "
Main.n : .word 0
.text
main:
move $fp, $sp


j CLASS.Main

#-----------------------------------block id: 140119141137656

jal exit_func

#-----------------------------------block id: 140119141137728
CLASS.Main:

lw $t5,Main.n
li $t5, 6

sw $t5, Main.n

move $fp, $sp
addiu $sp, $sp, -8
jal Main.main

#-----------------------------------block id: 140119141138872

jal exit_func

#-----------------------------------block id: 140119141138944
Main.fib:

lw $t5, -4($fp)
lw $t7, 0($fp)
sw $t7, -4($fp)
move $t5, $t7

lw $s6, -8($fp)
slti $s6, $t5, 3

li $t7,0
sw $t5, -4($fp)
sw $s6, -8($fp)

bgt $s6,$t7,label.1

#-----------------------------------block id: 140119141136792
lw $t5, -4($fp)
lw $s6, -12($fp)
addi $s6, $t5, -1

addiu $sp, $sp, -4
sw $ra, ($sp)
addiu $sp, $sp, -4
sw $fp, ($sp)

addiu $sp, $sp, -4
sw $s6, ($sp)

sw $t5, -4($fp)
sw $s6, -12($fp)

move $fp, $sp
addiu $sp, $sp, -28
jal Main.fib

#-----------------------------------block id: 140119141136864
lw $t5, -16($fp)
lw $fp, ($sp)
addiu $sp, $sp, 4
lw $ra, ($sp)
addiu $sp, $sp, 4
move $t5, $v0

lw $s6, -4($fp)
lw $s5, -20($fp)
addi $s5, $s6, -2

addiu $sp, $sp, -4
sw $ra, ($sp)
addiu $sp, $sp, -4
sw $fp, ($sp)

addiu $sp, $sp, -4
sw $s5, ($sp)

sw $s6, -4($fp)
sw $s5, -20($fp)
sw $t5, -16($fp)

move $fp, $sp
addiu $sp, $sp, -28
jal Main.fib

#-----------------------------------block id: 140119141135352
lw $t5, -24($fp)
lw $fp, ($sp)
addiu $sp, $sp, 4
lw $ra, ($sp)
addiu $sp, $sp, 4
move $t5, $v0

lw $s6, -16($fp)
lw $s5, -28($fp)
add $s5, $s6, $t5

sw $s5, -28($fp)
sw $t5, -24($fp)
sw $s6, -16($fp)

move $v0, $s5

#-----------------------------------block id: 140119141135424

j label.2

#-----------------------------------block id: 140119141131544
label.1:


li $v0, 1

#-----------------------------------block id: 140119141131616
label.2:

addiu $sp, $sp, 4

addiu $sp, $sp, 28

jr $ra

#-----------------------------------block id: 140119141133704
Main.main:


#-----------------------------------block id: 140119141133776
LET_BEGIN_Main.main.LET_1:

addiu $sp, $sp, -4
sw $ra, ($sp)
addiu $sp, $sp, -4
sw $fp, ($sp)

lw $t5, Main.n
addiu $sp, $sp, -4
sw $t5, ($sp)

sw $t5, Main.n

move $fp, $sp
addiu $sp, $sp, -28
jal Main.fib

#-----------------------------------block id: 140119141131256
lw $t5, -4($fp)
lw $fp, ($sp)
addiu $sp, $sp, 4
lw $ra, ($sp)
addiu $sp, $sp, 4
move $t5, $v0

lw $s6, -8($fp)
move $s6, $t5

move $a0,$s6
jal print_int

sw $t5, -4($fp)
sw $s6, -8($fp)

#-----------------------------------block id: 140119141131328
LET_OVER_LET_1:

addiu $sp, $sp, 8

jr $ra

#-----------------------------------block id: 140119141132696
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
