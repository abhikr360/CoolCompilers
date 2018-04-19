.data
space: .asciiz " "
Main.e : .word 0
Main.bar : .word 0
Main.c : .word 0
Main.d : .word 0
.text
main:

j CLASS.Main

#-----------------------------------block id: 140635593638976

jal exit_func

#-----------------------------------block id: 140635593639048
CLASS.Main:


move $fp, $sp
addiu $sp, $sp, -28
jal Main.main

#-----------------------------------block id: 140635593639120

jal exit_func

#-----------------------------------block id: 140635593639192
Main.main:

lw $t5, Main.c
lw $s6, -4($fp)
li $t7,0
sgt $s6, $t5, $t7

li $t7,0
ble $s6,$t7,label.5

lw $s5, Main.d
lw $t1, -8($fp)
li $t7,0
sgt $t1, $s5, $t7

li $t7,0
ble $t1,$t7,label.5

lw $s3, -12($fp)
li $s3, 1

sw $s6, -4($fp)
sw $s3, -12($fp)
sw $t1, -8($fp)
sw $s5, Main.d
sw $t5, Main.c

j label.6

#-----------------------------------block id: 140635593641136
label.5:

lw $t5, -12($fp)
li $t5, 0

sw $t5, -12($fp)

#-----------------------------------block id: 140635593641208
label.6:

lw $t5, -12($fp)
li $t7,0
sw $t5, -12($fp)

bgt $t5,$t7,label.9

#-----------------------------------block id: 140635593639264
lw $t5, Main.d
lw $s6, Main.e
lw $s5, -20($fp)
and $s5, $t5, $s6

li $t7,0
sw $s5, -20($fp)
sw $s6, Main.e
sw $t5, Main.d

bgt $s5,$t7,label.7

#-----------------------------------block id: 140635593639336
lw $t5, Main.d
lw $s6, -28($fp)
addi $s6, $t5, -1

move $t5, $s6

sw $s6, -28($fp)
sw $t5, Main.d

j label.8

#-----------------------------------block id: 140635593639408
label.7:

lw $t5, Main.e
lw $s6, -24($fp)
addi $s6, $t5, 1

move $t5, $s6

sw $s6, -24($fp)
sw $t5, Main.e

#-----------------------------------block id: 140635593639480
label.8:


j label.10

#-----------------------------------block id: 140635593639552
label.9:

lw $t5, Main.d
lw $s6, -16($fp)
addi $s6, $t5, 1

move $t5, $s6

sw $s6, -16($fp)
sw $t5, Main.d

#-----------------------------------block id: 140635593639624
label.10:


jal exit_func

#-----------------------------------block id: 140635593635888
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
