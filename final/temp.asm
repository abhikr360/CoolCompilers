.data
space: .asciiz " "
str.2: .asciiz "extra"
str.1: .asciiz "file.txt"
Main.file_name : .word 0
Main.input_str : .word 0
Main.temp : .word 0
.text
main:

j CLASS.Main

#-----------------------------------block id: 140632559981344

jal exit_func

#-----------------------------------block id: 140632559981416
CLASS.Main:

lw $t5,Main.file_name
li $v0, 9
li $a0, 100
sll $a0, $a0, 2
syscall
move $t5, $v0

la $t5, str.1

lw $s6,Main.input_str
li $v0, 9
li $a0, 100
sll $a0, $a0, 2
syscall
move $s6, $v0

la $s6, str.2

lw $s5,Main.temp
li $v0, 9
li $a0, 100
sll $a0, $a0, 2
syscall
move $s5, $v0

sw $s5, Main.temp
sw $s6, Main.input_str
sw $t5, Main.file_name

move $fp, $sp
addiu $sp, $sp, -4
jal Main.main

#-----------------------------------block id: 140632559981488

jal exit_func

#-----------------------------------block id: 140632559981632
Main.main:

lw $t5, Main.file_name
lw $s6,Main.temp
move $t9, $ra
li $a1, 0
move $a0,$t5
jal file_open
move $a0, $t8
move $a1, $s6
jal file_read
jal file_close
move $ra, $t9

lw $s5, Main.input_str
move $t6, $ra
move $a0,$s6
move $a1, $s5
jal strcat
move $ra, $t6

move $t9, $ra
li $a1, 1
move $a0,$t5
jal file_open
move $a0, $t8
move $a1, $s6
jal file_write
jal file_close
move $ra, $t9

lw $t1, -4($fp)
li $v0, 9
li $a0, 100
sll $a0, $a0, 2
syscall
move $t1, $v0

move $t9, $ra
li $a1, 0
move $a0,$t5
jal file_open
move $a0, $t8
move $a1, $t1
jal file_read
jal file_close
move $ra, $t9

move $t6, $ra
move $a0,$t1
move $a1, $s5
jal strcat
move $ra, $t6

move $t9, $ra
li $a1, 1
move $a0,$t5
jal file_open
move $a0, $t8
move $a1, $t1
jal file_write
jal file_close
move $ra, $t9

sw $s6, Main.temp
sw $s5, Main.input_str
sw $t1, -4($fp)
sw $t5, Main.file_name

jal exit_func

#-----------------------------------block id: 140632559981560
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
print_string:
li $v0,4
syscall
jr $ra
scan_string:
li $v0,8
syscall
jr $ra
file_open:
li $v0, 13
li $a2, 0
syscall
move $t8, $v0
jr $ra
file_read:
li $v0, 14
move $a0, $t8
li $a2, 100
syscall
jr $ra
file_close:
li $v0, 16
move $a0, $t8
syscall
jr $ra
file_write:
li $v0, 15
move $a0, $t8
move $t6, $ra
jal strlen
move $ra, $t6
syscall
jr $ra
strlen:
move $a3, $a1
li $a2, 0
j strlen.test
strlen.loop:
addi $a3, $a3, 1
addi $a2, $a2, 1
strlen.test:
lb $t7, 0($a3)
bnez $t7, strlen.loop
jr $ra
strcpy:
move $t9, $a0
move $t8, $a1
strcpy.loop:
lb $t7, 0($t9)
beq $t7, $zero, strcpy.end
addiu $t9, $t9, 1
sb $t7, 0($t8)
addiu $t8, $t8, 1
b strcpy.loop
strcpy.end:
sb $zero, 0($t8)
move $v0, $t9
jr $ra
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
