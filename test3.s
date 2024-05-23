
L0:
     j Lmain
L1:
L2:
      addi fp, sp,None
      add t0, sp,-20
      sw t0, -8(fp)
L3:
      lw t0, -4(sp)
      sw t0, -4(fp)
      addi sp, sp,None
      jal L2
      addi sp, sp,-None
L4:
      lw t0,-20(sp)
      sw t0,-12(sp)
L5:
      lw t1,-12(sp)
      li t2,1
      add t1, t2, t1
      sw t1,-24(sp)
L6:
      lw t0,-24(sp)
      sw t0,-12(sp)
L7:
Lmain:
      addi sp,sp,24
      mv gp,sp
L9:
      addi fp, sp,28
      add t0, sp,-20
      sw t0, -8(fp)
L10:
      sw sp, -4(fp)
      addi sp, sp,28
      jal L2
      addi sp, sp,-28
L11:
      lw t0,-20(sp)
      sw t0,-12(sp)
L13:
      li a0,0
      li a7,93
      ecall