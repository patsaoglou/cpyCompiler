
L0:
     j Lmain
L3:
      li t1,1
      li t2,1
      add t1, t2, t1
      sw t1,-16(sp)
L4:
      lw t0,-16(sp)
      sw t0,-12(sp)
L7:
      li t1,1
      li t2,1
      add t1, t2, t1
      sw t1,-16(sp)
L8:
      lw t0,-16(sp)
      sw t0,-12(sp)
L10:
      lw t1,-12(sp)
      li t2,10
      ble t1, t2, L12
L11:
      j L15
L12:
      lw t1,-12(sp)
      li t2,1
      add t1, t2, t1
      sw t1,-16(sp)
L13:
      lw t0,-16(sp)
      sw t0,-12(sp)
L14:
      j L10
Lmain:
      addi sp,sp,20
      mv gp,sp
L17:
      li t0,1
      sw t0,-12(sp)
L19:
      li a0,0
      li a7,93
      ecall