.data
space: .asciiz " "
Main.n : .word 0
Main.m : .word 0
.text
main:
move $fp, $sp


j CLASS.Main

#-----------------------------------block id: 140580232834656

jal exit_func

#-----------------------------------block id: 140580232832568
CLASS.Main:

lw $t5,Main.n
li $t5, 4

lw $s6,Main.m
li $s6, 1

sw $t5, Main.n
sw $s6, Main.m

move $fp, $sp
addiu $sp, $sp, -8
jal Main.main

#-----------------------------------block id: 140580232832640

jal exit_func

#-----------------------------------block id: 140580232831128
Main.fact:

lw $t5, -4($fp)
lw $t7, 0($fp)
sw $t7, -4($fp)
move $t5, $t7

lw $s6, -8($fp)
lw $t7, 4($fp)
sw $t7, -8($fp)
move $s6, $t7

lw $s5, -12($fp)
add $s5, $t5, $s6

lw $s4, -16($fp)
sub $t7, $zero, $s5
addi $s4, $t7, 3

li $t7,0
sw $s6, -8($fp)
sw $s5, -12($fp)
sw $s4, -16($fp)
sw $t5, -4($fp)

bgt $s4,$t7,label.1

#-----------------------------------block id: 140580232831200
lw $t5, -4($fp)
lw $s6, -8($fp)
lw $s5, -24($fp)
add $s5, $t5, $s6

lw $s4, -28($fp)
addi $s4, $t5, -1

addiu $sp, $sp, -4
sw $ra, ($sp)
addiu $sp, $sp, -4
sw $fp, ($sp)

addiu $sp, $sp, -4
sw $s4, ($sp)

addiu $sp, $sp, -4
sw $s6, ($sp)

sw $s6, -8($fp)
sw $s5, -24($fp)
sw $t5, -4($fp)
sw $s4, -28($fp)

move $fp, $sp
addiu $sp, $sp, -36
jal Main.fact

#-----------------------------------block id: 140580232827320
lw $t5, -32($fp)
lw $fp, ($sp)
addiu $sp, $sp, 4
lw $ra, ($sp)
addiu $sp, $sp, 4
move $t5, $v0

lw $s6, -24($fp)
lw $s5, -36($fp)
mult $s6, $t5
mflo $s5

sw $s6, -24($fp)
sw $t5, -32($fp)
sw $s5, -36($fp)

move $v0, $s5

#-----------------------------------block id: 140580232827392

j label.2

#-----------------------------------block id: 140580232829480
label.1:

lw $t5, -4($fp)
lw $s6, -8($fp)
lw $s5, -20($fp)
add $s5, $t5, $s6

sw $s6, -8($fp)
sw $s5, -20($fp)
sw $t5, -4($fp)

move $v0, $s5

#-----------------------------------block id: 140580232829552
label.2:

addiu $sp, $sp, 4

addiu $sp, $sp, 4

addiu $sp, $sp, 36

jr $ra

#-----------------------------------block id: 140580232827032
Main.main:


#-----------------------------------block id: 140580232827104
LET_BEGIN_Main.main.LET_1:

addiu $sp, $sp, -4
sw $ra, ($sp)
addiu $sp, $sp, -4
sw $fp, ($sp)

lw $t5, Main.n
addiu $sp, $sp, -4
sw $t5, ($sp)

lw $s6, Main.m
addiu $sp, $sp, -4
sw $s6, ($sp)

sw $t5, Main.n
sw $s6, Main.m

move $fp, $sp
addiu $sp, $sp, -36
jal Main.fact

#-----------------------------------block id: 140580232828472
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

sw $s6, -8($fp)
sw $t5, -4($fp)

#-----------------------------------block id: 140580232828544
LET_OVER_LET_1:

addiu $sp, $sp, 8

jr $ra

#-----------------------------------block id: 140580232828904
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
