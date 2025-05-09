dosseg
.model small
.stack 100h
.data
.code
main proc

   ; Initialize values
    mov ax, 50      ; Move the value 50 into AX register
    mov bx, 5       ; Move the value 5 into BX register
    
    ; Perform division
    div bx          ; Divide the value in AX register by BX register
                    ; Quotient will be stored in AX, remainder in DX

    mov bx, 2       ; Move the value 2 into BX register

    div bx    

    ; Exit the program
    mov ah, 4Ch     
    int 21h    
main endp
end main
