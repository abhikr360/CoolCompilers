.data
space: .asciiz " "
Main.t.1 : .word 0
Main.khetan : .word 0
Main.arjun : .word 0
Main.a : .word 0
.text
main:
move $fp, $sp


j CLASS.Main

#-----------------------------------block id: 139825730492176

jal exit_func

#-----------------------------------block id: 139825730492248
CLASS.Randi:


#-----------------------------------block id: 139825730481904
CLASS.Main:

lw $t5,Main.t.1
li $v0, 9
li $a0, 12
sll $a0, $a0, 2
syscall
move $t5, $v0

lw $s6,Main.khetan
move $s6, $t5

lw $s5,Main.a
li $s5, 4

sw $s6, Main.khetan
sw $t5, Main.t.1
sw $s5, Main.a

move $fp, $sp
addiu $sp, $sp, -8
jal Main.main

#-----------------------------------block id: 139825730480464

jal exit_func

#-----------------------------------block id: 139825730481976
Main.printrandis:

addiu $sp, $sp, -4
sw $ra, ($sp)
addiu $sp, $sp, -4
sw $fp, ($sp)

lw $t5, Main.a
addiu $sp, $sp, -4
sw $t5, ($sp)

move $a0,$t5
jal print_int

lw $s6, Main.arjun
lw $s5, -4($fp)
li $t7, 8
sll $t8, $t7, 2
add $t8, $s6,$t8
lw $s5, 0($t8)

addiu $sp, $sp, -4
sw $ra, ($sp)
addiu $sp, $sp, -4
sw $fp, ($sp)

addiu $sp, $sp, -4
sw $s5, ($sp)

move $a0,$s5
jal print_int

lw $s4, Main.khetan
lw $s3, -8($fp)
li $t7, 4
sll $t8, $t7, 2
add $t8, $s4,$t8
lw $s3, 0($t8)

addiu $sp, $sp, -4
sw $ra, ($sp)
addiu $sp, $sp, -4
sw $fp, ($sp)

addiu $sp, $sp, -4
sw $s3, ($sp)

move $a0,$s3
jal print_int

lw $s2, -12($fp)
li $t7, 0
sll $t8, $t7, 2
add $t8, $s4,$t8
lw $s2, 0($t8)

addiu $sp, $sp, -4
sw $ra, ($sp)
addiu $sp, $sp, -4
sw $fp, ($sp)

addiu $sp, $sp, -4
sw $s2, ($sp)

move $a0,$s2
jal print_int

addiu $sp, $sp, 12
sw $s2, -12($fp)
sw $s4, Main.khetan
sw $s3, -8($fp)
sw $s6, Main.arjun
sw $s5, -4($fp)
sw $t5, Main.a

jr $ra

#-----------------------------------block id: 139825730480536
Main.main:

addiu $sp, $sp, -4
sw $ra, ($sp)
addiu $sp, $sp, -4
sw $fp, ($sp)

lw $t5, Main.a
addiu $sp, $sp, -4
sw $t5, ($sp)

move $a0,$t5
jal print_int

lw $s6,Main.khetan
li $t7, 0
sll $t7, $t7, 2
add $t8, $s6,$t7
li $t9, 11
sw $t9, 0($t8)

li $t7, 4
sll $t7, $t7, 2
add $t8, $s6,$t7
li $t9, 999
sw $t9, 0($t8)

lw $s5, -4($fp)
li $v0, 9
li $a0, 12
sll $a0, $a0, 2
syscall
move $s5, $v0

lw $s4,Main.arjun
move $s4, $s5

li $t7, 8
sll $t7, $t7, 2
add $t8, $s4,$t7
li $t9, 4
sw $t9, 0($t8)

sw $s5, -4($fp)
sw $s6, Main.khetan
sw $s4, Main.arjun
sw $t5, Main.a

move $fp, $sp
addiu $sp, $sp, -12
jal Main.printrandis

#-----------------------------------block id: 139825730476656
lw $t5, -8($fp)
lw $fp, ($sp)
addiu $sp, $sp, 4
lw $ra, ($sp)
addiu $sp, $sp, 4
move $t5, $v0

addiu $sp, $sp, 8
sw $t5, -8($fp)

jr $ra

#-----------------------------------block id: 139825730476728
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
