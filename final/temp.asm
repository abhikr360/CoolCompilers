.data
space: .asciiz " "
Main.t.1 : .word 0
Main.t.2 : .word 0
Main.t.3 : .word 0
Main.khetan : .word 0
Main.arjun : .word 0
Main.a : .word 0
Main.hall12 : .word 0
.text
main:
move $fp, $sp


j CLASS.Main

#-----------------------------------block id: 140129104169728

jal exit_func

#-----------------------------------block id: 140129104169368
CLASS.Kotha:


#-----------------------------------block id: 140129104169440
CLASS.Randi:

la $t5, -16($fp)
li $v0, 9
li $a0, 5
sll $a0, $a0, 2
syscall
move $t5, $v0

la $s6, -36($fp)
li $v0, 9
li $a0, 4
sll $a0, $a0, 2
syscall
move $s6, $v0

sw $s6, -36($fp)
sw $t5, -16($fp)

#-----------------------------------block id: 140129104183024
CLASS.Main:

lw $t5,Main.t.1
li $v0, 9
li $a0, 20
sll $a0, $a0, 2
syscall
move $t5, $v0

lw $s6,Main.t.2
li $v0, 9
li $a0, 20
sll $a0, $a0, 2
syscall
move $s6, $v0

li $t7, 3
sll $t7, $t7, 2
add $t8, $t5,$t7
sw $s6, 0($t8)

lw $s5,Main.t.3
li $v0, 9
li $a0, 16
sll $a0, $a0, 2
syscall
move $s5, $v0

li $t7, 4
sll $t7, $t7, 2
add $t8, $t5,$t7
sw $s5, 0($t8)

lw $s4,Main.khetan
move $s4, $t5

lw $s3,Main.a
li $s3, 4

sw $s4, Main.khetan
sw $s3, Main.a
sw $s5, Main.t.3
sw $s6, Main.t.2
sw $t5, Main.t.1

move $fp, $sp
addiu $sp, $sp, -84
jal Main.main

#-----------------------------------block id: 140129104182952

jal exit_func

#-----------------------------------block id: 140129104169512
Main.printrandis:

lw $t5, Main.a
move $a0,$t5
jal print_int

lw $s6, Main.arjun
lw $s5, -4($fp)
li $t7, 2
sll $t8, $t7, 2
add $t8, $s6,$t8
lw $s5, 0($t8)

move $a0,$s5
jal print_int

lw $s4, Main.khetan
lw $s3, -8($fp)
li $t7, 1
sll $t8, $t7, 2
add $t8, $s4,$t8
lw $s3, 0($t8)

move $a0,$s3
jal print_int

lw $s2, -12($fp)
li $t7, 0
sll $t8, $t7, 2
add $t8, $s4,$t8
lw $s2, 0($t8)

move $a0,$s2
jal print_int

addiu $sp, $sp, 12
sw $s4, Main.khetan
sw $s3, -8($fp)
sw $s2, -12($fp)
sw $s6, Main.arjun
sw $t5, Main.a
sw $s5, -4($fp)

jr $ra

#-----------------------------------block id: 140129104169584
Main.main:

lw $t5, Main.a
move $a0,$t5
jal print_int

lw $s6, Main.khetan
lw $s5, -4($fp)
li $t7, 3
sll $t8, $t7, 2
add $t8, $s6,$t8
lw $s5, 0($t8)

li $t7, 0
sll $t7, $t7, 2
add $t8, $s5,$t7
li $t9, 1
sw $t9, 0($t8)

lw $s4, -8($fp)
li $t7, 3
sll $t8, $t7, 2
add $t8, $s6,$t8
lw $s4, 0($t8)

lw $s3, -12($fp)
li $t7, 0
sll $t8, $t7, 2
add $t8, $s4,$t8
lw $s3, 0($t8)

move $a0,$s3
jal print_int

li $t7, 1
sll $t7, $t7, 2
add $t8, $s6,$t7
li $t9, 999
sw $t9, 0($t8)

lw $s2, -16($fp)
li $v0, 9
li $a0, 20
sll $a0, $a0, 2
syscall
move $s2, $v0

lw $s1, -20($fp)
li $v0, 9
li $a0, 20
sll $a0, $a0, 2
syscall
move $s1, $v0

li $t7, 3
sll $t7, $t7, 2
add $t8, $s2,$t7
sw $s1, 0($t8)

lw $s0, -24($fp)
li $v0, 9
li $a0, 16
sll $a0, $a0, 2
syscall
move $s0, $v0

li $t7, 4
sll $t7, $t7, 2
add $t8, $s2,$t7
sw $s0, 0($t8)

lw $t2,Main.arjun
move $t2, $s2

lw $t3, -28($fp)
li $v0, 9
li $a0, 8
sll $a0, $a0, 2
syscall
move $t3, $v0

lw $t0,Main.hall12
move $t0, $t3

li $t7, 1
sll $t7, $t7, 2
add $t8, $t0,$t7
li $t9, 69
sw $t9, 0($t8)

lw $t1, -32($fp)
li $t7, 4
sll $t8, $t7, 2
add $t8, $t2,$t8
lw $t1, 0($t8)

li $t7, 1
sll $t7, $t7, 2
add $t8, $t1,$t7
sw $t0, 0($t8)

lw $t6, -36($fp)
li $t7, 4
sll $t8, $t7, 2
add $t8, $s6,$t8
lw $t6, 0($t8)

lw $t4, -40($fp)
li $t7, 4
sll $t8, $t7, 2
add $t8, $t2,$t8
lw $t4, 0($t8)

li $t7, 2
sll $t7, $t7, 2
add $t8, $t6,$t7
sw $t4, 0($t8)

sw $t6, -36($fp)
lw $t6, -44($fp)
li $t7, 1
sll $t8, $t7, 2
add $t8, $t4,$t8
lw $t6, 0($t8)

sw $t4, -40($fp)
lw $t4, -48($fp)
li $t7, 4
sll $t8, $t7, 2
add $t8, $s6,$t8
lw $t4, 0($t8)

sw $s6, Main.khetan
lw $s6, -52($fp)
li $t7, 2
sll $t8, $t7, 2
add $t8, $t4,$t8
lw $s6, 0($t8)

sw $t4, -48($fp)
lw $t4, -56($fp)
li $t7, 1
sll $t8, $t7, 2
add $t8, $s6,$t8
lw $t4, 0($t8)

move $a0,$t4
jal print_int

sw $t4, -56($fp)
lw $t4, -60($fp)
li $t7, 4
sll $t8, $t7, 2
add $t8, $t2,$t8
lw $t4, 0($t8)

sw $s6, -52($fp)
lw $s6, -64($fp)
li $t7, 1
sll $t8, $t7, 2
add $t8, $t4,$t8
lw $s6, 0($t8)

sw $t4, -60($fp)
lw $t4, -68($fp)
li $t7, 1
sll $t8, $t7, 2
add $t8, $s6,$t8
lw $t4, 0($t8)

move $a0,$t4
jal print_int

li $t7, 2
sll $t7, $t7, 2
add $t8, $t2,$t7
li $t9, 4
sw $t9, 0($t8)

sw $t4, -68($fp)
lw $t4, -72($fp)
li $t7, 3
sll $t8, $t7, 2
add $t8, $t2,$t8
lw $t4, 0($t8)

li $t7, 0
sll $t7, $t7, 2
add $t8, $t4,$t7
li $t9, 555
sw $t9, 0($t8)

sw $t4, -72($fp)
lw $t4, -76($fp)
li $t7, 3
sll $t8, $t7, 2
add $t8, $t2,$t8
lw $t4, 0($t8)

sw $t2, Main.arjun
lw $t2, -80($fp)
li $t7, 0
sll $t8, $t7, 2
add $t8, $t4,$t8
lw $t2, 0($t8)

move $a0,$t2
jal print_int

sw $s6, -64($fp)
sw $t4, -76($fp)
sw $t2, -80($fp)
sw $t1, -32($fp)
sw $t6, -44($fp)
sw $s4, -8($fp)
sw $t5, Main.a
sw $s1, -20($fp)
sw $s2, -16($fp)
sw $t3, -28($fp)
sw $s0, -24($fp)
sw $t0, Main.hall12
sw $s5, -4($fp)
sw $s3, -12($fp)

move $fp, $sp
addiu $sp, $sp, -12
jal Main.printrandis

#-----------------------------------block id: 140129104169080
lw $t5, -84($fp)
lw $fp, ($sp)
addiu $sp, $sp, 4
lw $ra, ($sp)
addiu $sp, $sp, 4
move $t5, $v0

addiu $sp, $sp, 84
sw $t5, -84($fp)

jr $ra

#-----------------------------------block id: 140129104169152
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
