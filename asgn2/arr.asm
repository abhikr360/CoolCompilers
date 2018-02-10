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

#-----------------------------------block id: 140112357704048
LOOP:

lw $t5, i
li $t7,3
sw $t5, i

bge $t5,$t7,LOOPEXIT

#-----------------------------------block id: 140112357704264
lw $t5, i
la $s6, arr
sll $t7, $t5, 2
add $t8, $s6, $t7
sw $t5, 0($t8)
addi $t5, $t5, 1

li $t7,3
sw $t5, i

blt $t5,$t7,LOOP

#-----------------------------------block id: 140112357704336
LOOPEXIT:

lw $t5,sum
li $t5, 0

lw $s5,i
li $s5, 0

sw $s5, i
sw $t5, sum

#-----------------------------------block id: 140112357704408
SUM_LOOP:

lw $t5, i
li $t7,3
sw $t5, i

bge $t5,$t7,SUM_LOOPEXIT

#-----------------------------------block id: 140112357704480
lw $t5, i
lw $s5,temp
sll $t7, $t5, 2
add $t8, $s6, $t7
lw $s5, 0($t8)
lw $s4, sum
add $s4, $s4, $s5

sll $t7, $0, 2
add $t8, $s6, $t7
lw $a0,0($t8)
jal print_int

addi $t5, $t5, 1

li $t7,3
sw $t5, i
sw $s4, sum
sw $s5, temp

blt $t5,$t7,SUM_LOOP

#-----------------------------------block id: 140112357704552
SUM_LOOPEXIT:


#-----------------------------------block id: 140112357705776
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

