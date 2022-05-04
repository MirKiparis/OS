.586 ;686
.MODEL FLAT, C
.STACK
.DATA
a       dd      0
b       dd      2
t       dd      3
iter    dd      100000000
i       dd      0
EXTRN printf : proc
.CODE

cicle PROC 

        mov     edx, i          ; use edx as i
        mov     ebx, b   ; use ebx as 2*b + c
        add     ebx, ebx
        add     ebx, t
        mov     eax, 0          ; use eax as a
        mov     ecx, iter ; ecx is loop counter
        
_for:
        add     eax, ebx        ; a += b*2 + c
        sub     eax, edx        ; a += -i
        inc     edx             ; i++
        LOOP     _for
    

ret

cicle ENDP

END