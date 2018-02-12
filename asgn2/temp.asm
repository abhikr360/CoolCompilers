.data
space: .asciiz " "
a : .word 0
c : .word 0
.text
main:
lw $t5,a
li $t5, 2

sw $t5, a

#-----------------------------------block id: 140234410926736
L:

lw $t5, a
addi $t5, $t5, 1

li $t7,9
sw $t5, a

ble $t5,$t7,L

#-----------------------------------block id: 140234410926952

jal func

#-----------------------------------block id: 140234410927024
lw $t5,c
li $t5, -1

lw $s6, a
add $s6, $s6, $t5

move $a0,$s6
jal print_int

jal space_func

sw $s6, a
sw $t5, c

jal exit_func

#-----------------------------------block id: 140234410927096
func:
add $sp, $sp, -4
sw $ra, ($sp)

lw $t5, a
li $t7, 2
div $t5, $t7
mflo $t5

lw $ra, ($sp)
add $sp, $sp, 4
sw $t5, a

jr $ra

#-----------------------------------block id: 140234410927168
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
