.data  
fin: .asciiz "file.txt"      # filename for input
buffer: .space 1024

.text
#open a file for writing

main:
li   $v0, 13       # system call for open file
la   $a0, fin      # board file name
li   $a1, 0        # Open for reading
li   $a2, 0
syscall            # open a file (file descriptor returned in $v0)
move $s6, $v0      # save the file descriptor 

#read from file
li   $v0, 14       # system call for read from file
move $a0, $s6      # file descriptor 
la   $a1, buffer   # address of buffer to which to read
li   $a2, 1024     # hardcoded buffer length
syscall            # read from file

li $v0, 4
la $a0, buffer
syscall

# Close the file 
li   $v0, 16       # system call for close file
move $a0, $s6      # file descriptor to close
syscall            # close file

li $v0,10
syscall