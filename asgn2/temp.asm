.data
i : .word 0
jaj : .word 0
array : .space 12
rev_array : .space 12
t : .word 0
.text
main:
lw $s0,i
li $s0, 0

sw $s0, i

#-----------------------------------block id: 139956143753768
scan:

la $s0, array
lw $t2, i
jal scan_int
sll $t7, $t2, 2
add $t8, $s0, $t7
sw $v0,0($t8)

addi $t2, $t2, 1

li $t7,3
sw $t2, i

blt $t2,$t7,scan

#-----------------------------------block id: 139956143753984
lw $t2,i
li $t2, 0

lw $t0,jaj
li $t0, 2

sw $t2, i
sw $t0, jaj

#-----------------------------------block id: 139956143754056
rev:

lw $t2, i
lw $t0,t
sll $t7, $t2, 2
add $t8, $s0, $t7
lw $t0, 0($t8)

lw $t1, jaj
sw $s0, array
la $s0, rev_array
sll $t7, $t1, 2
add $t8, $s0, $t7
sw $t0, 0($t8)
addi $t2, $t2, 1

addi $t1, $t1, -1

li $t7,3
sw $t2, i
sw $t1, jaj
sw $t0, t

blt $t2,$t7,rev

#-----------------------------------block id: 139956143754200
lw $t2,i
li $t2, 0

sw $t2, i

#-----------------------------------block id: 139956143754128
print:

lw $t2, i
sll $t7, $t2, 2
add $t8, $s0, $t7
lw $a0,0($t8)
jal print_int

addi $t2, $t2, 1

li $t7,3
sw $t2, i

blt $t2,$t7,print

#-----------------------------------block id: 139956143754272
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
