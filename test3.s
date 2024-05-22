
L0:
     j Lmain
L3:
      li t0,0
      sw t0,-12(sp)
L4:
      lw t1,-12(sp)
      li t2,10
      ble t1, t2, L6
L5:
      j L9
L6:
      lw t1,-12(sp)
      li t2,1
      add t1, t2, t1
      sw t1,-16(sp)
L7:
      lw t0,-16(sp)
      sw t0,-12(sp)
L8:
      j L4
L3:
      li t0,0
      sw t0,-12(sp)
L4:
      lw t1,-12(sp)
      li t2,10
      ble t1, t2, L6
L5:
      j L9
L6:
      lw t1,-12(sp)
      li t2,1
      add t1, t2, t1
      lw t0,-4(sp)
      lw t0,-4(t0)