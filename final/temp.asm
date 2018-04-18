.data
space: .asciiz " "
Main.t.13 : .word 0
Main.a : .word 0
Main.t.14 : .word 0
Main.k : .word 0
Main.t.15 : .word 0
Main.man : .word 0
.text
main:

j CLASS.Main

#-----------------------------------block id: 140494227278376

jal exit_func

#-----------------------------------block id: 140494227278448
CLASS.A:


#-----------------------------------block id: 140494227278088
A.sum:

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

lw $s4, -16($fp)
add $s4, $s5, $s6

lw $s3, -20($fp)
li $t7, 0
sll $t8, $t7, 2
add $t8, $t5,$t8
lw $s3, 0($t8)

lw $s2, -24($fp)
add $s2, $s4, $s3

sw $s2, -24($fp)
sw $s3, -20($fp)
sw $s4, -16($fp)
sw $s6, -8($fp)
sw $s5, -4($fp)
sw $t5, -12($fp)

move $v0, $s2

#-----------------------------------block id: 140494227278160
addiu $sp, $sp, 4

addiu $sp, $sp, 4

addiu $sp, $sp, 4

addiu $sp, $sp, 24

jr $ra

#-----------------------------------block id: 140494227277944
B.sum:

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

lw $s4, -16($fp)
add $s4, $s5, $s6

lw $s3, -20($fp)
li $t7, 0
sll $t8, $t7, 2
add $t8, $t5,$t8
lw $s3, 0($t8)

lw $s2, -24($fp)
add $s2, $s4, $s3

lw $s1, -28($fp)
li $t7, 2
sll $t8, $t7, 2
add $t8, $t5,$t8
lw $s1, 0($t8)

lw $s0, -32($fp)
add $s0, $s2, $s1

sw $t5, -12($fp)
sw $s5, -4($fp)
sw $s6, -8($fp)
sw $s0, -32($fp)
sw $s4, -16($fp)
sw $s3, -20($fp)
sw $s2, -24($fp)
sw $s1, -28($fp)

move $v0, $s0

#-----------------------------------block id: 140494227278016
addiu $sp, $sp, 4

addiu $sp, $sp, 4

addiu $sp, $sp, 4

addiu $sp, $sp, 32

jr $ra

#-----------------------------------block id: 140494227276576
B.setsum:

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

addiu $sp, $sp, -4
sw $ra, ($sp)
addiu $sp, $sp, -4
sw $fp, ($sp)

addiu $sp, $sp, -4
sw $s5, ($sp)

addiu $sp, $sp, -4
sw $s6, ($sp)

addiu $sp, $sp, -4
sw $t5, ($sp)

sw $t5, -12($fp)
sw $s5, -4($fp)
sw $s6, -8($fp)

move $fp, $sp
addiu $sp, $sp, -32
jal B.sum

#-----------------------------------block id: 140494227277872
lw $t5, -16($fp)
lw $fp, ($sp)
addiu $sp, $sp, 4
lw $ra, ($sp)
addiu $sp, $sp, 4
move $t5, $v0

lw $s6, -12($fp)
li $t7, 2
sll $t7, $t7, 2
add $t8, $s6,$t7
sw $t5, 0($t8)

sw $s6, -12($fp)
sw $t5, -16($fp)

li $v0, 0

#-----------------------------------block id: 140494227276504
addiu $sp, $sp, 4

addiu $sp, $sp, 4

addiu $sp, $sp, 4

addiu $sp, $sp, 16

jr $ra

#-----------------------------------block id: 140494227276432
C.me:

lw $t5, -4($fp)
lw $t7, 0($fp)
sw $t7, -4($fp)
move $t5, $t7

addiu $sp, $sp, -4
sw $ra, ($sp)
addiu $sp, $sp, -4
sw $fp, ($sp)

addiu $sp, $sp, -4
li $t7, 99
sw $t7, ($sp)

addiu $sp, $sp, -4
li $t7, 101
sw $t7, ($sp)

addiu $sp, $sp, -4
sw $t5, ($sp)

sw $t5, -4($fp)

move $fp, $sp
addiu $sp, $sp, -16
jal B.setsum

#-----------------------------------block id: 140494227276288
lw $t5, -8($fp)
lw $fp, ($sp)
addiu $sp, $sp, 4
lw $ra, ($sp)
addiu $sp, $sp, 4
move $t5, $v0

lw $s6, -4($fp)
lw $s5, -12($fp)
li $t7, 2
sll $t8, $t7, 2
add $t8, $s6,$t8
lw $s5, 0($t8)

move $t9, $ra
move $a0,$s5
jal print_int
move $ra, $t9

lw $s4, -16($fp)
li $t7, 3
sll $t8, $t7, 2
add $t8, $s6,$t8
lw $s4, 0($t8)

move $t9, $ra
move $a0,$s4
jal print_int
move $ra, $t9

sw $t5, -8($fp)
sw $s4, -16($fp)
sw $s5, -12($fp)
sw $s6, -4($fp)

li $v0, 0

#-----------------------------------block id: 140494227276360
addiu $sp, $sp, 4

addiu $sp, $sp, 16

jr $ra

#-----------------------------------block id: 140494227303240
CLASS.Main:

lw $t5,Main.t.13
li $v0, 9
li $a0, 8
sll $a0, $a0, 2
syscall
move $t5, $v0

lw $s6,Main.a
move $s6, $t5

lw $s5,Main.t.14
li $v0, 9
li $a0, 12
sll $a0, $a0, 2
syscall
move $s5, $v0

lw $s4,Main.k
move $s4, $s5

lw $s3,Main.t.15
li $v0, 9
li $a0, 16
sll $a0, $a0, 2
syscall
move $s3, $v0

lw $s2,Main.man
move $s2, $s3

sw $s4, Main.k
sw $t5, Main.t.13
sw $s3, Main.t.15
sw $s5, Main.t.14
sw $s2, Main.man
sw $s6, Main.a

move $fp, $sp
addiu $sp, $sp, -28
jal Main.main

#-----------------------------------block id: 140494227303312

jal exit_func

#-----------------------------------block id: 140494227065744
Main.main:

lw $t5,Main.k
li $t7, 0
sll $t7, $t7, 2
add $t8, $t5,$t7
li $t9, 100
sw $t9, 0($t8)

li $t7, 1
sll $t7, $t7, 2
add $t8, $t5,$t7
li $t9, 200
sw $t9, 0($t8)

li $t7, 2
sll $t7, $t7, 2
add $t8, $t5,$t7
li $t9, 300
sw $t9, 0($t8)

lw $s6,Main.a
li $t7, 0
sll $t7, $t7, 2
add $t8, $s6,$t7
li $t9, 1000
sw $t9, 0($t8)

li $t7, 1
sll $t7, $t7, 2
add $t8, $s6,$t7
li $t9, 2000
sw $t9, 0($t8)

lw $s5,Main.man
li $t7, 0
sll $t7, $t7, 2
add $t8, $s5,$t7
li $t9, 10000
sw $t9, 0($t8)

li $t7, 1
sll $t7, $t7, 2
add $t8, $s5,$t7
li $t9, 20000
sw $t9, 0($t8)

li $t7, 2
sll $t7, $t7, 2
add $t8, $s5,$t7
li $t9, 30000
sw $t9, 0($t8)

addiu $sp, $sp, -4
sw $ra, ($sp)
addiu $sp, $sp, -4
sw $fp, ($sp)

addiu $sp, $sp, -4
li $t7, 2
sw $t7, ($sp)

addiu $sp, $sp, -4
li $t7, 3
sw $t7, ($sp)

addiu $sp, $sp, -4
sw $t5, ($sp)

sw $t5, Main.k
sw $s5, Main.man
sw $s6, Main.a

move $fp, $sp
addiu $sp, $sp, -32
jal B.sum

#-----------------------------------block id: 140494227065816
lw $t5, -4($fp)
lw $fp, ($sp)
addiu $sp, $sp, 4
lw $ra, ($sp)
addiu $sp, $sp, 4
move $t5, $v0

move $t9, $ra
move $a0,$t5
jal print_int
move $ra, $t9

move $t9,$ra
jal space_func
move $ra,$t9

addiu $sp, $sp, -4
sw $ra, ($sp)
addiu $sp, $sp, -4
sw $fp, ($sp)

addiu $sp, $sp, -4
li $t7, 2
sw $t7, ($sp)

addiu $sp, $sp, -4
li $t7, 3
sw $t7, ($sp)

lw $s6, Main.k
addiu $sp, $sp, -4
sw $s6, ($sp)

sw $s6, Main.k
sw $t5, -4($fp)

move $fp, $sp
addiu $sp, $sp, -24
jal A.sum

#-----------------------------------block id: 140494227065888
lw $t5, -8($fp)
lw $fp, ($sp)
addiu $sp, $sp, 4
lw $ra, ($sp)
addiu $sp, $sp, 4
move $t5, $v0

move $t9, $ra
move $a0,$t5
jal print_int
move $ra, $t9

move $t9,$ra
jal space_func
move $ra,$t9

addiu $sp, $sp, -4
sw $ra, ($sp)
addiu $sp, $sp, -4
sw $fp, ($sp)

addiu $sp, $sp, -4
li $t7, 5
sw $t7, ($sp)

addiu $sp, $sp, -4
li $t7, 7
sw $t7, ($sp)

lw $s6, Main.k
addiu $sp, $sp, -4
sw $s6, ($sp)

sw $s6, Main.k
sw $t5, -8($fp)

move $fp, $sp
addiu $sp, $sp, -16
jal B.setsum

#-----------------------------------block id: 140494227065960
lw $t5, -12($fp)
lw $fp, ($sp)
addiu $sp, $sp, 4
lw $ra, ($sp)
addiu $sp, $sp, 4
move $t5, $v0

lw $s6, Main.k
lw $s5, -16($fp)
li $t7, 2
sll $t8, $t7, 2
add $t8, $s6,$t8
lw $s5, 0($t8)

move $t9, $ra
move $a0,$s5
jal print_int
move $ra, $t9

move $t9,$ra
jal space_func
move $ra,$t9

addiu $sp, $sp, -4
sw $ra, ($sp)
addiu $sp, $sp, -4
sw $fp, ($sp)

addiu $sp, $sp, -4
li $t7, 99
sw $t7, ($sp)

addiu $sp, $sp, -4
li $t7, 1
sw $t7, ($sp)

lw $s4, Main.a
addiu $sp, $sp, -4
sw $s4, ($sp)

sw $s6, Main.k
sw $s5, -16($fp)
sw $t5, -12($fp)
sw $s4, Main.a

move $fp, $sp
addiu $sp, $sp, -24
jal A.sum

#-----------------------------------block id: 140494227066032
lw $t5, -20($fp)
lw $fp, ($sp)
addiu $sp, $sp, 4
lw $ra, ($sp)
addiu $sp, $sp, 4
move $t5, $v0

move $t9, $ra
move $a0,$t5
jal print_int
move $ra, $t9

lw $s6, -24($fp)
li $s6, -9

lw $s5,Main.man
li $t7, 3
sll $t7, $t7, 2
add $t8, $s5,$t7
sw $s6, 0($t8)

addiu $sp, $sp, -4
sw $ra, ($sp)
addiu $sp, $sp, -4
sw $fp, ($sp)

addiu $sp, $sp, -4
sw $s5, ($sp)

sw $s6, -24($fp)
sw $t5, -20($fp)
sw $s5, Main.man

move $fp, $sp
addiu $sp, $sp, -16
jal C.me

#-----------------------------------block id: 140494227066104
lw $t5, -28($fp)
lw $fp, ($sp)
addiu $sp, $sp, 4
lw $ra, ($sp)
addiu $sp, $sp, 4
move $t5, $v0

sw $t5, -28($fp)

jal exit_func

#-----------------------------------block id: 140494227066176
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
