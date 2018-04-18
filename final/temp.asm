.data
space: .asciiz " "
Main.n : .word 0
Main.i : .word 0
Main.head : .word 0
Main.temp : .word 0
Main.fast : .word 0
Main.slow : .word 0
.text
main:

j CLASS.Main

#-----------------------------------block id: 140602152381184

jal exit_func

#-----------------------------------block id: 140602152353376
CLASS.Node:


#-----------------------------------block id: 140602152353160
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

sw $s6, -4($fp)
sw $t5, -8($fp)

li $v0, 1

#-----------------------------------block id: 140602152353016
addiu $sp, $sp, 4

addiu $sp, $sp, 4

addiu $sp, $sp, 8

jr $ra

#-----------------------------------block id: 140602152353232
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

sw $s5, -12($fp)
sw $s6, -4($fp)
sw $t5, -8($fp)

li $v0, 1

#-----------------------------------block id: 140602152353088
addiu $sp, $sp, 4

addiu $sp, $sp, 4

addiu $sp, $sp, 12

jr $ra

#-----------------------------------block id: 140602152352728
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

sw $t5, -4($fp)
sw $s6, -8($fp)

li $v0, 1

#-----------------------------------block id: 140602152352800
addiu $sp, $sp, 4

addiu $sp, $sp, 8

jr $ra

#-----------------------------------block id: 140602152378664
CLASS.Main:


move $fp, $sp
addiu $sp, $sp, -72
jal Main.main

#-----------------------------------block id: 140602152378736

jal exit_func

#-----------------------------------block id: 140602152352872
Main.main:

lw $t5,Main.n
li $t5, 20

lw $s6,Main.i
li $s6, 1

li $s6, 0

sw $t5, Main.n
sw $s6, Main.i

#-----------------------------------block id: 140602152352944
label.1:

lw $t5, Main.i
lw $s6, Main.n
lw $s5, -4($fp)
slt $s5, $t5, $s6

li $t7,0
sw $s6, Main.n
sw $t5, Main.i
sw $s5, -4($fp)

beq $s5,$t7,label.2

#-----------------------------------block id: 140602152352440
lw $t5, -12($fp)
li $v0, 9
li $a0, 8
sll $a0, $a0, 2
syscall
move $t5, $v0

lw $s6,Main.temp
move $s6, $t5

lw $s5, Main.i
lw $s4, -16($fp)
addi $s4, $s5, 5

addiu $sp, $sp, -4
sw $ra, ($sp)
addiu $sp, $sp, -4
sw $fp, ($sp)

addiu $sp, $sp, -4
sw $s4, ($sp)

addiu $sp, $sp, -4
sw $s6, ($sp)

sw $s6, Main.temp
sw $s5, Main.i
sw $s4, -16($fp)
sw $t5, -12($fp)

move $fp, $sp
addiu $sp, $sp, -8
jal Node.set_data

#-----------------------------------block id: 140602152352512
lw $t5, -20($fp)
lw $fp, ($sp)
addiu $sp, $sp, 4
lw $ra, ($sp)
addiu $sp, $sp, 4
move $t5, $v0

lw $s6, Main.head
lw $s5,Main.temp
li $t7, 1
sll $t7, $t7, 2
add $t8, $s5,$t7
sw $s6, 0($t8)

move $s6, $s5

lw $s4, Main.i
lw $s3, -8($fp)
addi $s3, $s4, 1

move $s4, $s3

sw $s5, Main.temp
sw $s4, Main.i
sw $s3, -8($fp)
sw $t5, -20($fp)
sw $s6, Main.head

j label.1

#-----------------------------------block id: 140602152352296
label.2:

move $t9,$ra
jal space_func
move $ra,$t9

lw $t5, Main.head
lw $s6,Main.fast
move $s6, $t5

lw $s5,Main.slow
move $s5, $t5

lw $s4, -24($fp)
li $t7, 1
sll $t8, $t7, 2
add $t8, $s6,$t8
lw $s4, 0($t8)

lw $s3, -28($fp)
li $t7, 1
sll $t8, $t7, 2
add $t8, $s4,$t8
lw $s3, 0($t8)

addiu $sp, $sp, -4
sw $ra, ($sp)
addiu $sp, $sp, -4
sw $fp, ($sp)

addiu $sp, $sp, -4
sw $s3, ($sp)

sw $s5, Main.slow
sw $s6, Main.fast
sw $t5, Main.head
sw $s3, -28($fp)
sw $s4, -24($fp)

move $fp, $sp
addiu $sp, $sp, -8
jal Node.print_data

#-----------------------------------block id: 140602152352368
lw $t5, -32($fp)
lw $fp, ($sp)
addiu $sp, $sp, 4
lw $ra, ($sp)
addiu $sp, $sp, 4
move $t5, $v0

sw $t5, -32($fp)

#-----------------------------------block id: 140602152352008
label.9:

lw $t5, Main.fast
lw $s6, -36($fp)
li $t9, 0
seq $s6, $t5, $t9

li $t7,0
sw $s6, -36($fp)
sw $t5, Main.fast

beq $s6,$t7,label.3

#-----------------------------------block id: 140602152352080
lw $t5, -40($fp)
li $t5, 0

sw $t5, -40($fp)

j label.4

#-----------------------------------block id: 140602152351864
label.3:

lw $t5, -40($fp)
li $t5, 1

sw $t5, -40($fp)

#-----------------------------------block id: 140602152351936
label.4:

lw $t5, -40($fp)
li $t7,0
ble $t5,$t7,label.7

lw $s6, Main.fast
lw $s5, -44($fp)
li $t7, 1
sll $t8, $t7, 2
add $t8, $s6,$t8
lw $s5, 0($t8)

lw $s4, -48($fp)
li $t9, 0
seq $s4, $s5, $t9

li $t7,0
sw $s4, -48($fp)
sw $s5, -44($fp)
sw $t5, -40($fp)
sw $s6, Main.fast

beq $s4,$t7,label.5

#-----------------------------------block id: 140602152350496
lw $t5, -52($fp)
li $t5, 0

sw $t5, -52($fp)

j label.6

#-----------------------------------block id: 140602152351792
label.5:

lw $t5, -52($fp)
li $t5, 1

sw $t5, -52($fp)

#-----------------------------------block id: 140602152350424
label.6:

lw $t5, -52($fp)
li $t7,0
ble $t5,$t7,label.7

lw $s6, -56($fp)
li $s6, 1

sw $t5, -52($fp)
sw $s6, -56($fp)

j label.8

#-----------------------------------block id: 140602152350352
label.7:

lw $t5, -56($fp)
li $t5, 0

sw $t5, -56($fp)

#-----------------------------------block id: 140602152350208
label.8:

lw $t5, -56($fp)
li $t7,0
sw $t5, -56($fp)

beq $t5,$t7,label.10

#-----------------------------------block id: 140602152350280
lw $t5, Main.fast
lw $s6, -60($fp)
li $t7, 1
sll $t8, $t7, 2
add $t8, $t5,$t8
lw $s6, 0($t8)

lw $s5, -64($fp)
li $t7, 1
sll $t8, $t7, 2
add $t8, $s6,$t8
lw $s5, 0($t8)

move $t5, $s5

lw $s4, Main.slow
lw $s3, -68($fp)
li $t7, 1
sll $t8, $t7, 2
add $t8, $s4,$t8
lw $s3, 0($t8)

move $s4, $s3

sw $s6, -60($fp)
sw $s4, Main.slow
sw $t5, Main.fast
sw $s3, -68($fp)
sw $s5, -64($fp)

j label.9

#-----------------------------------block id: 140602152381256
label.10:

addiu $sp, $sp, -4
sw $ra, ($sp)
addiu $sp, $sp, -4
sw $fp, ($sp)

lw $t5, Main.slow
addiu $sp, $sp, -4
sw $t5, ($sp)

sw $t5, Main.slow

move $fp, $sp
addiu $sp, $sp, -8
jal Node.print_data

#-----------------------------------block id: 140602152381328
lw $t5, -72($fp)
lw $fp, ($sp)
addiu $sp, $sp, 4
lw $ra, ($sp)
addiu $sp, $sp, 4
move $t5, $v0

sw $t5, -72($fp)

jal exit_func

#-----------------------------------block id: 140602152124712
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
