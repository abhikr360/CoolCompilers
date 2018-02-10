.data
i : .word 0
jaj : .word 0
array : .space 28
rev_array : .space 28
t : .word 0

.text
main:
lw $t5,i
li $t5, 0

sw $t5, i

#-----------------------------------block id: 140041096524216
scan:

la $t5, array
lw $s6, i
jal scan_int
sll $t7, $s6, 2
add $t8, $t5, $t7
sw $v0,0($t8)

addi $s6, $s6, 1

li $t7,7
sw $s6, i

blt $s6,$t7,scan

#-----------------------------------block id: 140041096524432
lw $s6,i
li $s6, 0

lw $s5,jaj
li $s5, 6

sw $s6, i
sw $s5, jaj

#-----------------------------------block id: 140041096524504
rev:

lw $s6, i
lw $s5,t
sll $t7, $s6, 2
add $t8, $t5, $t7
lw $s5, 0($t8)
lw $s4, jaj
la $s3, rev_array
sll $t7, $s4, 2
add $t8, $s3, $t7
sw $s5, 0($t8)
addi $s6, $s6, 1

addi $s4, $s4, -1

li $t7,7
sw $s6, i
sw $s4, jaj
sw $s5, t

blt $s6,$t7,rev

#-----------------------------------block id: 140041096524576
lw $s6,i
li $s6, 0

sw $s6, i

#-----------------------------------block id: 140041096524648
print:

lw $s6, i
sll $t7, $s6, 2
add $t8, $s3, $t7
lw $a0,0($t8)
jal print_int

addi $s6, $s6, 1

li $t7,7
sw $s6, i

blt $s6,$t7,print

#-----------------------------------block id: 140041096524720

jr $ra

#-----------------------------------block id: 140041096526088
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

