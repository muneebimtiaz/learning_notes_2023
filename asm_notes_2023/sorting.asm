include 'emu8086.inc'

org 100h 
.data
array  db 9,1,5,3,8,2,6
count  dw 7

.code
    mov cx, count      
    dec cx               

nextscan:                
    mov bx, cx
    mov si, 0 

nextcomp:
    mov al, array[si]
    mov dl, array[si+1]
    cmp al, dl

    jnc noswap 

    mov array[si], dl
    mov array[si+1], al

noswap: 
    inc si
    dec bx
    jnz nextcomp

    loop nextscan    

    mov cx, 7
    mov si, 0

print:
    mov al, array[si]  
    add al, 30h
    mov ah, 0eh
    int 10h 
    mov ah, 2
    mov dl, ' '
    int 21h
    inc si
    loop print

    ret
