.data
space: .asciiz " "
a : .word 0
c : .word 0
e : .word 0
d : .word 0
f : .word 0
.text
main:
lw $t5,a
li $t5, 2

lw $s6,c
li $s6, 3

sw $t5, a
sw $s6, c

bge $t5,$s6,L

#-----------------------------------block id: 139684614404720
lw $t5, a
lw $s6, c
mult $t5, $s6
mflo $t5

sw $t5, a
sw $s6, c

#-----------------------------------block id: 139684614405008
L:

lw $t5, c
lw $s6, a
sub $t5, $t5, $s6

move $a0,$t5
jal print_int

lw $s5,d
li $s5, 1

lw $s4,e
li $s4, 1

lw $s3, f
jal scan_int
move $s3,$v0

add $s3, $s3, $s5

add $s3, $s3, $s4

jal space_func

move $a0,$s3
jal print_int

sw $s6, a
sw $t5, c
sw $s4, e
sw $s5, d
sw $s3, f

#-----------------------------------block id: 139684614405080
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
