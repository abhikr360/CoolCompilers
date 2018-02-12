.data
space: .asciiz " "
n : .word 0
ans : .word 0
.text
main:
lw $t5, n
jal scan_int
move $t5,$v0

lw $s6,ans
li $s6, 1

sw $t5, n
sw $s6, ans

jal factorial

#-----------------------------------block id: 139740808190792
lw $t5, ans
move $a0,$t5
jal print_int

sw $t5, ans

jal exit_func

#-----------------------------------block id: 139740808190936
factorial:
add $sp, $sp, -4
sw $ra, ($sp)

lw $t5, n
li $t7,1
sw $t5, n

ble $t5,$t7,ret

#-----------------------------------block id: 139740808191008
lw $t5, n
addi $t5, $t5, -1

sw $t5, n

jal factorial

#-----------------------------------block id: 139740808191152
lw $t5, n
addi $t5, $t5, 1

lw $s6, ans
mult $s6, $t5
mflo $s6

sw $t5, n
sw $s6, ans

#-----------------------------------block id: 139740808191080
ret:

lw $ra, ($sp)
add $sp, $sp, 4

jr $ra

#-----------------------------------block id: 139740808191224
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
