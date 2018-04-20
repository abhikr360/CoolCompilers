.data
space: .asciiz " "
Main.n : .word 0
Main.m : .word 0
.text
main:

j CLASS.Main

#-----------------------------------block id: 140399007904328

jal exit_func

#-----------------------------------block id: 140399007904400
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

#-----------------------------------block id: 140399007904472

jal exit_func

#-----------------------------------block id: 140399007904544
Main.fact:

lw $t5, -8($fp)
lw $t7, 0($fp)
sw $t7, -4($fp)
move $t5, $t7

lw $s6, -4($fp)
lw $t7, 4($fp)
sw $t7, -8($fp)
move $s6, $t7

lw $s5, -12($fp)
add $s5, $s6, $t5

lw $t1, -16($fp)
li $t7,3
slt $t1, $s5, $t7

li $t7,0
sw $t5, -4($fp)
sw $s5, -12($fp)
sw $t1, -16($fp)
sw $s6, -8($fp)

bgt $t1,$t7,label.1

#-----------------------------------block id: 140399007904616
lw $t5, -8($fp)
lw $s6, -4($fp)
lw $s5, -24($fp)
add $s5, $t5, $s6

lw $t1, -28($fp)
addi $t1, $t5, -1

addiu $sp, $sp, -4
sw $ra, ($sp)
addiu $sp, $sp, -4
sw $fp, ($sp)

addiu $sp, $sp, -4
sw $t1, ($sp)

addiu $sp, $sp, -4
sw $s6, ($sp)

sw $s6, -4($fp)
sw $s5, -24($fp)
sw $t5, -8($fp)
sw $t1, -28($fp)

move $fp, $sp
addiu $sp, $sp, -36
jal Main.fact

#-----------------------------------block id: 140399007892688
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

#-----------------------------------block id: 140399007892760

j label.2

#-----------------------------------block id: 140399007904832
label.1:

lw $t5, -8($fp)
lw $s6, -4($fp)
lw $s5, -20($fp)
add $s5, $t5, $s6

sw $s6, -4($fp)
sw $s5, -20($fp)
sw $t5, -8($fp)

move $v0, $s5

#-----------------------------------block id: 140399007904904
label.2:

addiu $sp, $sp, 4

addiu $sp, $sp, 4

addiu $sp, $sp, 36

jr $ra

#-----------------------------------block id: 140399007904976
Main.main:


#-----------------------------------block id: 140399007905048
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

#-----------------------------------block id: 140399007905408
lw $t5, -4($fp)
lw $fp, ($sp)
addiu $sp, $sp, 4
lw $ra, ($sp)
addiu $sp, $sp, 4
move $t5, $v0

lw $s6, -8($fp)
move $s6, $t5

move $t9, $ra
move $a0,$s6
jal print_int
move $ra, $t9

sw $s6, -8($fp)
sw $t5, -4($fp)

#-----------------------------------block id: 140399007905480
LET_OVER_LET_1:


jal exit_func

#-----------------------------------block id: 140399007905264
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
print_string:
li $v0,4
syscall
jr $ra
scan_string:
li $v0,8
syscall
jr $ra
file_open:
li $v0, 13
li $a2, 0
syscall
move $t8, $v0
jr $ra
file_read:
li $v0, 14
move $a0, $t8
li $a2, 100
syscall
jr $ra
file_close:
li $v0, 16
move $a0, $t8
syscall
jr $ra
file_write:
li $v0, 15
move $a0, $t8
move $t6, $ra
jal strlen
move $ra, $t6
syscall
jr $ra
strlen:
move $a3, $a1
li $a2, 0
j strlen.test
strlen.loop:
addi $a3, $a3, 1
addi $a2, $a2, 1
strlen.test:
lb $t7, 0($a3)
bnez $t7, strlen.loop
jr $ra
