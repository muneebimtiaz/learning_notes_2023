dosseg
.model small
.stack 100h
.data
.code
main proc

    ; Initialize values
    mov ax, 20      ; Move the value 20 into AX register
    mov bx, 10      ; Move the value 10 into BX register
    
    ; Perform subtraction
    sub ax, bx      ; Subtract the value in BX register from AX register

    ; Exit the program
    mov ah, 4Ch     
    int 21h    
main endp
end main
