.data
space: .asciiz " "
SELF : .word 0
.text
main:
move $fp, $sp


j CLASS.Main

#-----------------------------------block id: 140232733142696

jal exit_func

#-----------------------------------block id: 140232733142192
CLASS.WHATSUP:


move $fp, $sp
addiu $sp, $sp, -16
jal Main.main

#-----------------------------------block id: 140232733142264

jal exit_func

#-----------------------------------block id: 140232733129760
WHATSUP.printme:

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

lw $s4, -16($fp)
li $t7, 1
sll $t8, $t7, 2
add $t8, $t5,$t8
lw $s4, 0($t8)

lw $s3, -20($fp)
add $s3, $s4, $s6

move $a0,$s3
jal print_int

lw $s2, -24($fp)
li $t7, 0
sll $t8, $t7, 2
add $t8, $t5,$t8
lw $s2, 0($t8)

move $a0,$s2
jal print_int

addiu $sp, $sp, 4

addiu $sp, $sp, 4

addiu $sp, $sp, 4

addiu $sp, $sp, 4

addiu $sp, $sp, 24
sw $s4, -16($fp)
sw $s2, -24($fp)
sw $s6, -8($fp)
sw $s5, -4($fp)
sw $s3, -20($fp)
sw $t5, -12($fp)

jr $ra

#-----------------------------------block id: 140232733129832
CLASS.Fibonacci:


#-----------------------------------block id: 140232733142912
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
sw $s6, -4($fp)
sw $s5, -12($fp)
sw $t5, -8($fp)

bgt $s5,$t7,label.1

#-----------------------------------block id: 140232733142984
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

sw $t5, -4($fp)
sw $s6, -16($fp)
sw $s5, -8($fp)

move $fp, $sp
addiu $sp, $sp, -32
jal Fibonacci.fibonacci

#-----------------------------------block id: 140232733139168
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

sw $s6, -4($fp)
sw $s4, -8($fp)
sw $t5, -20($fp)
sw $s5, -24($fp)

move $fp, $sp
addiu $sp, $sp, -32
jal Fibonacci.fibonacci

#-----------------------------------block id: 140232733146432
lw $t5, -28($fp)
lw $fp, ($sp)
addiu $sp, $sp, 4
lw $ra, ($sp)
addiu $sp, $sp, 4
move $t5, $v0

lw $s6, -20($fp)
lw $s5, -32($fp)
add $s5, $s6, $t5

sw $s5, -32($fp)
sw $t5, -28($fp)
sw $s6, -20($fp)

move $v0, $s5

#-----------------------------------block id: 140232733146504

j label.2

#-----------------------------------block id: 140232733139240
label.1:

lw $t5, -4($fp)
sw $t5, -4($fp)

move $v0, $t5

#-----------------------------------block id: 140232733139024
label.2:

addiu $sp, $sp, 4

addiu $sp, $sp, 4

addiu $sp, $sp, 4

addiu $sp, $sp, 32

jr $ra

#-----------------------------------block id: 140232733139096
CLASS.Main:


#-----------------------------------block id: 140232733130624
Main.main:


#-----------------------------------block id: 140232733130696
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

sw $s5, -8($fp)
sw $t5, -12($fp)
sw $s6, -4($fp)

move $fp, $sp
addiu $sp, $sp, -32
jal Fibonacci.fibonacci

#-----------------------------------block id: 140232733130336
lw $t5, -16($fp)
lw $fp, ($sp)
addiu $sp, $sp, 4
lw $ra, ($sp)
addiu $sp, $sp, 4
move $t5, $v0

move $a0,$t5
jal print_int

sw $t5, -16($fp)

#-----------------------------------block id: 140232733130408
LET_OVER_LET_1:

addiu $sp, $sp, 16

jr $ra

#-----------------------------------block id: 140232733143984
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
