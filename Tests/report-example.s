
.data
str_nl: .asciz "\n"
.text
L0:
     j Lmain
L1:
      sw ra,-0(sp)
L2:
      li t1,1
      sw t1,-12(gp)
L3:
      lw t1,-16(sp)
      li t2,1
      beq t1, t2, L5
L4:
      j L7
L5:
      lw t1,-12(sp)
      lw t0, -8(sp)
      sw t1, 0(t0)
      j L19
L6:
      j L19
L7:
      lw t1,-16(sp)
      li t2,0
      beq t1, t2, L9
L8:
      j L11
L9:
      li t1,1
      lw t0, -8(sp)
      sw t1, 0(t0)
      j L19
L10:
      j L19
L11:
      addi fp, sp,32
      lw t1,-12(sp)
      sw t1, -12(fp)
L12:
      lw t1,-16(sp)
      li t2,1
      sub t1, t1, t2
      sw t1,-20(sp)
L13:
      lw t1,-20(sp)
      sw t1, -16(fp)
L14:
      addi t0, sp,-24
      sw t0, -8(fp)
L15:
      lw t0, -4(sp)
      sw t0, -4(fp)
      addi sp, sp,32
      sw ra, 0(sp)
      jal L1
      addi sp, sp,-32
L16:
      lw t1,-12(sp)
      lw t2,-24(sp)
      mul t1, t1, t2
      sw t1,-28(sp)
L17:
      lw t1,-28(sp)
      lw t0, -8(sp)
      sw t1, 0(t0)
      j L19
L18:
      j L19
L19:
      lw ra, 0(sp)
      jr ra
Lmain:
      addi sp,sp,24
      mv gp,sp
L21:
      li t1,0
      sw t1,-12(sp)
L22:
      addi fp, sp,32
      li t1,2
      sw t1, -12(fp)
L23:
      li t1,8
      sw t1, -16(fp)
L24:
      addi t0, sp,-20
      sw t0, -8(fp)
L25:
      sw sp, -4(fp)
      addi sp, sp,32
      sw ra, 0(sp)
      jal L1
      addi sp, sp,-32
L26:
      lw t1,-20(sp)
      sw t1,-16(sp)
L27:
      lw a0,-16(sp)
      li a7, 1
      ecall
      la a0, str_nl
      li a7, 4
      ecall
L28:
      lw a0,-12(sp)
      li a7, 1
      ecall
      la a0, str_nl
      li a7, 4
      ecall
L29:
      li a0,0
      li a7,93
      ecall