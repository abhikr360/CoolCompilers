.data
space: .asciiz " "
i : .word 0
jaj : .word 0
array : .space 12
rev_array : .space 12
t : .word 0
.text
main:
lw $t5,i
li $t5, 0

sw $t5, i

#-----------------------------------block id: 140461103215248
scan:

la $t5, array
lw $s6, i
jal scan_int
sll $t7, $s6, 2
add $t8, $t5, $t7
sw $v0,0($t8)

addi $s6, $s6, 1

li $t7,3
sw $s6, i

blt $s6,$t7,scan

#-----------------------------------block id: 140461103215464
lw $t5,i
li $t5, 0

lw $s6,jaj
li $s6, 2

sw $t5, i
sw $s6, jaj

#-----------------------------------block id: 140461103215536
rev:

la $t5, array
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

li $t7,3
sw $s6, i
sw $s4, jaj
sw $s5, t

blt $s6,$t7,rev

#-----------------------------------block id: 140461103215608
lw $t5,i
li $t5, 0

sw $t5, i

#-----------------------------------block id: 140461103215680
print:

la $t5, rev_array
lw $s6, i
sll $t7, $s6, 2
add $t8, $t5, $t7
lw $a0,0($t8)
jal print_int

jal space_func

addi $s6, $s6, 1

li $t7,3
sw $s6, i

blt $s6,$t7,print

#-----------------------------------block id: 140461103215752
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
