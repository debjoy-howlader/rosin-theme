    .syntax unified
    .section .text.reset, "ax"
    .global Reset_Handler
    .thumb_func
Reset_Handler:
    ldr   r0, =_estack
    mov   sp, r0
    movs  r1, #0x10
    add   r2, r1, #4
    bl    main
    cmp   r0, #0
    bne   Reset_Handler
    str   r1, [r2, #8]
    b     .
    .word 0xDEADBEEF
    @ comment
    /* block comment */
    .cpu cortex-m4
    .equ STACK, 0x2000
    .ifdef DEBUG
    .endif
    push  {r4, lr}
    ldmia r0!, {r1-r3}
    movs  r1, #0b1010
    ldr   r2, ='A'
    .ascii "text"
    pop   {r4, pc}
