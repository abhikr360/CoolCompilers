.data
space: .asciiz " "
str.1: .asciiz "\n"
Main.n : .word 0
Main.i : .word 0
Main.head : .word 0
Main.temp : .word 0
Main.arr : .word 0
.text
main:

j CLASS.Main

#-----------------------------------block id: 140116755316392

jal exit_func

#-----------------------------------block id: 140116755039440
CLASS.Node:


#-----------------------------------block id: 140116755039512
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

sw $s6, -8($fp)
sw $t5, -4($fp)

li $v0, 1

#-----------------------------------block id: 140116755039656
addiu $sp, $sp, 4

addiu $sp, $sp, 4

addiu $sp, $sp, 8

jr $ra

#-----------------------------------block id: 140116755039584
Node.set_left:

lw $t5, -8($fp)
lw $t7, 0($fp)
sw $t7, -4($fp)
move $t5, $t7

lw $s6, -4($fp)
lw $t7, 4($fp)
sw $t7, -8($fp)
move $s6, $t7

li $t7, 1
sll $t7, $t7, 2
add $t8, $t5,$t7
sw $s6, 0($t8)

sw $t5, -4($fp)
sw $s6, -8($fp)

li $v0, 1

#-----------------------------------block id: 140116755039728
addiu $sp, $sp, 4

addiu $sp, $sp, 4

addiu $sp, $sp, 8

jr $ra

#-----------------------------------block id: 140116755112304
Node.set_right:

lw $t5, -8($fp)
lw $t7, 0($fp)
sw $t7, -4($fp)
move $t5, $t7

lw $s6, -4($fp)
lw $t7, 4($fp)
sw $t7, -8($fp)
move $s6, $t7

li $t7, 2
sll $t7, $t7, 2
add $t8, $t5,$t7
sw $s6, 0($t8)

sw $s6, -8($fp)
sw $t5, -4($fp)

li $v0, 1

#-----------------------------------block id: 140116755112376
addiu $sp, $sp, 4

addiu $sp, $sp, 4

addiu $sp, $sp, 8

jr $ra

#-----------------------------------block id: 140116755112448
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

move $t9, $ra
la $a0,str.1
jal print_string
move $ra, $t9

addiu $sp, $sp, 4

addiu $sp, $sp, 8
sw $t5, -4($fp)
sw $s6, -8($fp)

jr $ra

#-----------------------------------block id: 140116755112520
CLASS.Main:

lw $t5, Main.arr
li $v0, 9
li $a0, 2
sll $a0, $a0, 2
syscall
move $t5, $v0

sw $t5, Main.arr

move $fp, $sp
addiu $sp, $sp, -104
jal Main.main

#-----------------------------------block id: 140116755112592

jal exit_func

#-----------------------------------block id: 140116755112664
Main.printTree:

lw $t5, -4($fp)
lw $t7, 0($fp)
sw $t7, -4($fp)
move $t5, $t7

lw $s6, -8($fp)
li $t9, 0
seq $s6, $t5, $t9

li $t7,0
sw $t5, -4($fp)
sw $s6, -8($fp)

beq $s6,$t7,label.1

#-----------------------------------block id: 140116755112736
lw $t5, -12($fp)
li $t5, 0

sw $t5, -12($fp)

j label.2

#-----------------------------------block id: 140116755112808
label.1:

lw $t5, -12($fp)
li $t5, 1

sw $t5, -12($fp)

#-----------------------------------block id: 140116755112880
label.2:

lw $t5, -12($fp)
li $t7,0
sw $t5, -12($fp)

bgt $t5,$t7,label.3

#-----------------------------------block id: 140116755112952

j label.4

#-----------------------------------block id: 140116755113024
label.3:

lw $t5, -4($fp)
lw $s6, -16($fp)
li $t7, 1
sll $t8, $t7, 2
add $t8, $t5,$t8
lw $s6, 0($t8)

addiu $sp, $sp, -4
sw $ra, ($sp)
addiu $sp, $sp, -4
sw $fp, ($sp)

addiu $sp, $sp, -4
sw $s6, ($sp)

sw $t5, -4($fp)
sw $s6, -16($fp)

move $fp, $sp
addiu $sp, $sp, -32
jal Main.printTree

#-----------------------------------block id: 140116755113096
lw $t5, -20($fp)
lw $fp, ($sp)
addiu $sp, $sp, 4
lw $ra, ($sp)
addiu $sp, $sp, 4
move $t5, $v0

addiu $sp, $sp, -4
sw $ra, ($sp)
addiu $sp, $sp, -4
sw $fp, ($sp)

lw $s6, -4($fp)
addiu $sp, $sp, -4
sw $s6, ($sp)

sw $s6, -4($fp)
sw $t5, -20($fp)

move $fp, $sp
addiu $sp, $sp, -8
jal Node.print_data

#-----------------------------------block id: 140116755113168
lw $t5, -24($fp)
lw $fp, ($sp)
addiu $sp, $sp, 4
lw $ra, ($sp)
addiu $sp, $sp, 4
move $t5, $v0

lw $s6, -4($fp)
lw $s5, -28($fp)
li $t7, 2
sll $t8, $t7, 2
add $t8, $s6,$t8
lw $s5, 0($t8)

addiu $sp, $sp, -4
sw $ra, ($sp)
addiu $sp, $sp, -4
sw $fp, ($sp)

addiu $sp, $sp, -4
sw $s5, ($sp)

sw $s6, -4($fp)
sw $t5, -24($fp)
sw $s5, -28($fp)

move $fp, $sp
addiu $sp, $sp, -32
jal Main.printTree

#-----------------------------------block id: 140116755113240
lw $t5, -32($fp)
lw $fp, ($sp)
addiu $sp, $sp, 4
lw $ra, ($sp)
addiu $sp, $sp, 4
move $t5, $v0

sw $t5, -32($fp)

#-----------------------------------block id: 140116755113312
label.4:

addiu $sp, $sp, 4

addiu $sp, $sp, 32

jr $ra

#-----------------------------------block id: 140116755113384
Main.main:

lw $t5,Main.n
li $t5, 10

lw $s6,Main.i
li $s6, 1

lw $s5, -4($fp)
li $v0, 9
li $a0, 12
sll $a0, $a0, 2
syscall
move $s5, $v0

lw $s4, Main.arr
li $t7, 0
sll $t7, $t7, 2
add $t8, $s4,$t7
sw $s5, 0($t8)

lw $s3, -8($fp)
li $t7, 0
sll $t8, $t7, 2
add $t8, $s4,$t8
lw $s3, 0($t8)

addiu $sp, $sp, -4
sw $ra, ($sp)
addiu $sp, $sp, -4
sw $fp, ($sp)

addiu $sp, $sp, -4
li $t7, 5
sw $t7, ($sp)

addiu $sp, $sp, -4
sw $s3, ($sp)

sw $t5, Main.n
sw $s6, Main.i
sw $s4, Main.arr
sw $s3, -8($fp)
sw $s5, -4($fp)

move $fp, $sp
addiu $sp, $sp, -8
jal Node.set_data

#-----------------------------------block id: 140116755113456
lw $t5, -12($fp)
lw $fp, ($sp)
addiu $sp, $sp, 4
lw $ra, ($sp)
addiu $sp, $sp, 4
move $t5, $v0

lw $s6, -16($fp)
li $v0, 9
li $a0, 12
sll $a0, $a0, 2
syscall
move $s6, $v0

lw $s5, Main.arr
li $t7, 1
sll $t7, $t7, 2
add $t8, $s5,$t7
sw $s6, 0($t8)

lw $s4, -20($fp)
li $t7, 1
sll $t8, $t7, 2
add $t8, $s5,$t8
lw $s4, 0($t8)

addiu $sp, $sp, -4
sw $ra, ($sp)
addiu $sp, $sp, -4
sw $fp, ($sp)

addiu $sp, $sp, -4
li $t7, 12
sw $t7, ($sp)

addiu $sp, $sp, -4
sw $s4, ($sp)

sw $s5, Main.arr
sw $t5, -12($fp)
sw $s4, -20($fp)
sw $s6, -16($fp)

move $fp, $sp
addiu $sp, $sp, -8
jal Node.set_data

#-----------------------------------block id: 140116755113528
lw $t5, -24($fp)
lw $fp, ($sp)
addiu $sp, $sp, 4
lw $ra, ($sp)
addiu $sp, $sp, 4
move $t5, $v0

lw $s6, -28($fp)
li $v0, 9
li $a0, 12
sll $a0, $a0, 2
syscall
move $s6, $v0

lw $s5,Main.temp
move $s5, $s6

addiu $sp, $sp, -4
sw $ra, ($sp)
addiu $sp, $sp, -4
sw $fp, ($sp)

addiu $sp, $sp, -4
li $t7, 13
sw $t7, ($sp)

addiu $sp, $sp, -4
sw $s5, ($sp)

sw $t5, -24($fp)
sw $s5, Main.temp
sw $s6, -28($fp)

move $fp, $sp
addiu $sp, $sp, -8
jal Node.set_data

#-----------------------------------block id: 140116755113600
lw $t5, -32($fp)
lw $fp, ($sp)
addiu $sp, $sp, 4
lw $ra, ($sp)
addiu $sp, $sp, 4
move $t5, $v0

lw $s6, Main.arr
lw $s5, -36($fp)
li $t7, 0
sll $t8, $t7, 2
add $t8, $s6,$t8
lw $s5, 0($t8)

addiu $sp, $sp, -4
sw $ra, ($sp)
addiu $sp, $sp, -4
sw $fp, ($sp)

addiu $sp, $sp, -4
sw $s5, ($sp)

lw $s4, Main.temp
addiu $sp, $sp, -4
sw $s4, ($sp)

sw $s4, Main.temp
sw $s6, Main.arr
sw $s5, -36($fp)
sw $t5, -32($fp)

move $fp, $sp
addiu $sp, $sp, -8
jal Node.set_left

#-----------------------------------block id: 140116755113672
lw $t5, -40($fp)
lw $fp, ($sp)
addiu $sp, $sp, 4
lw $ra, ($sp)
addiu $sp, $sp, 4
move $t5, $v0

lw $s6, Main.arr
lw $s5, -44($fp)
li $t7, 1
sll $t8, $t7, 2
add $t8, $s6,$t8
lw $s5, 0($t8)

addiu $sp, $sp, -4
sw $ra, ($sp)
addiu $sp, $sp, -4
sw $fp, ($sp)

addiu $sp, $sp, -4
sw $s5, ($sp)

lw $s4, Main.temp
addiu $sp, $sp, -4
sw $s4, ($sp)

sw $s4, Main.temp
sw $s6, Main.arr
sw $s5, -44($fp)
sw $t5, -40($fp)

move $fp, $sp
addiu $sp, $sp, -8
jal Node.set_right

#-----------------------------------block id: 140116755113744
lw $t5, -48($fp)
lw $fp, ($sp)
addiu $sp, $sp, 4
lw $ra, ($sp)
addiu $sp, $sp, 4
move $t5, $v0

lw $s6, Main.temp
lw $s5,Main.head
move $s5, $s6

lw $s4, -52($fp)
li $v0, 9
li $a0, 12
sll $a0, $a0, 2
syscall
move $s4, $v0

move $s6, $s4

addiu $sp, $sp, -4
sw $ra, ($sp)
addiu $sp, $sp, -4
sw $fp, ($sp)

addiu $sp, $sp, -4
li $t7, 21
sw $t7, ($sp)

addiu $sp, $sp, -4
sw $s6, ($sp)

sw $t5, -48($fp)
sw $s4, -52($fp)
sw $s6, Main.temp
sw $s5, Main.head

move $fp, $sp
addiu $sp, $sp, -8
jal Node.set_data

#-----------------------------------block id: 140116755113816
lw $t5, -56($fp)
lw $fp, ($sp)
addiu $sp, $sp, 4
lw $ra, ($sp)
addiu $sp, $sp, 4
move $t5, $v0

lw $s6, Main.head
lw $s5, -60($fp)
li $t7, 1
sll $t8, $t7, 2
add $t8, $s6,$t8
lw $s5, 0($t8)

addiu $sp, $sp, -4
sw $ra, ($sp)
addiu $sp, $sp, -4
sw $fp, ($sp)

lw $s4, Main.temp
addiu $sp, $sp, -4
sw $s4, ($sp)

addiu $sp, $sp, -4
sw $s5, ($sp)

sw $t5, -56($fp)
sw $s5, -60($fp)
sw $s4, Main.temp
sw $s6, Main.head

move $fp, $sp
addiu $sp, $sp, -8
jal Node.set_left

#-----------------------------------block id: 140116755113888
lw $t5, -64($fp)
lw $fp, ($sp)
addiu $sp, $sp, 4
lw $ra, ($sp)
addiu $sp, $sp, 4
move $t5, $v0

lw $s6, -68($fp)
li $v0, 9
li $a0, 12
sll $a0, $a0, 2
syscall
move $s6, $v0

lw $s5,Main.temp
move $s5, $s6

addiu $sp, $sp, -4
sw $ra, ($sp)
addiu $sp, $sp, -4
sw $fp, ($sp)

addiu $sp, $sp, -4
li $t7, 33
sw $t7, ($sp)

addiu $sp, $sp, -4
sw $s5, ($sp)

sw $t5, -64($fp)
sw $s6, -68($fp)
sw $s5, Main.temp

move $fp, $sp
addiu $sp, $sp, -8
jal Node.set_data

#-----------------------------------block id: 140116755113960
lw $t5, -72($fp)
lw $fp, ($sp)
addiu $sp, $sp, 4
lw $ra, ($sp)
addiu $sp, $sp, 4
move $t5, $v0

lw $s6, Main.head
lw $s5, -76($fp)
li $t7, 1
sll $t8, $t7, 2
add $t8, $s6,$t8
lw $s5, 0($t8)

lw $s4, -80($fp)
li $t7, 1
sll $t8, $t7, 2
add $t8, $s5,$t8
lw $s4, 0($t8)

addiu $sp, $sp, -4
sw $ra, ($sp)
addiu $sp, $sp, -4
sw $fp, ($sp)

lw $s3, Main.temp
addiu $sp, $sp, -4
sw $s3, ($sp)

addiu $sp, $sp, -4
sw $s4, ($sp)

sw $t5, -72($fp)
sw $s4, -80($fp)
sw $s3, Main.temp
sw $s5, -76($fp)
sw $s6, Main.head

move $fp, $sp
addiu $sp, $sp, -8
jal Node.set_right

#-----------------------------------block id: 140116755114032
lw $t5, -84($fp)
lw $fp, ($sp)
addiu $sp, $sp, 4
lw $ra, ($sp)
addiu $sp, $sp, 4
move $t5, $v0

lw $s6, -88($fp)
li $v0, 9
li $a0, 12
sll $a0, $a0, 2
syscall
move $s6, $v0

lw $s5,Main.temp
move $s5, $s6

addiu $sp, $sp, -4
sw $ra, ($sp)
addiu $sp, $sp, -4
sw $fp, ($sp)

addiu $sp, $sp, -4
li $t7, 11
sw $t7, ($sp)

addiu $sp, $sp, -4
sw $s5, ($sp)

sw $t5, -84($fp)
sw $s5, Main.temp
sw $s6, -88($fp)

move $fp, $sp
addiu $sp, $sp, -8
jal Node.set_data

#-----------------------------------block id: 140116755114104
lw $t5, -92($fp)
lw $fp, ($sp)
addiu $sp, $sp, 4
lw $ra, ($sp)
addiu $sp, $sp, 4
move $t5, $v0

lw $s6, Main.head
lw $s5, -96($fp)
li $t7, 2
sll $t8, $t7, 2
add $t8, $s6,$t8
lw $s5, 0($t8)

addiu $sp, $sp, -4
sw $ra, ($sp)
addiu $sp, $sp, -4
sw $fp, ($sp)

lw $s4, Main.temp
addiu $sp, $sp, -4
sw $s4, ($sp)

addiu $sp, $sp, -4
sw $s5, ($sp)

sw $s4, Main.temp
sw $s5, -96($fp)
sw $t5, -92($fp)
sw $s6, Main.head

move $fp, $sp
addiu $sp, $sp, -8
jal Node.set_left

#-----------------------------------block id: 140116755114176
lw $t5, -100($fp)
lw $fp, ($sp)
addiu $sp, $sp, 4
lw $ra, ($sp)
addiu $sp, $sp, 4
move $t5, $v0

addiu $sp, $sp, -4
sw $ra, ($sp)
addiu $sp, $sp, -4
sw $fp, ($sp)

lw $s6, Main.head
addiu $sp, $sp, -4
sw $s6, ($sp)

sw $t5, -100($fp)
sw $s6, Main.head

move $fp, $sp
addiu $sp, $sp, -32
jal Main.printTree

#-----------------------------------block id: 140116755114248
lw $t5, -104($fp)
lw $fp, ($sp)
addiu $sp, $sp, 4
lw $ra, ($sp)
addiu $sp, $sp, 4
move $t5, $v0

sw $t5, -104($fp)

jal exit_func

#-----------------------------------block id: 140116755114320
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
