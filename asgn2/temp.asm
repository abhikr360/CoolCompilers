.data
i : .word 0
n : .word 0
f : .word 0
s : .word 0
cur : .word 0

.text
main:
lw $t5,i
li $t5, 2

lw $s6, n
jal scan_int
move $s6,$v0

lw $s5,f
li $s5, 1

lw $s4,s
li $s4, 1

lw $s3,cur
li $s3, 1

li $t7,2
sw $t5, i
sw $s4, s
sw $s5, f
sw $s3, cur
sw $s6, n

ble $s6,$t7,out

#-----------------------------------block id: 140141874082232
rep:

lw $t5, f
lw $s6,s
move $s6, $t5

lw $s5, cur
move $t5, $s5

add $s5, $t5, $s6

lw $s4, i
addi $s4, $s4, 1

lw $s3, n
sw $s4, i
sw $s6, s
sw $t5, f
sw $s5, cur
sw $s3, n

blt $s4,$s3,rep

#-----------------------------------block id: 140141874082448
out:

lw $t5, cur
move $a0,$t5
jal print_int

sw $t5, cur

jr $ra

#-----------------------------------block id: 140141874082520
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

