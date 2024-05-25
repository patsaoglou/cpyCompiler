
.data
str_nl: .asciz "\n"
.text
L0:
     j Lmain
L1:
      sw ra,-0(sp)
L2:
      lw t1,-12(sp)
      li t2,0
      ble t1, t2, L4
L3:
      j L6
L4:
      li t1,0
      lw t0, -8(sp)
      sw t1, 0(t0)
      j L21
L5:
      j L21
L6:
      lw t1,-12(sp)
      li t2,1
      beq t1, t2, L8
L7:
      j L10
L8:
      li t1,1
      lw t0, -8(sp)
      sw t1, 0(t0)
      j L21
L9:
      j L21
L10:
      lw t1,-12(sp)
      li t2,1
      sub t1, t1, t2
      sw t1,-16(sp)
L11:
      addi fp, sp,36
      lw t1,-16(sp)
      sw t1, -12(fp)
L12:
      addi t0, sp,-20
      sw t0, -8(fp)
L13:
      lw t0, -4(sp)
      sw t0, -4(fp)
      addi sp, sp,36
      sw ra, 0(sp)
      jal L1
      addi sp, sp,-36
L14:
      lw t1,-12(sp)
      li t2,2
      sub t1, t1, t2
      sw t1,-24(sp)
L15:
      addi fp, sp,36
      lw t1,-24(sp)
      sw t1, -12(fp)
L16:
      addi t0, sp,-28
      sw t0, -8(fp)
L17:
      lw t0, -4(sp)
      sw t0, -4(fp)
      addi sp, sp,36
      sw ra, 0(sp)
      jal L1
      addi sp, sp,-36
L18:
      lw t1,-20(sp)
      lw t2,-28(sp)
      add t1, t1, t2
      sw t1,-32(sp)
L19:
      lw t1,-32(sp)
      lw t0, -8(sp)
      sw t1, 0(t0)
      j L21
L20:
      j L21
L21:
      lw ra, 0(sp)
      jr ra
Lmain:
      addi sp,sp,20
      mv gp,sp
L23:
      addi fp, sp,36
      li t1,3
      sw t1, -12(fp)
L24:
      addi t0, sp,-16
      sw t0, -8(fp)
L25:
      sw sp, -4(fp)
      addi sp, sp,36
      sw ra, 0(sp)
      jal L1
      addi sp, sp,-36
L26:
      lw t1,-16(sp)
      sw t1,-12(sp)
L27:
      li a0,0
      li a7,93
      ecall