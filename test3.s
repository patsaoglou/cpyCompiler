
.data
str_nl: .asciz "\n"
.text
L0:
     j Lmain
L1:
      sw ra,-0(sp)
L2:
      lw t0,-4(sp)
      addi t0,t0,-12
      lw t1, 0(t0)
      li t2,1
      add t1, t2, t1
      sw t1,-12(sp)
L3:
      lw t1,-12(sp)
      lw t0,-4(sp)
      addi t0,t0,-12
      sw t1, 0(t0)
L4:
      lw ra, 0(sp)
      jr ra