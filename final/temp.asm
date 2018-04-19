.data
space: .asciiz " "
str.6: .asciiz "Tushar"
str.4: .asciiz "Goodbye\n"
str.5: .asciiz "popo"
str.2: .asciiz "\ndude\n"
str.3: .asciiz "Hello W\n"
str.1: .asciiz "Hello "
Main.a : .word 0
Main.b : .word 0
Main.t.1 : .word 0
Main.c : .word 0
.text
main:

j CLASS.Main

#-----------------------------------block id: 140242350057880

jal exit_func

#-----------------------------------block id: 140242350057952
CLASS.Do:


#-----------------------------------block id: 140242350058024
Do.hello:

lw $t5, -8($fp)
lw $t7, 0($fp)
sw $t7, -4($fp)
move $t5, $t7

lw $s6, -4($fp)
lw $t7, 4($fp)
sw $t7, -8($fp)
move $s6, $t7

move $t9, $ra
move $a0,$s6
jal print_string
move $ra, $t9

addiu $sp, $sp, 4

addiu $sp, $sp, 4

addiu $sp, $sp, 8
sw $t5, -4($fp)
sw $s6, -8($fp)

jr $ra

#-----------------------------------block id: 140242350058240
Do.greet:

lw $t5, -8($fp)
lw $t7, 0($fp)
sw $t7, -4($fp)
move $t5, $t7

lw $s6, -4($fp)
lw $t7, 4($fp)
sw $t7, -8($fp)
move $s6, $t7

move $t9, $ra
la $a0,str.1
jal print_string
move $ra, $t9

move $t9, $ra
move $a0,$s6
jal print_string
move $ra, $t9

sw $s6, -8($fp)
sw $t5, -4($fp)

la $v0, str.2

#-----------------------------------block id: 140242350058312
addiu $sp, $sp, 4

addiu $sp, $sp, 4

addiu $sp, $sp, 8

jr $ra

#-----------------------------------block id: 140242350058384
CLASS.Main:

lw $t5,Main.a
li $v0, 9
li $a0, 100
sll $a0, $a0, 2
syscall
move $t5, $v0

la $t5, str.3

lw $s6,Main.b
li $v0, 9
li $a0, 100
sll $a0, $a0, 2
syscall
move $s6, $v0

lw $s5,Main.t.1
li $v0, 9
li $a0, 0
sll $a0, $a0, 2
syscall
move $s5, $v0

lw $s4,Main.c
move $s4, $s5

sw $s5, Main.t.1
sw $s4, Main.c
sw $s6, Main.b
sw $t5, Main.a

move $fp, $sp
addiu $sp, $sp, -8
jal Main.main

#-----------------------------------block id: 140242350058456

jal exit_func

#-----------------------------------block id: 140242350058528
Main.main:

lw $t5,Main.a
la $t5, str.4

lw $s6,Main.b
la $s6, str.5

move $t9, $ra
move $a0,$t5
jal print_string
move $ra, $t9

move $t9, $ra
move $a0,$s6
jal print_string
move $ra, $t9

addiu $sp, $sp, -4
sw $ra, ($sp)
addiu $sp, $sp, -4
sw $fp, ($sp)

addiu $sp, $sp, -4
sw $s6, ($sp)

lw $s5, Main.c
addiu $sp, $sp, -4
sw $s5, ($sp)

sw $s5, Main.c
sw $s6, Main.b
sw $t5, Main.a

move $fp, $sp
addiu $sp, $sp, -8
jal Do.hello

#-----------------------------------block id: 140242350058600
lw $t5, -4($fp)
lw $fp, ($sp)
addiu $sp, $sp, 4
lw $ra, ($sp)
addiu $sp, $sp, 4
move $t5, $v0

addiu $sp, $sp, -4
sw $ra, ($sp)
addiu $sp, $sp, -4
sw $fp, ($sp)

addiu $sp, $sp, -4
la $t7, str.6
sw $t7, ($sp)

lw $s6, Main.c
addiu $sp, $sp, -4
sw $s6, ($sp)

sw $t5, -4($fp)
sw $s6, Main.c

move $fp, $sp
addiu $sp, $sp, -8
jal Do.greet

#-----------------------------------block id: 140242350055792
lw $t5, -8($fp)
lw $fp, ($sp)
addiu $sp, $sp, 4
lw $ra, ($sp)
addiu $sp, $sp, 4
move $t5, $v0

lw $s6,Main.a
move $s6, $t5

move $t9, $ra
move $a0,$s6
jal print_string
move $ra, $t9

sw $t5, -8($fp)
sw $s6, Main.a

jal exit_func

#-----------------------------------block id: 140242350055864
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
