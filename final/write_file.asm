.data
str_exit: .asciiz "file.txt"
str_data: .asciiz "This is a test!again2\n"
str_data_end:

.text

main:
file_open:
    li $v0, 13
    la $a0, str_exit
    li $a1, 1
    li $a2, 0
    syscall  # File descriptor gets returned in $v0
file_write:
    move $a0, $v0  # Syscall 15 requieres file descriptor in $a0
    li $v0, 15
    la $a1, str_data
    la $a2, str_data_end
    la $a3, str_data
    subu $a2, $a2, $a3  # computes the length of the string, this is really a constant
    li $a2, 100
    syscall

file_close:
    li $v0, 16  # $a0 already has the file descriptor
    syscall

li $v0,10
syscall