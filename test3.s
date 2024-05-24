
L0:
     j Lmain
L1:
L2:
L3:
      lw t1,-12(sp)
      li t2,1
      add t1, t2, t1
      sw t1,-16(sp)
L4:
      lw t1,-16(sp)
      sw t1,-12(sp)
L5:
      lw ra, 0(sp)
      jr ra
L6:
      lw a0,-12(sp)
      li a7, 1
      ecall
      la a0, str_nl
      li a7, 4
      ecall
L7:
      lw ra, 0(sp)
      jr ra
Lmain:
      addi sp,sp,20
      mv gp,sp
L9:
      li t1,1
      sw t1,-16(sp)
L10:
      li a0,0
      li a7,93
      ecall