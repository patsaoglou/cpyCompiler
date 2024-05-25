
.data
str_nl: .asciz "\n"
.text
L0:
     j Lmain
L1:
      sw ra,-0(sp)
L2:
      lw t1,-12(gp)
      li t2,1
      add t1, t2, t1
      sw t1,-28(sp)
L3:
      lw t1,-28(sp)
      sw t1,-12(gp)
L4:
      lw t1,-12(sp)
      lw t2,-16(sp)
      bgt t1, t2, L6
L5:
      j L10
L6:
      lw t1,-12(sp)
      lw t2,-20(sp)
      bgt t1, t2, L8
L7:
      j L10
L8:
      lw t1,-12(sp)
      sw t1,-24(sp)
L9:
      j L18
L10:
      lw t1,-16(sp)
      lw t2,-12(sp)
      bgt t1, t2, L12
L11:
      j L16
L12:
      lw t1,-16(sp)
      lw t2,-20(sp)
      bgt t1, t2, L14
L13:
      j L16
L14:
      lw t1,-16(sp)
      sw t1,-24(sp)
L15:
      j L18
L16:
      lw t1,-20(sp)
      sw t1,-24(sp)
L17:
      j L18
L18:
      lw t0,-24(sp)
      lw t0, -8(sp)
      sw t1, 0(t0)
      j L19
L19:
      lw ra, 0(sp)
      jr ra
L20:
      sw ra,-0(sp)
L21:
      lw t1,-12(gp)
      li t2,1
      add t1, t2, t1
      sw t1,-16(sp)
L22:
      lw t1,-16(sp)
      sw t1,-12(gp)
L23:
      lw t1,-12(sp)
      li t2,0
      blt t1, t2, L25
L24:
      j L28
L25:
      lw t0,-4(sp)
      lw t0,-4(t0)