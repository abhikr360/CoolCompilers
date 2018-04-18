.data
space: .asciiz " "
Main.n : .word 0
Main.i : .word 0
Main.list : .word 0
Main.no : .word 0
.text
main:

j CLASS.Main

#-----------------------------------block id: 140108591460720

jal exit_func

#-----------------------------------block id: 140108591460792
CLASS.Node:


#-----------------------------------block id: 140108591463744
Node.set_data:

lw $t5, -8($fp)
lw $t7, 0($fp)
sw $t7, -4($fp)
move $t5, $t7

lw $s6, -4($fp)
lw $t7, 4($fp)
sw $t7, -8($fp)
move $s6, $t7

li $t7, 0
sll $t7, $t7, 2
add $t8, $t5,$t7
sw $s6, 0($t8)

addiu $sp, $sp, 4

addiu $sp, $sp, 4

addiu $sp, $sp, 8
sw $t5, -8($fp)
sw $s6, -4($fp)

jr $ra

#-----------------------------------block id: 140108591463816
Node.set_next:

lw $t5, -8($fp)
lw $t7, 0($fp)
sw $t7, -4($fp)
move $t5, $t7

lw $s6, -4($fp)
lw $t7, 4($fp)
sw $t7, -8($fp)
move $s6, $t7

lw $s5, -12($fp)
li $v0, 9
li $a0, 8
sll $a0, $a0, 2
syscall
move $s5, $v0

li $t7, 1
sll $t7, $t7, 2
add $t8, $t5,$t7
sw $s5, 0($t8)

li $t7, 1
sll $t7, $t7, 2
add $t8, $t5,$t7
sw $s6, 0($t8)

addiu $sp, $sp, 4

addiu $sp, $sp, 4

addiu $sp, $sp, 12
sw $s5, -12($fp)
sw $t5, -8($fp)
sw $s6, -4($fp)

jr $ra

#-----------------------------------block id: 140108591464176
Node.print_data:

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

addiu $sp, $sp, 4

addiu $sp, $sp, 8
sw $s6, -8($fp)
sw $t5, -4($fp)

jr $ra

#-----------------------------------block id: 140108591464248
CLASS.Main:

lw $t5, Main.list
li $v0, 9
li $a0, 6
sll $a0, $a0, 2
syscall
move $t5, $v0

sw $t5, Main.list

move $fp, $sp
addiu $sp, $sp, -16
jal Main.main

#-----------------------------------block id: 140108591464032

jal exit_func

#-----------------------------------block id: 140108591464104
Main.main:

lw $t5,Main.n
li $t5, 1

lw $s6,Main.i
li $s6, 1

lw $s5, -4($fp)
li $v0, 9
li $a0, 8
sll $a0, $a0, 2
syscall
move $s5, $v0

lw $s4, Main.list
li $t7, 1
sll $t7, $t7, 2
add $t8, $s4,$t7
sw $s5, 0($t8)

lw $s3, -8($fp)
li $t7, 0
sll $t7, $t7, 2
add $t8, $s3,$t7
li $t9, 4
sw $t9, 0($t8)

move $t9, $ra
move $a0,$s6
jal print_int
move $ra, $t9

lw $s2, -12($fp)
li $t7, 1
sll $t8, $t7, 2
add $t8, $s4,$t8
lw $s2, 0($t8)

addiu $sp, $sp, -4
sw $s2, ($sp)

addiu $sp, $sp, -4
sw $ra, ($sp)
addiu $sp, $sp, -4
sw $fp, ($sp)

sw $s2, -12($fp)
sw $s3, -8($fp)
sw $s5, -4($fp)
sw $t5, Main.n
sw $s4, Main.list
sw $s6, Main.i

move $fp, $sp
addiu $sp, $sp, -8
jal Node.print_data

#-----------------------------------block id: 140108591463600
lw $t5, -16($fp)
lw $fp, ($sp)
addiu $sp, $sp, 4
lw $ra, ($sp)
addiu $sp, $sp, 4
move $t5, $v0

sw $t5, -16($fp)

jal exit_func

#-----------------------------------block id: 140108591463672
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
