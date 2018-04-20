.data
str1: .asciiz "Hello "
str2: .asciiz "world!"
result: .space 200

.text

main:
# Copy first string to result buffer
la $a0, str1
la $a1, str2
jal strcat


la $a0, str1
li $v0, 4
syscall
li $v0, 10
syscall


strcat:
move $t9, $a0
move $t8, $a1

strcat.first:
lb $t7, 0($t9)
beqz $t7, strcat.second
addiu $t9, $t9 ,1
j strcat.first

strcat.second:
lb $t7, 0($t8)
sb $t7, 0($t9)

beqz $t7, strcat.end

addiu $t8, $t8, 1
addiu $t9, $t9, 1

j strcat.second

strcat.end:
sb $zero, 0($t9)

jr $ra












# Concatenate second string on result buffer
la $a0, str2
or $a1, $v0, $zero
jal strcopier

la $a0, result
li $v0, 4
syscall

li $v0, 10
syscall


# String copier function
strcopier:
or $t0, $a0, $zero # Source
or $t1, $a1, $zero # Destination

loop:
lb $t2, 0($t0)
beq $t2, $zero, end
addiu $t0, $t0, 1
sb $t2, 0($t1)
addiu $t1, $t1, 1
b loop

end:
or $v0, $t1, $zero # Return last position on result buffer
jr $ra