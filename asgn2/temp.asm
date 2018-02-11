.data
space: .asciiz " "
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

#-----------------------------------block id: 140197921004144
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

#-----------------------------------block id: 140197921004360
lw $s0,i
li $s0, 0

lw $t2,jaj
li $t2, 2

sw $s0, i
sw $t2, jaj

#-----------------------------------block id: 140197921004432
rev:

la $s0, array
lw $t2, i
lw $t0,t
sll $t7, $t2, 2
add $t8, $s0, $t7
lw $t0, 0($t8)

lw $t1, jaj
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

#-----------------------------------block id: 140197921004504
lw $s0,i
li $s0, 0

sw $s0, i

#-----------------------------------block id: 140197921004576
print:

la $s0, rev_array
lw $t2, i
sll $t7, $t2, 2
add $t8, $s0, $t7
lw $a0,0($t8)
jal print_int

jal space_func

addi $t2, $t2, 1

li $t7,3
sw $t2, i

blt $t2,$t7,print

#-----------------------------------block id: 140197921004648
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
