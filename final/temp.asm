.data
space: .asciiz " "
Main.n : .word 0
Main.m : .word 0
Main.t.14 : .word 0
Main.arith : .word 0
.text
main:

j CLASS.Main

#-----------------------------------block id: 140335880313456

jal exit_func

#-----------------------------------block id: 140335880030616
CLASS.Arith:


#-----------------------------------block id: 140335880030688
Arith.mul:

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

sw $s5, -4($fp)
sw $s6, -8($fp)
sw $t5, -12($fp)

#-----------------------------------block id: 140335880030832
LET_BEGIN_Arith.mul.LET_1:

lw $t5, -20($fp)
li $t5, 0

lw $s6, -16($fp)
li $s6, 0

sw $t5, -20($fp)
sw $s6, -16($fp)

#-----------------------------------block id: 140335880030760
label.1:

lw $t5, -16($fp)
lw $s6, -8($fp)
lw $s5, -24($fp)
slt $s5, $t5, $s6

li $t7,0
sw $s6, -8($fp)
sw $s5, -24($fp)
sw $t5, -16($fp)

beq $s5,$t7,label.2

#-----------------------------------block id: 140335880030904
lw $t5, -20($fp)
lw $s6, -4($fp)
lw $s5, -32($fp)
add $s5, $t5, $s6

move $t5, $s5

lw $s4, -16($fp)
lw $s3, -28($fp)
addi $s3, $s4, 1

move $s4, $s3

sw $s6, -4($fp)
sw $t5, -20($fp)
sw $s3, -28($fp)
sw $s5, -32($fp)
sw $s4, -16($fp)

j label.1

#-----------------------------------block id: 140335880092416
label.2:

lw $t5, -20($fp)
sw $t5, -20($fp)

move $v0, $t5

#-----------------------------------block id: 140335880092488
LET_OVER_LET_1:

addiu $sp, $sp, 4

addiu $sp, $sp, 4

addiu $sp, $sp, 4

addiu $sp, $sp, 32

jr $ra

#-----------------------------------block id: 140335880092560
Arith.add:

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

sw $s6, -8($fp)
sw $s5, -4($fp)
sw $t5, -12($fp)

#-----------------------------------block id: 140335880092632
LET_BEGIN_Arith.add.LET_2:

lw $t5, -4($fp)
lw $s6, -20($fp)
move $s6, $t5

lw $s5, -16($fp)
li $s5, 0

sw $t5, -4($fp)
sw $s5, -16($fp)
sw $s6, -20($fp)

#-----------------------------------block id: 140335880092704
label.3:

lw $t5, -16($fp)
lw $s6, -8($fp)
lw $s5, -24($fp)
slt $s5, $t5, $s6

li $t7,0
sw $s6, -8($fp)
sw $t5, -16($fp)
sw $s5, -24($fp)

beq $s5,$t7,label.4

#-----------------------------------block id: 140335880092776
lw $t5, -20($fp)
lw $s6, -32($fp)
addi $s6, $t5, 1

move $t5, $s6

lw $s5, -16($fp)
lw $s4, -28($fp)
addi $s4, $s5, 1

move $s5, $s4

sw $s5, -16($fp)
sw $t5, -20($fp)
sw $s4, -28($fp)
sw $s6, -32($fp)

j label.3

#-----------------------------------block id: 140335880092848
label.4:

lw $t5, -20($fp)
sw $t5, -20($fp)

move $v0, $t5

#-----------------------------------block id: 140335880092920
LET_OVER_LET_2:

addiu $sp, $sp, 4

addiu $sp, $sp, 4

addiu $sp, $sp, 4

addiu $sp, $sp, 32

jr $ra

#-----------------------------------block id: 140335880092992
Arith.power:

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

sw $t5, -12($fp)
sw $s6, -8($fp)
sw $s5, -4($fp)

#-----------------------------------block id: 140335880093064
LET_BEGIN_Arith.power.LET_3:

lw $t5, -20($fp)
li $t5, 1

lw $s6, -16($fp)
li $s6, 0

sw $s6, -16($fp)
sw $t5, -20($fp)

#-----------------------------------block id: 140335880093136
label.5:

lw $t5, -16($fp)
lw $s6, -8($fp)
lw $s5, -24($fp)
slt $s5, $t5, $s6

li $t7,0
sw $t5, -16($fp)
sw $s6, -8($fp)
sw $s5, -24($fp)

beq $s5,$t7,label.6

#-----------------------------------block id: 140335880093208
lw $t5, -20($fp)
lw $s6, -4($fp)
lw $s5, -32($fp)
mult $t5, $s6
mflo $s5

move $t5, $s5

lw $s4, -16($fp)
lw $s3, -28($fp)
addi $s3, $s4, 1

move $s4, $s3

sw $s4, -16($fp)
sw $s5, -32($fp)
sw $s3, -28($fp)
sw $s6, -4($fp)
sw $t5, -20($fp)

j label.5

#-----------------------------------block id: 140335880093280
label.6:

lw $t5, -20($fp)
sw $t5, -20($fp)

move $v0, $t5

#-----------------------------------block id: 140335880093352
LET_OVER_LET_3:

addiu $sp, $sp, 4

addiu $sp, $sp, 4

addiu $sp, $sp, 4

addiu $sp, $sp, 32

jr $ra

#-----------------------------------block id: 140335880093424
Arith.log:

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

sw $s6, -8($fp)
sw $t5, -12($fp)
sw $s5, -4($fp)

#-----------------------------------block id: 140335880093496
LET_BEGIN_Arith.log.LET_4:

lw $t5, -20($fp)
li $t5, 0

lw $s6, -16($fp)
li $s6, 0

sw $s6, -16($fp)
sw $t5, -20($fp)

#-----------------------------------block id: 140335880093568
label.9:

lw $t5, -20($fp)
lw $s6, -8($fp)
lw $s5, -24($fp)
div $t5, $s6
mflo $s5

lw $s4, -28($fp)
li $t9, 1
seq $s4, $s5, $t9

li $t7,0
sw $t5, -20($fp)
sw $s6, -8($fp)
sw $s4, -28($fp)
sw $s5, -24($fp)

beq $s4,$t7,label.10

#-----------------------------------block id: 140335880093640
lw $t5, -20($fp)
lw $s6, -8($fp)
lw $s5, -36($fp)
div $t5, $s6
mflo $s5

move $t5, $s5

lw $s4, -16($fp)
lw $s3, -32($fp)
addi $s3, $s4, 1

move $s4, $s3

sw $s4, -16($fp)
sw $t5, -20($fp)
sw $s6, -8($fp)
sw $s5, -36($fp)
sw $s3, -32($fp)

j label.9

#-----------------------------------block id: 140335880110160
label.10:

lw $t5, -20($fp)
sw $t5, -20($fp)

move $v0, $t5

#-----------------------------------block id: 140335880110232
LET_OVER_LET_4:

addiu $sp, $sp, 4

addiu $sp, $sp, 4

addiu $sp, $sp, 4

addiu $sp, $sp, 36

jr $ra

#-----------------------------------block id: 140335880110304
CLASS.Main:

lw $t5,Main.n
li $t5, 10000

lw $s6,Main.m
li $s6, 10

lw $s5,Main.t.14
li $v0, 9
li $a0, 0
sll $a0, $a0, 2
syscall
move $s5, $v0

lw $s4,Main.arith
move $s4, $s5

sw $t5, Main.n
sw $s6, Main.m
sw $s4, Main.arith
sw $s5, Main.t.14

move $fp, $sp
addiu $sp, $sp, -8
jal Main.main

#-----------------------------------block id: 140335880110376

jal exit_func

#-----------------------------------block id: 140335880110448
Main.main:

addiu $sp, $sp, -4
sw $ra, ($sp)
addiu $sp, $sp, -4
sw $fp, ($sp)

lw $t5, Main.n
addiu $sp, $sp, -4
sw $t5, ($sp)

lw $s6, Main.m
addiu $sp, $sp, -4
sw $s6, ($sp)

lw $s5, Main.arith
addiu $sp, $sp, -4
sw $s5, ($sp)

sw $t5, Main.n
sw $s6, Main.m
sw $s5, Main.arith

move $fp, $sp
addiu $sp, $sp, -32
jal Arith.add

#-----------------------------------block id: 140335880110520
lw $t5, -4($fp)
lw $fp, ($sp)
addiu $sp, $sp, 4
lw $ra, ($sp)
addiu $sp, $sp, 4
move $t5, $v0

move $a0,$t5
jal print_int

sw $t5, -4($fp)

#-----------------------------------block id: 140335880110592
LET_BEGIN_Main.main.LET_5:

lw $t5, -8($fp)
jal scan_int
move $t5,$v0

move $a0,$t5
jal print_int

sw $t5, -8($fp)

#-----------------------------------block id: 140335880110664
LET_OVER_LET_5:


jal exit_func

#-----------------------------------block id: 140335880110736
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
