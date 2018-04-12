.data
space: .asciiz " "
a : .word 0
b_ : .word 0
t.1 : .word 0
t.2 : .word 0
t.3 : .word 0
t.4 : .word 0
t.5 : .word 0
t.6 : .word 0
t.7 : .word 0
t.8 : .word 0
t.9 : .word 0
t.10 : .word 0
t.11 : .word 0
t.12 : .word 0
t.13 : .word 0
t.14 : .word 0
t.15 : .word 0
t.16 : .word 0
.text
main:

jal THE_MAIN_CLASS

#-----------------------------------block id: 140491805884568

jal exit_func

#-----------------------------------block id: 140491805884712
THE_MAIN_CLASS:
add $sp, $sp, -4
sw $ra, ($sp)

lw $t5,b_
li $t5, 4

sw $t5, b_

#-----------------------------------block id: 140491805884784
Main.main:
add $sp, $sp, -4
sw $ra, ($sp)

lw $t5, b_
lw $s6,t.1


lw $s5,t.2


lw $s4,t.3
li $s4, 1

sw $s6, t.1
sw $s4, t.3
sw $s5, t.2
sw $t5, b_

j label.4

#-----------------------------------block id: 140491805884856
label.3:

lw $t5,t.3
li $t5, 0

sw $t5, t.3

#-----------------------------------block id: 140491805884928
label.4:

lw $t5, t.3
li $t7,0
sw $t5, t.3

bne $t5,$t7,label.5

#-----------------------------------block id: 140491805885000
lw $t5,t.4
li $t5, -1

lw $s6, b_
lw $s5,t.5

li $t7,0
sw $t5, t.4
sw $s5, t.5
sw $s6, b_

bne $s5,$t7,label.5

#-----------------------------------block id: 140491805909936
lw $t5,t.6
li $t5, 0

sw $t5, t.6

j label.6

#-----------------------------------block id: 140491805910008
label.5:

lw $t5,t.6
li $t5, 1

sw $t5, t.6

#-----------------------------------block id: 140491805910080
label.6:

lw $t5, t.6

lw $s6, b_
lw $s5,t.7

li $t7,0
sw $s5, t.7
sw $t5, t.6
sw $s6, b_

beq $s5,$t7,label.9

#-----------------------------------block id: 140491805910152
lw $t5,t.8
li $t5, 0

sw $t5, t.8

j label.10

#-----------------------------------block id: 140491805910224
label.9:

lw $t5,t.8
li $t5, 1

sw $t5, t.8

#-----------------------------------block id: 140491805910296
label.10:

lw $t5, t.8
li $t7,0
sw $t5, t.8

bne $t5,$t7,label.17

#-----------------------------------block id: 140491805910368
lw $t5, b_
lw $s6,t.9

li $t7,0
sw $s6, t.9
sw $t5, b_

bne $s6,$t7,label.15

#-----------------------------------block id: 140491805910440
lw $t5, b_
lw $s6,t.10

li $t7,0
sw $s6, t.10
sw $t5, b_

bne $s6,$t7,label.15

#-----------------------------------block id: 140491805910512
lw $t5,t.11
li $t5, 0

sw $t5, t.11

j label.16

#-----------------------------------block id: 140491805910584
label.15:

lw $t5,t.11
li $t5, 1

sw $t5, t.11

#-----------------------------------block id: 140491805910656
label.16:

lw $t5, t.11
li $t7,0
sw $t5, t.11

bne $t5,$t7,label.17

#-----------------------------------block id: 140491805910728
lw $t5,t.12
li $t5, 0

sw $t5, t.12

j label.18

#-----------------------------------block id: 140491805910800
label.17:

lw $t5,t.12
li $t5, 1

sw $t5, t.12

#-----------------------------------block id: 140491805910872
label.18:

lw $t5, t.12

lw $s6,t.13
li $s6, 1

sw $t5, t.12
sw $s6, t.13

j label.20

#-----------------------------------block id: 140491805910944
label.19:

lw $t5,t.13
li $t5, 0

sw $t5, t.13

#-----------------------------------block id: 140491805911016
label.20:

lw $t5, t.13
li $t7,0
sw $t5, t.13

bne $t5,$t7,label.21

#-----------------------------------block id: 140491805911088
lw $t5,a
li $t5, 0

sw $t5, a

j label.22

#-----------------------------------block id: 140491805911160
label.21:

lw $t5,a
li $t5, 1

sw $t5, a

#-----------------------------------block id: 140491805911232
label.22:

lw $ra, ($sp)
add $sp, $sp, 4

jr $ra

#-----------------------------------block id: 140491805911304
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

