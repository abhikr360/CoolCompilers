.data
space: .asciiz " "
Main.n : .word 0
Main.i : .word 0
Main.list : .word 0
Main.no : .word 0
.text
main:

j CLASS.Main

#-----------------------------------block id: 140009149648120

jal exit_func

#-----------------------------------block id: 140009149635616
CLASS.Node:


#-----------------------------------block id: 140009149635688
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
sw $s6, -4($fp)
sw $t5, -8($fp)

jr $ra

#-----------------------------------block id: 140009149648768
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
sw $s6, -4($fp)
sw $t5, -8($fp)

jr $ra

#-----------------------------------block id: 140009149648840
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
sw $t5, -4($fp)
sw $s6, -8($fp)

jr $ra

#-----------------------------------block id: 140009149645024
CLASS.Main:

lw $t5, Main.list
li $v0, 9
li $a0, 6
sll $a0, $a0, 2
syscall
move $t5, $v0

sw $t5, Main.list

move $fp, $sp
addiu $sp, $sp, -52
jal Main.main

#-----------------------------------block id: 140009149652288

jal exit_func

#-----------------------------------block id: 140009149652360
Main.main:

lw $t5,Main.n
li $t5, 6

lw $s6, -4($fp)
li $v0, 9
li $a0, 8
sll $a0, $a0, 2
syscall
move $s6, $v0

lw $s5,Main.no
move $s5, $s6

lw $s4,Main.i
li $s4, 0

sw $s5, Main.no
sw $t5, Main.n
sw $s4, Main.i
sw $s6, -4($fp)

#-----------------------------------block id: 140009149645096
label.5:

lw $t5, Main.i
lw $s6, Main.n
lw $s5, -8($fp)
slt $s5, $t5, $s6

li $t7,0
sw $s6, Main.n
sw $t5, Main.i
sw $s5, -8($fp)

beq $s5,$t7,label.6

#-----------------------------------block id: 140009149644880
lw $t5, Main.i
move $t9, $ra
move $a0,$t5
jal print_int
move $ra, $t9

lw $s6, -16($fp)
li $v0, 9
li $a0, 8
sll $a0, $a0, 2
syscall
move $s6, $v0

lw $s5, Main.list
sll $t7, $t5, 2
add $t8, $s5, $t7
sw $s6, 0($t8)

lw $s4, -20($fp)
sll $t7, $t5, 2
add $t8, $s5, $t7
lw $s4, 0($t8)

addiu $sp, $sp, -4
sw $ra, ($sp)
addiu $sp, $sp, -4
sw $fp, ($sp)

addiu $sp, $sp, -4
sw $t5, ($sp)

addiu $sp, $sp, -4
sw $s4, ($sp)

sw $t5, Main.i
sw $s5, Main.list
sw $s6, -16($fp)
sw $s4, -20($fp)

move $fp, $sp
addiu $sp, $sp, -8
jal Node.set_data

#-----------------------------------block id: 140009149644952
lw $t5, -24($fp)
lw $fp, ($sp)
addiu $sp, $sp, 4
lw $ra, ($sp)
addiu $sp, $sp, 4
move $t5, $v0

lw $s6, Main.i
lw $s5, -28($fp)
li $t7,0
sgt $s5, $s6, $t7

li $t7,0
sw $s6, Main.i
sw $s5, -28($fp)
sw $t5, -24($fp)

bgt $s5,$t7,label.3

#-----------------------------------block id: 140009149636480

j label.4

#-----------------------------------block id: 140009149636552
label.3:

lw $t5, Main.list
lw $s6, Main.i
lw $s5, -32($fp)
sll $t7, $s6, 2
add $t8, $t5, $t7
lw $s5, 0($t8)

lw $s4, -36($fp)
addi $s4, $s6, -1

lw $s3, -40($fp)
sll $t7, $s4, 2
add $t8, $t5, $t7
lw $s3, 0($t8)

addiu $sp, $sp, -4
sw $ra, ($sp)
addiu $sp, $sp, -4
sw $fp, ($sp)

addiu $sp, $sp, -4
sw $s3, ($sp)

addiu $sp, $sp, -4
sw $s5, ($sp)

sw $s6, Main.i
sw $s4, -36($fp)
sw $s5, -32($fp)
sw $s3, -40($fp)
sw $t5, Main.list

move $fp, $sp
addiu $sp, $sp, -12
jal Node.set_next

#-----------------------------------block id: 140009149636192
lw $t5, -44($fp)
lw $fp, ($sp)
addiu $sp, $sp, 4
lw $ra, ($sp)
addiu $sp, $sp, 4
move $t5, $v0

sw $t5, -44($fp)

#-----------------------------------block id: 140009149636264
label.4:

lw $t5, Main.list
lw $s6, Main.i
lw $s5, -48($fp)
sll $t7, $s6, 2
add $t8, $t5, $t7
lw $s5, 0($t8)

addiu $sp, $sp, -4
sw $s5, ($sp)

sw $s6, Main.i
sw $s5, -48($fp)
sw $t5, Main.list

move $fp, $sp
addiu $sp, $sp, -8
jal Node.print_data

#-----------------------------------block id: 140009149649840
lw $t5, -52($fp)
lw $fp, ($sp)
addiu $sp, $sp, 4
lw $ra, ($sp)
addiu $sp, $sp, 4
move $t5, $v0

lw $s6, Main.i
move $t9, $ra
move $a0,$s6
jal print_int
move $ra, $t9

lw $s5, -12($fp)
addi $s5, $s6, 1

move $s6, $s5

sw $s6, Main.i
sw $t5, -52($fp)
sw $s5, -12($fp)

j label.5

#-----------------------------------block id: 140009149649912
label.6:


jal exit_func

#-----------------------------------block id: 140009149636336
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
