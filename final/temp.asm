.data
space: .asciiz " "
Main.n : .word 0
Main.m : .word 0
.text
main:
move $fp, $sp


j CLASS.Main

#-----------------------------------block id: 139986924757360

jal exit_func

#-----------------------------------block id: 139986924757720
CLASS.Main:

lw $t5, Main.n
li $v0, 9
li $a0, 3
sll $a0, $a0, 2
syscall
move $t5, $v0

lw $s6, Main.m
li $v0, 9
li $a0, 6
sll $a0, $a0, 2
syscall
move $s6, $v0

sw $t5, Main.n
sw $s6, Main.m

move $fp, $sp
addiu $sp, $sp, -32
jal Main.main

#-----------------------------------block id: 139986924757792

jal exit_func

#-----------------------------------block id: 139986924757144
Main.main:

lw $t5, Main.m
li $t7, 0
sll $t7, $t7, 2
add $t8, $t5,$t7
li $t9, 5
sw $t9, 0($t8)

li $t7, 1
sll $t7, $t7, 2
add $t8, $t5,$t7
li $t9, 1
sw $t9, 0($t8)

li $t7, 2
sll $t7, $t7, 2
add $t8, $t5,$t7
li $t9, 2
sw $t9, 0($t8)

li $t7, 3
sll $t7, $t7, 2
add $t8, $t5,$t7
li $t9, 3
sw $t9, 0($t8)

li $t7, 4
sll $t7, $t7, 2
add $t8, $t5,$t7
li $t9, 4
sw $t9, 0($t8)

li $t7, 5
sll $t7, $t7, 2
add $t8, $t5,$t7
li $t9, 3
sw $t9, 0($t8)

sw $t5, Main.m

#-----------------------------------block id: 139986924757216
LET_BEGIN_Main.main.LET_1:

la $t5, -16($fp)
li $v0, 9
li $a0, 4
sll $a0, $a0, 2
syscall
move $t5, $v0

lw $s6, Main.m
lw $s5, -28($fp)
li $t7, 1
sll $t8, $t7, 2
add $t8, $s6,$t8
lw $s5, 0($t8)

lw $s4, -20($fp)
li $t7, 5
sll $t8, $t7, 2
add $t8, $s6,$t8
lw $s4, 0($t8)

lw $s3, -24($fp)
sll $t7, $s4, 2
add $t8, $s6, $t7
lw $s3, 0($t8)

sll $t7, $s3, 2
add $t8, $t5, $t7
sw $s5, 0($t8)

lw $s2, -32($fp)
li $t7, 3
sll $t8, $t7, 2
add $t8, $t5,$t8
lw $s2, 0($t8)

addiu $sp, $sp, -4
sw $ra, ($sp)
addiu $sp, $sp, -4
sw $fp, ($sp)

addiu $sp, $sp, -4
sw $s2, ($sp)

move $a0,$s2
jal print_int

sw $t5, -16($fp)
sw $s2, -32($fp)
sw $s6, Main.m
sw $s3, -24($fp)
sw $s5, -28($fp)
sw $s4, -20($fp)

#-----------------------------------block id: 139986924758296
LET_OVER_LET_1:

lw $t5, Main.m
lw $s6, -4($fp)
li $t7, 5
sll $t8, $t7, 2
add $t8, $t5,$t8
lw $s6, 0($t8)

lw $s5, -8($fp)
sll $t7, $s6, 2
add $t8, $t5, $t7
lw $s5, 0($t8)

lw $s4, -12($fp)
sll $t7, $s5, 2
add $t8, $t5, $t7
lw $s4, 0($t8)

addiu $sp, $sp, -4
sw $ra, ($sp)
addiu $sp, $sp, -4
sw $fp, ($sp)

addiu $sp, $sp, -4
sw $s4, ($sp)

move $a0,$s4
jal print_int

addiu $sp, $sp, 32
sw $s6, -4($fp)
sw $s4, -12($fp)
sw $s5, -8($fp)
sw $t5, Main.m

jr $ra

#-----------------------------------block id: 139986924758368
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
