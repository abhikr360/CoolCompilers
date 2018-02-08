.data
aalo : .word 0
bhalu : .word 0
C : .word 0
chor : .word 0
kachalu : .word 0
str : .asciiz "\nHello\n"

.text
main:
lw $t2,aalo
li $t2, 2

lw $t0,bhalu
li $t0, 3

sw $t2, aalo
sw $t0, bhalu

jal print_hello

#-----------------------------------block id: 140637126959400
lw $t2, aalo
lw $t0, bhalu
sw $t2, aalo
sw $t0, bhalu

blt $t2,$t0,L1

#-----------------------------------block id: 140637126959688

jal print_false

#-----------------------------------block id: 140637126959760
L1:

lw $t2, aalo
lw $t0, bhalu
lw $t1,kachalu
add $t1, $t2, $t0

sub $t2, $t2, $t2

sw $t1, kachalu
sw $t2, aalo
sw $t0, bhalu

jr $ra

#-----------------------------------block id: 140637126959832
print_hello:

lw $t2,C
li $t2, 70

la $a0,str
li $v0,4
syscall

sw $t2, C

jr $ra

#-----------------------------------block id: 140637126959904
print_false:

lw $t2,chor
li $t2, 4

sw $t2, chor

jr $ra

#-----------------------------------block id: 139640244974440

li $v0,10
syscall

la $a0,str
li $v0,4
syscall
