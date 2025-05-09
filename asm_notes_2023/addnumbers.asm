dosseg
.model small
.stack 100h
.data
.code
main proc

    ; Initialize values
    mov ax, 20      ; Move the value 20 into AX register
    mov bx, 10      ; Move the value 10 into BX register
    
    ; Perform addition
    add ax, bx      ; Add the value in BX register to AX register

    ; Exit the program
    mov ah, 4Ch     
    int 21h    
main endp
end main
