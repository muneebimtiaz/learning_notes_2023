include 'emu8086.inc'

org 100h

.data
array  dw 5 dup(?)     ; Array to store user input, fixed size 5
count  dw 5            ; Number of elements in the array, fixed size 5
input_message db 'Enter element from (0-9): $'
newline db 0Ah, 0Dh, '$'
sorted_message db 'Sorted array: $'

.code
    ; Prompt user to enter each element
    mov cx, count
    lea di, array

input_loop:
    ; Display input message
    mov ah, 09h
    lea dx, input_message
    int 21h

    ; Read a single character from the user
    mov ah, 01h
    int 21h

    ; Subtract ASCII '0' to convert character to numerical value
    sub al, '0'

    ; Store the entered value in the array
    mov [di], ax
    add di, 2  ; Move to the next element (2 bytes per element)

    ; Display newline characters
    mov ah, 09h
    lea dx, newline
    int 21h

    ; Move to the next element
    loop input_loop

    ; Sort the array
    mov cx, count
    dec cx

nextscan:
    mov bx, cx
    mov si, 0

nextcomp:
    mov ax, array[si]
    mov dx, array[si + 2]
    cmp ax, dx

    jnc noswap

    mov array[si], dx
    mov array[si + 2], ax

noswap:
    add si, 2
    dec bx
    jnz nextcomp

    loop nextscan

    ; Display sorted message
    mov ah, 09h
    lea dx, sorted_message
    int 21h

    ; Display sorted array
    mov cx, count
    mov si, 0

print:
    ; Print each element
    mov ax, array[si]
    add ax, '0'         ; Convert the number to ASCII
    mov ah, 0eh
    int 10h

    ; Display separator between elements
    mov ah, 02h
    mov dl, ' '
    int 21h

    add si, 2  ; Move to the next element (2 bytes per element)
    loop print

    ; Display newline characters
    mov ah, 09h
    lea dx, newline
    int 21h

    ; Exit the program
    ret
