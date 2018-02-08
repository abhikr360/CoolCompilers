.data

i : .word 0
arr : .space 40
sum : .word 0
temp : .word 0

.text

main:
li $t5, 0
sw $t5, i
#------------new block started---------------------
LOOP:

sw $t5, i
#------------new block started---------------------
li $t7,10
bge $t5,$t7,LOOPEXIT

lw $t5, i
la $s6, arr
add $t5, $t5, $t5
add $t5, $t5, $t5
add $t5, $t5, $s6
sw $t5, 0($t5)
sw $t5, i
sw $s6, arr
#------------new block started---------------------
li $t7,10
blt $t5,$t7,LOOP

LOOP_EXIT:

sw $t5, i
#------------new block started---------------------
li $t5, 0

SUM_LOOP:

sw $t5, sum
#------------new block started---------------------
li $t7,10
bge $t5,$t7,SUM_LOOPEXIT

la $s6, arr
add $t5, $t5, $t5
add $t5, $t5, $t5
add $t5, $t5, $s6
lw $s5, 0($t5)
lw $s4, sum
add $s4, $s4, $s5

sw $t5, i
sw $s6, arr
sw $s4, sum
sw $s5, temp
#------------new block started---------------------
li $t7,10
blt $t5,$t7,SUM_LOOP

SUM_LOOPEXIT:

sw $t5, i
#------------new block started---------------------

lw $a0, sum
li $v0, 1
syscall

.end main