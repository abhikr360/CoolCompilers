.data
space: .asciiz " "
Main.n : .word 0
.text
main:
move $fp, $sp


j CLASS.Main

#-----------------------------------block id: 139641432805248

jal exit_func

#-----------------------------------block id: 139641432805320
CLASS.Main:

lw $t5,Main.n
li $t5, 1

sw $t5, Main.n

j Main.main

#-----------------------------------block id: 139641432804672
Main.fact:

lw $t5, -4($fp)
lw $t7, 0($fp)
sw $t7, -4($fp)

lw $s6, -8($fp)
sub $t7, $zero, $t5
addi $s6, $t7, 3

li $t7,0
sw $s6, -8($fp)
sw $t5, -4($fp)

bgt $s6,$t7,label.1

#-----------------------------------block id: 139641432804744
lw $t5, -4($fp)
lw $s6, -12($fp)
addi $s6, $t5, -1

addiu $sp, $sp, -4
sw $ra, ($sp)
addiu $sp, $sp, -4
sw $fp, ($sp)

addiu $sp, $sp, -4
sw $s6, ($sp)

lw $s5, -16($fp)
move $fp, $sp
addiu $sp, $sp, -20
jal Main.fact
lw $ra, ($sp)
addiu $sp, $sp, 4
lw $fp, ($sp)
addiu $sp, $sp, 4
sw $s6, -12($fp)
sw $s5, -16($fp)
sw $t5, -4($fp)

move $s5, $v0

#-----------------------------------block id: 139641432805888
lw $t5, -4($fp)
lw $s6, -16($fp)
lw $s5, -20($fp)
mult $t5, $s6
mflo $s5

sw $s6, -16($fp)
sw $s5, -20($fp)
sw $t5, -4($fp)

move $v0, $s5

#-----------------------------------block id: 139641432805960

j label.2

#-----------------------------------block id: 139641432803808
label.1:

lw $t5, -4($fp)
sw $t5, -4($fp)

move $v0, $t5

#-----------------------------------block id: 139641432803880
label.2:

addiu $sp, $sp, 4

lw $ra, ($sp)
add $sp, $sp, 4

jr $ra

#-----------------------------------block id: 139641432802368
Main.main:


#-----------------------------------block id: 139641432802440
LET_BEGIN_Main.main.LET_1:

addiu $sp, $sp, -4
sw $ra, ($sp)
addiu $sp, $sp, -4
sw $fp, ($sp)

lw $t5, Main.n
addiu $sp, $sp, -4
sw $t5, ($sp)

lw $s6, -4($fp)
move $fp, $sp
addiu $sp, $sp, -20
jal Main.fact
lw $ra, ($sp)
addiu $sp, $sp, 4
lw $fp, ($sp)
addiu $sp, $sp, 4
sw $t5, Main.n
sw $s6, -4($fp)

move $s6, $v0

#-----------------------------------block id: 139641432798560
lw $t5, -4($fp)
lw $s6, -8($fp)
move $s6, $t5

move $a0,$s6
jal print_int

sw $s6, -8($fp)
sw $t5, -4($fp)

#-----------------------------------block id: 139641432798632
LET_OVER_LET_1:

lw $ra, ($sp)
add $sp, $sp, 4

jr $ra

#-----------------------------------block id: 139641432800720
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
