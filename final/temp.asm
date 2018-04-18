.data
space: .asciiz " "
Main.n : .word 0
Main.m : .word 0
.text
main:

j CLASS.Main

#-----------------------------------block id: 140387501453752

jal exit_func

#-----------------------------------block id: 140387501453824
CLASS.Secure:

lw $t5, -20($fp)
li $v0, 9
li $a0, 5
sll $a0, $a0, 2
syscall
move $t5, $v0

sw $t5, -20($fp)

#-----------------------------------block id: 140387501453896
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

lw $s4, -16($fp)
li $t7, 4
sll $t8, $t7, 2
add $t8, $t5,$t8
lw $s4, 0($t8)

li $t7, 0
sll $t7, $t7, 2
add $t8, $s4,$t7
li $t9, 888
sw $t9, 0($t8)

addiu $sp, $sp, 4

addiu $sp, $sp, 4

addiu $sp, $sp, 4

addiu $sp, $sp, 16
sw $s4, -16($fp)
sw $t5, -4($fp)
sw $s6, -8($fp)
sw $s5, -12($fp)

jr $ra

#-----------------------------------block id: 140387501454040
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

#-----------------------------------block id: 140387501453968
addiu $sp, $sp, 4

addiu $sp, $sp, 8

jr $ra

#-----------------------------------block id: 140387501454112
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

#-----------------------------------block id: 140387501503624
addiu $sp, $sp, 4

addiu $sp, $sp, 8

jr $ra

#-----------------------------------block id: 140387501503696
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

#-----------------------------------block id: 140387501503768
lw $t5, -12($fp)
li $v0, 9
li $a0, 4
sll $a0, $a0, 2
syscall
move $t5, $v0

sw $t5, -12($fp)

#-----------------------------------block id: 140387501503840
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
li $t7, 5
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
li $t7, 6
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

#-----------------------------------block id: 140387501503912
Sec_course.woo:

lw $t5, -4($fp)
lw $t7, 0($fp)
sw $t7, -4($fp)
move $t5, $t7

lw $s6, -8($fp)
li $t7, 7
sll $t8, $t7, 2
add $t8, $t5,$t8
lw $s6, 0($t8)

li $t7, 0
sll $t7, $t7, 2
add $t8, $s6,$t7
li $t9, 1
sw $t9, 0($t8)

lw $s5, -12($fp)
li $t7, 7
sll $t8, $t7, 2
add $t8, $t5,$t8
lw $s5, 0($t8)

li $t7, 1
sll $t7, $t7, 2
add $t8, $s5,$t7
li $t9, 2
sw $t9, 0($t8)

addiu $sp, $sp, 4

addiu $sp, $sp, 12
sw $t5, -4($fp)
sw $s6, -8($fp)
sw $s5, -12($fp)

jr $ra

#-----------------------------------block id: 140387501503984
CLASS.Main:

lw $t5,Main.n
li $t5, 4

lw $s6,Main.m
li $s6, 2

sw $t5, Main.n
sw $s6, Main.m

move $fp, $sp
addiu $sp, $sp, -72
jal Main.main

#-----------------------------------block id: 140387501504056

jal exit_func

#-----------------------------------block id: 140387501504128
Main.main:


#-----------------------------------block id: 140387501504200
LET_BEGIN_Main.main.LET_1:

lw $t5, -16($fp)
li $v0, 9
li $a0, 32
sll $a0, $a0, 2
syscall
move $t5, $v0

lw $s6, -20($fp)
li $v0, 9
li $a0, 16
sll $a0, $a0, 2
syscall
move $s6, $v0

li $t7, 7
sll $t7, $t7, 2
add $t8, $t5,$t7
sw $s6, 0($t8)

lw $s5, -24($fp)
li $v0, 9
li $a0, 20
sll $a0, $a0, 2
syscall
move $s5, $v0

li $t7, 4
sll $t7, $t7, 2
add $t8, $t5,$t7
sw $s5, 0($t8)

lw $s4, -12($fp)
move $s4, $t5

lw $s3, -28($fp)
li $v0, 9
li $a0, 40
sll $a0, $a0, 2
syscall
move $s3, $v0

lw $s2, -32($fp)
li $v0, 9
li $a0, 16
sll $a0, $a0, 2
syscall
move $s2, $v0

li $t7, 7
sll $t7, $t7, 2
add $t8, $s3,$t7
sw $s2, 0($t8)

lw $s1, -36($fp)
li $v0, 9
li $a0, 20
sll $a0, $a0, 2
syscall
move $s1, $v0

li $t7, 4
sll $t7, $t7, 2
add $t8, $s3,$t7
sw $s1, 0($t8)

lw $s0, -4($fp)
move $s0, $s3

lw $t2, -40($fp)
li $v0, 9
li $a0, 32
sll $a0, $a0, 2
syscall
move $t2, $v0

lw $t3, -44($fp)
li $v0, 9
li $a0, 16
sll $a0, $a0, 2
syscall
move $t3, $v0

li $t7, 7
sll $t7, $t7, 2
add $t8, $t2,$t7
sw $t3, 0($t8)

lw $t0, -48($fp)
li $v0, 9
li $a0, 20
sll $a0, $a0, 2
syscall
move $t0, $v0

li $t7, 4
sll $t7, $t7, 2
add $t8, $t2,$t7
sw $t0, 0($t8)

lw $t1, -8($fp)
move $t1, $t2

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
sw $s0, ($sp)

sw $s2, -32($fp)
sw $s6, -20($fp)
sw $s5, -24($fp)
sw $t3, -44($fp)
sw $t5, -16($fp)
sw $t1, -8($fp)
sw $t2, -40($fp)
sw $s0, -4($fp)
sw $s4, -12($fp)
sw $t0, -48($fp)
sw $s1, -36($fp)
sw $s3, -28($fp)

move $fp, $sp
addiu $sp, $sp, -16
jal Secure.set

#-----------------------------------block id: 140387501504272
lw $t5, -52($fp)
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

sw $s6, -4($fp)
sw $t5, -52($fp)

move $fp, $sp
addiu $sp, $sp, -12
jal Sec_course.woo

#-----------------------------------block id: 140387501504344
lw $t5, -56($fp)
lw $fp, ($sp)
addiu $sp, $sp, 4
lw $ra, ($sp)
addiu $sp, $sp, 4
move $t5, $v0

lw $s6, -4($fp)
lw $s5, -60($fp)
li $t7, 4
sll $t8, $t7, 2
add $t8, $s6,$t8
lw $s5, 0($t8)

lw $s4, -64($fp)
li $t7, 0
sll $t8, $t7, 2
add $t8, $s5,$t8
lw $s4, 0($t8)

move $t9, $ra
move $a0,$s4
jal print_int
move $ra, $t9

lw $s3, -68($fp)
li $t7, 7
sll $t8, $t7, 2
add $t8, $s6,$t8
lw $s3, 0($t8)

lw $s2, -72($fp)
li $t7, 1
sll $t8, $t7, 2
add $t8, $s3,$t8
lw $s2, 0($t8)

move $t9, $ra
move $a0,$s2
jal print_int
move $ra, $t9

sw $s2, -72($fp)
sw $s6, -4($fp)
sw $s5, -60($fp)
sw $t5, -56($fp)
sw $s3, -68($fp)
sw $s4, -64($fp)

#-----------------------------------block id: 140387501504416
LET_OVER_LET_1:


jal exit_func

#-----------------------------------block id: 140387501504488
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
