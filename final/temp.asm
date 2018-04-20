.data
space: .asciiz " "
str.1: .asciiz "h "
Main.n : .word 0
Main.t.19 : .word 0
Main.arr : .word 0
Main.arr2 : .word 0
Main.obj : .word 0
Main.i : .word 0
Main.m : .word 0
Main.j : .word 0
.text
main:

j CLASS.Main

#-----------------------------------block id: 140249140334248

jal exit_func

#-----------------------------------block id: 140249140333888
CLASS.Test:


#-----------------------------------block id: 140249140333960
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

#-----------------------------------block id: 140249140333816
label.4:

lw $t5, -4($fp)
lw $s6, -16($fp)
li $t7, 0
sll $t8, $t7, 2
add $t8, $t5,$t8
lw $s6, 0($t8)

lw $s5, -20($fp)
li $t7,3
slt $s5, $s6, $t7

li $t7,0
sw $s6, -16($fp)
sw $s5, -20($fp)
sw $t5, -4($fp)

beq $s5,$t7,label.5

#-----------------------------------block id: 140249140333744
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

#-----------------------------------block id: 140249140332232
label.1:

lw $t5, -4($fp)
lw $s6, -32($fp)
li $t7, 1
sll $t8, $t7, 2
add $t8, $t5,$t8
lw $s6, 0($t8)

lw $s5, -36($fp)
li $t7,3
slt $s5, $s6, $t7

li $t7,0
sw $s6, -32($fp)
sw $s5, -36($fp)
sw $t5, -4($fp)

beq $s5,$t7,label.2

#-----------------------------------block id: 140249140333528
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

#-----------------------------------block id: 140249140332160
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

#-----------------------------------block id: 140249140332088
label.2:


#-----------------------------------block id: 140249140331944
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

#-----------------------------------block id: 140249140332016
label.5:

addiu $sp, $sp, 4

addiu $sp, $sp, 4

addiu $sp, $sp, 4

addiu $sp, $sp, 60

jr $ra

#-----------------------------------block id: 140249140359968
Test.print1darray:

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

li $t7, 1
sll $t7, $t7, 2
add $t8, $t5,$t7
li $t9, 0
sw $t9, 0($t8)

sw $s6, -8($fp)
sw $s5, -12($fp)
sw $t5, -4($fp)

#-----------------------------------block id: 140249140360040
label.7:

lw $t5, -4($fp)
lw $s6, -16($fp)
li $t7, 1
sll $t8, $t7, 2
add $t8, $t5,$t8
lw $s6, 0($t8)

lw $s5, -8($fp)
lw $t1, -20($fp)
slt $t1, $s6, $s5

li $t7,0
sw $t1, -20($fp)
sw $s6, -16($fp)
sw $s5, -8($fp)
sw $t5, -4($fp)

beq $t1,$t7,label.8

#-----------------------------------block id: 140249139615072
lw $t5, -4($fp)
lw $s6, -32($fp)
li $t7, 1
sll $t8, $t7, 2
add $t8, $t5,$t8
lw $s6, 0($t8)

lw $s5, -12($fp)
lw $t1, -36($fp)
sll $t7, $s6, 2
add $t8, $s5, $t7
lw $t1, 0($t8)

move $t9, $ra
move $a0,$t1
jal print_int
move $ra, $t9

sw $s6, -32($fp)
sw $t1, -36($fp)
sw $s5, -12($fp)
sw $t5, -4($fp)

#-----------------------------------block id: 140249139615144
label.9:

lw $t5, -4($fp)
lw $s6, -24($fp)
li $t7, 1
sll $t8, $t7, 2
add $t8, $t5,$t8
lw $s6, 0($t8)

lw $s5, -28($fp)
addi $s5, $s6, 1

li $t7, 1
sll $t7, $t7, 2
add $t8, $t5,$t7
sw $s5, 0($t8)

sw $s5, -28($fp)
sw $s6, -24($fp)
sw $t5, -4($fp)

j label.7

#-----------------------------------block id: 140249139615216
label.8:

addiu $sp, $sp, 4

addiu $sp, $sp, 4

addiu $sp, $sp, 4

addiu $sp, $sp, 36

jr $ra

#-----------------------------------block id: 140249139615288
CLASS.Main:

lw $t5,Main.n
li $t5, 4

lw $s6,Main.t.19
li $t7, 3
mult $t5, $t7
mflo $s6

lw $s5,Main.arr
li $v0, 9
move $a0, $s6
sll $a0, $a0, 2
syscall
move $s5, $v0

lw $t1, Main.arr2
li $v0, 9
move $a0, $t5
sll $a0, $a0, 2
syscall
move $t1, $v0

lw $s3,Main.m
li $s3, 0

lw $s2,Main.j
li $s2, 0

sw $t5, Main.n
sw $s2, Main.j
sw $t1, Main.arr2
sw $s3, Main.m
sw $s6, Main.t.19
sw $s5, Main.arr

move $fp, $sp
addiu $sp, $sp, -28
jal Main.main

#-----------------------------------block id: 140249139615360

jal exit_func

#-----------------------------------block id: 140249139615432
Main.main:


#-----------------------------------block id: 140249139615504
LET_BEGIN_Main.main.LET_1:

lw $t5, Main.n
lw $s6, -4($fp)
li $v0, 9
move $a0, $t5
sll $a0, $a0, 2
syscall
move $s6, $v0

lw $s5,Main.j
li $s5, 0

sw $t5, Main.n
sw $s5, Main.j
sw $s6, -4($fp)

#-----------------------------------block id: 140249139615576
label.10:

lw $t5, Main.j
lw $s6, Main.n
lw $s5, -8($fp)
slt $s5, $t5, $s6

li $t7,0
sw $s6, Main.n
sw $t5, Main.j
sw $s5, -8($fp)

beq $s5,$t7,label.11

#-----------------------------------block id: 140249139615648
lw $t5, Main.j
lw $s6, Main.m
lw $s5, Main.arr2
sll $t7, $t5, 2
add $t8, $s5, $t7
sw $s6, 0($t8)

lw $t1, -16($fp)
addi $t1, $s6, 1

move $s6, $t1

lw $s3, -20($fp)
sll $t7, $t5, 2
add $t8, $s5, $t7
lw $s3, 0($t8)

move $t9, $ra
move $a0,$s3
jal print_int
move $ra, $t9

sw $t5, Main.j
sw $s5, Main.arr2
sw $s6, Main.m
sw $s3, -20($fp)
sw $t1, -16($fp)

#-----------------------------------block id: 140249139615720
label.12:

lw $t5, Main.j
lw $s6, -12($fp)
addi $s6, $t5, 1

move $t5, $s6

sw $t5, Main.j
sw $s6, -12($fp)

j label.10

#-----------------------------------block id: 140249139615792
label.11:

lw $t5, -24($fp)
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

lw $s5, Main.arr2
addiu $sp, $sp, -4
sw $s5, ($sp)

addiu $sp, $sp, -4
li $t7, 4
sw $t7, ($sp)

addiu $sp, $sp, -4
sw $s6, ($sp)

sw $s6, Main.obj
sw $s5, Main.arr2
sw $t5, -24($fp)

move $fp, $sp
addiu $sp, $sp, -36
jal Test.print1darray

#-----------------------------------block id: 140249139615864
lw $t5, -28($fp)
lw $fp, ($sp)
addiu $sp, $sp, 4
lw $ra, ($sp)
addiu $sp, $sp, 4
move $t5, $v0

sw $t5, -28($fp)

#-----------------------------------block id: 140249139615936
LET_OVER_LET_1:


jal exit_func

#-----------------------------------block id: 140249139616008
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
strcpy:
move $t9, $a0
move $t8, $a1
strcpy.loop:
lb $t7, 0($t9)
beq $t7, $zero, strcpy.end
addiu $t9, $t9, 1
sb $t7, 0($t8)
addiu $t8, $t8, 1
b strcpy.loop
strcpy.end:
sb $zero, 0($t8)
move $v0, $t9
jr $ra
strcat:
move $t9, $a0
move $t8, $a1
strcat.first:
lb $t7, 0($t9)
beqz $t7, strcat.second
addiu $t9, $t9 ,1
j strcat.first
strcat.second:
lb $t7, 0($t8)
sb $t7, 0($t9)
beqz $t7, strcat.end
addiu $t8, $t8, 1
addiu $t9, $t9, 1
j strcat.second
strcat.end:
sb $zero, 0($t9)
jr $ra
