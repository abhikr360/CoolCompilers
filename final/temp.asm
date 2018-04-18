.data
space: .asciiz " "
Main.n : .word 0
Main.m : .word 0
.text
main:

j CLASS.Main

#-----------------------------------block id: 139766607880064

jal exit_func

#-----------------------------------block id: 139766607880136
CLASS.Secure:


#-----------------------------------block id: 139766607913040
Secure.set:

lw $t5, -12($fp)
lw $t7, 0($fp)
sw $t7, -4($fp)
move $t5, $t7

lw $s6, -8($fp)
lw $t7, 4($fp)
sw $t7, -8($fp)
move $s6, $t7

lw $s5, -4($fp)
lw $t7, 8($fp)
sw $t7, -12($fp)
move $s5, $t7

li $t7, 0
sll $t7, $t7, 2
add $t8, $t5,$t7
sw $s5, 0($t8)

li $t7, 1
sll $t7, $t7, 2
add $t8, $t5,$t7
sw $s6, 0($t8)

addiu $sp, $sp, 4

addiu $sp, $sp, 4

addiu $sp, $sp, 4

addiu $sp, $sp, 12
sw $t5, -4($fp)
sw $s5, -12($fp)
sw $s6, -8($fp)

jr $ra

#-----------------------------------block id: 139766607913184
Secure.get_aa:

lw $t5, -4($fp)
lw $t7, 0($fp)
sw $t7, -4($fp)
move $t5, $t7

lw $s6, -8($fp)
li $t7, 0
sll $t8, $t7, 2
add $t8, $t5,$t8
lw $s6, 0($t8)

sw $s6, -8($fp)
sw $t5, -4($fp)

move $v0, $s6

#-----------------------------------block id: 139766607913112
addiu $sp, $sp, 4

addiu $sp, $sp, 8

jr $ra

#-----------------------------------block id: 139766607913256
Secure.get_bb:

lw $t5, -4($fp)
lw $t7, 0($fp)
sw $t7, -4($fp)
move $t5, $t7

lw $s6, -8($fp)
li $t7, 1
sll $t8, $t7, 2
add $t8, $t5,$t8
lw $s6, 0($t8)

sw $s6, -8($fp)
sw $t5, -4($fp)

move $v0, $s6

#-----------------------------------block id: 139766607935968
addiu $sp, $sp, 4

addiu $sp, $sp, 8

jr $ra

#-----------------------------------block id: 139766607936040
Secure.printdata:

lw $t5, -4($fp)
lw $t7, 0($fp)
sw $t7, -4($fp)
move $t5, $t7

lw $s6, -8($fp)
li $t7, 0
sll $t8, $t7, 2
add $t8, $t5,$t8
lw $s6, 0($t8)

move $t9, $ra
move $a0,$s6
jal print_int
move $ra, $t9

move $t9,$ra
jal space_func
move $ra,$t9

lw $s5, -12($fp)
li $t7, 1
sll $t8, $t7, 2
add $t8, $t5,$t8
lw $s5, 0($t8)

move $t9, $ra
move $a0,$s5
jal print_int
move $ra, $t9

move $t9,$ra
jal space_func
move $ra,$t9

lw $s4, -16($fp)
li $t7, 2
sll $t8, $t7, 2
add $t8, $t5,$t8
lw $s4, 0($t8)

move $t9, $ra
move $a0,$s4
jal print_int
move $ra, $t9

move $t9,$ra
jal space_func
move $ra,$t9

lw $s3, -20($fp)
li $t7, 3
sll $t8, $t7, 2
add $t8, $t5,$t8
lw $s3, 0($t8)

move $t9, $ra
move $a0,$s3
jal print_int
move $ra, $t9

move $t9,$ra
jal space_func
move $ra,$t9

addiu $sp, $sp, 4

addiu $sp, $sp, 20
sw $s6, -8($fp)
sw $s5, -12($fp)
sw $s4, -16($fp)
sw $s3, -20($fp)
sw $t5, -4($fp)

jr $ra

#-----------------------------------block id: 139766607936112
Shukla.printdata:

lw $t5, -4($fp)
lw $t7, 0($fp)
sw $t7, -4($fp)
move $t5, $t7

move $t9,$ra
jal space_func
move $ra,$t9

lw $s6, -8($fp)
li $t7, 1
sll $t8, $t7, 2
add $t8, $t5,$t8
lw $s6, 0($t8)

move $t9, $ra
move $a0,$s6
jal print_int
move $ra, $t9

move $t9,$ra
jal space_func
move $ra,$t9

move $t9,$ra
jal space_func
move $ra,$t9

lw $s5, -12($fp)
li $t7, 3
sll $t8, $t7, 2
add $t8, $t5,$t8
lw $s5, 0($t8)

move $t9, $ra
move $a0,$s5
jal print_int
move $ra, $t9

move $t9,$ra
jal space_func
move $ra,$t9

lw $s4, -16($fp)
li $t7, 4
sll $t8, $t7, 2
add $t8, $t5,$t8
lw $s4, 0($t8)

lw $s3, -20($fp)
addi $s3, $s4, 1

move $t9, $ra
move $a0,$s3
jal print_int
move $ra, $t9

move $t9,$ra
jal space_func
move $ra,$t9

lw $s2, -24($fp)
li $t7, 5
sll $t8, $t7, 2
add $t8, $t5,$t8
lw $s2, 0($t8)

lw $s1, -28($fp)
addi $s1, $s2, 2

move $t9, $ra
move $a0,$s1
jal print_int
move $ra, $t9

move $t9,$ra
jal space_func
move $ra,$t9

addiu $sp, $sp, 4

addiu $sp, $sp, 28
sw $t5, -4($fp)
sw $s1, -28($fp)
sw $s2, -24($fp)
sw $s3, -20($fp)
sw $s4, -16($fp)
sw $s5, -12($fp)
sw $s6, -8($fp)

jr $ra

#-----------------------------------block id: 139766607936184
CLASS.Main:

lw $t5,Main.n
li $t5, 4

lw $s6,Main.m
li $s6, 2

sw $t5, Main.n
sw $s6, Main.m

move $fp, $sp
addiu $sp, $sp, -32
jal Main.main

#-----------------------------------block id: 139766607936256

jal exit_func

#-----------------------------------block id: 139766607936328
Main.main:


#-----------------------------------block id: 139766607936400
LET_BEGIN_Main.main.LET_1:

lw $t5, -16($fp)
li $v0, 9
li $a0, 24
sll $a0, $a0, 2
syscall
move $t5, $v0

lw $s6, -12($fp)
move $s6, $t5

lw $s5, -20($fp)
li $v0, 9
li $a0, 32
sll $a0, $a0, 2
syscall
move $s5, $v0

lw $s4, -4($fp)
move $s4, $s5

lw $s3, -24($fp)
li $v0, 9
li $a0, 24
sll $a0, $a0, 2
syscall
move $s3, $v0

lw $s2, -8($fp)
move $s2, $s3

addiu $sp, $sp, -4
sw $ra, ($sp)
addiu $sp, $sp, -4
sw $fp, ($sp)

addiu $sp, $sp, -4
li $t7, 4
sw $t7, ($sp)

addiu $sp, $sp, -4
li $t7, 5
sw $t7, ($sp)

addiu $sp, $sp, -4
sw $s4, ($sp)

sw $s5, -20($fp)
sw $t5, -16($fp)
sw $s3, -24($fp)
sw $s2, -8($fp)
sw $s4, -4($fp)
sw $s6, -12($fp)

move $fp, $sp
addiu $sp, $sp, -12
jal Secure.set

#-----------------------------------block id: 139766607936472
lw $t5, -28($fp)
lw $fp, ($sp)
addiu $sp, $sp, 4
lw $ra, ($sp)
addiu $sp, $sp, 4
move $t5, $v0

addiu $sp, $sp, -4
sw $ra, ($sp)
addiu $sp, $sp, -4
sw $fp, ($sp)

lw $s6, -4($fp)
addiu $sp, $sp, -4
sw $s6, ($sp)

sw $t5, -28($fp)
sw $s6, -4($fp)

move $fp, $sp
addiu $sp, $sp, -28
jal Shukla.printdata

#-----------------------------------block id: 139766607936544
lw $t5, -32($fp)
lw $fp, ($sp)
addiu $sp, $sp, 4
lw $ra, ($sp)
addiu $sp, $sp, 4
move $t5, $v0

sw $t5, -32($fp)

#-----------------------------------block id: 139766607936616
LET_OVER_LET_1:


jal exit_func

#-----------------------------------block id: 139766607936688
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
