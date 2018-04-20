.data
space: .asciiz " "
str.2: .asciiz "g "
str.1: .asciiz "h "
Main.n : .word 0
Main.t.13 : .word 0
Main.arr : .word 0
Main.obj : .word 0
Main.i : .word 0
Main.m : .word 0
Main.j : .word 0
.text
main:

j CLASS.Main

#-----------------------------------block id: 140117499854648

jal exit_func

#-----------------------------------block id: 140117499854432
CLASS.Test:


#-----------------------------------block id: 140117499854504
Test.print2darray:

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
li $t9, 0
sw $t9, 0($t8)

sw $s5, -12($fp)
sw $t5, -4($fp)
sw $s6, -8($fp)

#-----------------------------------block id: 140117499854360
label.4:

lw $t5, -4($fp)
lw $s6, -16($fp)
li $t7, 0
sll $t8, $t7, 2
add $t8, $t5,$t8
lw $s6, 0($t8)

lw $s5, -20($fp)
slti $s5, $s6, 3

li $t7,0
sw $s6, -16($fp)
sw $s5, -20($fp)
sw $t5, -4($fp)

beq $s5,$t7,label.5

#-----------------------------------block id: 140117499854288
move $t9, $ra
la $a0,str.1
jal print_string
move $ra, $t9

lw $t5, -4($fp)
li $t7, 1
sll $t7, $t7, 2
add $t8, $t5,$t7
li $t9, 0
sw $t9, 0($t8)

sw $t5, -4($fp)

#-----------------------------------block id: 140117499854000
label.1:

lw $t5, -4($fp)
lw $s6, -32($fp)
li $t7, 1
sll $t8, $t7, 2
add $t8, $t5,$t8
lw $s6, 0($t8)

lw $s5, -36($fp)
slti $s5, $s6, 3

li $t7,0
sw $s6, -32($fp)
sw $s5, -36($fp)
sw $t5, -4($fp)

beq $s5,$t7,label.2

#-----------------------------------block id: 140117499854072
lw $t5, -4($fp)
lw $s6, -48($fp)
li $t7, 0
sll $t8, $t7, 2
add $t8, $t5,$t8
lw $s6, 0($t8)

lw $s5, -52($fp)
li $t7, 1
sll $t8, $t7, 2
add $t8, $t5,$t8
lw $s5, 0($t8)

lw $t1, -60($fp)
li $t7, 3
mult $s6, $t7
mflo $t1

add $t1, $t1, $s5

lw $s3, -12($fp)
lw $s2, -56($fp)
sll $t7, $t1, 2
add $t8, $s3, $t7
lw $s2, 0($t8)

move $t9, $ra
move $a0,$s2
jal print_int
move $ra, $t9

sw $s3, -12($fp)
sw $s6, -48($fp)
sw $s2, -56($fp)
sw $s5, -52($fp)
sw $t1, -60($fp)
sw $t5, -4($fp)

#-----------------------------------block id: 140117499863984
label.3:

lw $t5, -4($fp)
lw $s6, -40($fp)
li $t7, 1
sll $t8, $t7, 2
add $t8, $t5,$t8
lw $s6, 0($t8)

lw $s5, -44($fp)
addi $s5, $s6, 1

li $t7, 1
sll $t7, $t7, 2
add $t8, $t5,$t7
sw $s5, 0($t8)

sw $s5, -44($fp)
sw $s6, -40($fp)
sw $t5, -4($fp)

j label.1

#-----------------------------------block id: 140117499864056
label.2:


#-----------------------------------block id: 140117499854144
label.6:

lw $t5, -4($fp)
lw $s6, -24($fp)
li $t7, 0
sll $t8, $t7, 2
add $t8, $t5,$t8
lw $s6, 0($t8)

lw $s5, -28($fp)
addi $s5, $s6, 1

li $t7, 0
sll $t7, $t7, 2
add $t8, $t5,$t7
sw $s5, 0($t8)

sw $s5, -28($fp)
sw $s6, -24($fp)
sw $t5, -4($fp)

j label.4

#-----------------------------------block id: 140117499854216
label.5:

addiu $sp, $sp, 4

addiu $sp, $sp, 4

addiu $sp, $sp, 4

addiu $sp, $sp, 60

jr $ra

#-----------------------------------block id: 140117499853712
CLASS.Main:

lw $t5,Main.n
li $t5, 3

lw $s6,Main.t.13
li $t7, 3
mult $t5, $t7
mflo $s6

lw $s5,Main.arr
li $v0, 9
move $a0, $s6
sll $a0, $a0, 2
syscall
move $s5, $v0

lw $t1,Main.m
li $t1, 0

lw $s3,Main.j
li $s3, 0

sw $t1, Main.m
sw $t5, Main.n
sw $s3, Main.j
sw $s6, Main.t.13
sw $s5, Main.arr

move $fp, $sp
addiu $sp, $sp, -32
jal Main.main

#-----------------------------------block id: 140117499853784

jal exit_func

#-----------------------------------block id: 140117499853568
Main.main:

lw $t5,Main.i
li $t5, 0

sw $t5, Main.i

#-----------------------------------block id: 140117499853640
label.10:

lw $t5, Main.i
lw $s6, Main.n
lw $s5, -4($fp)
slt $s5, $t5, $s6

li $t7,0
sw $s6, Main.n
sw $t5, Main.i
sw $s5, -4($fp)

beq $s5,$t7,label.11

#-----------------------------------block id: 140117499853280
lw $t5,Main.j
li $t5, 0

sw $t5, Main.j

#-----------------------------------block id: 140117499853352
label.7:

lw $t5, Main.j
lw $s6, -12($fp)
slti $s6, $t5, 3

li $t7,0
sw $t5, Main.j
sw $s6, -12($fp)

beq $s6,$t7,label.8

#-----------------------------------block id: 140117499853136
lw $t5, Main.i
lw $s6, -20($fp)
li $t7, 3
mult $t5, $t7
mflo $s6

lw $s5, Main.j
add $s6, $s6, $s5

lw $t1, Main.m
lw $s3,Main.arr
sll $t7, $s6, 2
add $t8, $s3, $t7
sw $t1, 0($t8)

lw $s2, -24($fp)
addi $s2, $t1, 1

move $t1, $s2

move $t9, $ra
la $a0,str.2
jal print_string
move $ra, $t9

sw $t1, Main.m
sw $s2, -24($fp)
sw $s5, Main.j
sw $t5, Main.i
sw $s6, -20($fp)
sw $s3, Main.arr

#-----------------------------------block id: 140117499853208
label.9:

lw $t5, Main.j
lw $s6, -16($fp)
addi $s6, $t5, 1

move $t5, $s6

sw $t5, Main.j
sw $s6, -16($fp)

j label.7

#-----------------------------------block id: 140117499851768
label.8:


#-----------------------------------block id: 140117499853064
label.12:

lw $t5, Main.i
lw $s6, -8($fp)
addi $s6, $t5, 1

move $t5, $s6

sw $t5, Main.i
sw $s6, -8($fp)

j label.10

#-----------------------------------block id: 140117499851696
label.11:

lw $t5, -28($fp)
li $v0, 9
li $a0, 8
sll $a0, $a0, 2
syscall
move $t5, $v0

lw $s6,Main.obj
move $s6, $t5

addiu $sp, $sp, -4
sw $ra, ($sp)
addiu $sp, $sp, -4
sw $fp, ($sp)

lw $s5, Main.arr
addiu $sp, $sp, -4
sw $s5, ($sp)

addiu $sp, $sp, -4
li $t7, 3
sw $t7, ($sp)

addiu $sp, $sp, -4
sw $s6, ($sp)

sw $t5, -28($fp)
sw $s6, Main.obj
sw $s5, Main.arr

move $fp, $sp
addiu $sp, $sp, -60
jal Test.print2darray

#-----------------------------------block id: 140117499851624
lw $t5, -32($fp)
lw $fp, ($sp)
addiu $sp, $sp, 4
lw $ra, ($sp)
addiu $sp, $sp, 4
move $t5, $v0

sw $t5, -32($fp)

jal exit_func

#-----------------------------------block id: 140117499851480
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
