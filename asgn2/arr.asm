.data
i : .word 0
arr : .space 40
sum : .word 0
temp : .word 0
.text 

main:
lw $t5,i
li $t5, 0

sw $t5, i

#-----------------------------------block id: 139915193114848
LOOP:

lw $t5, i
li $t7,10
sw $t5, i

bge $t5,$t7,LOOPEXIT

#-----------------------------------block id: 139915193115064
lw $t5, i
la $s6, arr
sll $t7, $t5, 2
add $t8, $s6, $t7
sw $t5, 0($t8)
addi $t5, $t5, 1

li $t7,10
sw $t5, i

blt $t5,$t7,LOOP

#-----------------------------------block id: 139915193115136
LOOPEXIT:

lw $t5,sum
li $t5, 0

lw $s5,i
li $s5, 0

sw $s5, i
sw $t5, sum

#-----------------------------------block id: 139915193115280
SUM_LOOP:

lw $t5, i
li $t7,10
sw $t5, i

bge $t5,$t7,SUM_LOOPEXIT

#-----------------------------------block id: 139915193115208
lw $t5, i
lw $s5,temp
sll $t7, $t5, 2
add $t8, $s6, $t7
lw $s5, 0($t8)
lw $s4, sum
add $s4, $s4, $s5

addi $t5, $t5, 1

li $t7,10
sw $t5, i
sw $s4, sum
sw $s5, temp

blt $t5,$t7,SUM_LOOP

#-----------------------------------block id: 139915193115352
SUM_LOOPEXIT:

lw $a0,sum
li $v0,1
syscall

li $v0,10
syscall
.end main