
.data
str_nl: .asciz "\n"
.text
L0:
     j Lmain
L1:
      sw ra,-0(sp)
L2:
      li t1,0
      sw t1,-12(sp)
L3:
      lw t1,-12(sp)
      li t2,10
      ble t1, t2, L5
L4:
      j L8
L5:
      lw t1,-12(sp)
      li t2,1
      add t1, t1, t2
      sw t1,-16(sp)
L6:
      lw t1,-16(sp)
      sw t1,-12(sp)
L7:
      j L3
L8:
      lw t1,-12(sp)
      lw t0, -8(sp)
      sw t1, 0(t0)
      j L9
L9:
      lw ra, 0(sp)
      jr ra
L10:
      sw ra,-0(sp)
L11:
      lw t1,-12(sp)
      lw t2,-16(sp)
      div t1, t1, t2
      sw t1,-24(sp)
L12:
      lw t1,-20(sp)
      lw t2,-24(sp)
      beq t1, t2, L14
L13:
      j L16
L14:
      li t1,1
      lw t0, -8(sp)
      sw t1, 0(t0)
      j L18
L15:
      j L18
L16:
      li t1,0
      lw t0, -8(sp)
      sw t1, 0(t0)
      j L18
L17:
      j L18
L18:
      lw ra, 0(sp)
      jr ra
L19:
      sw ra,-0(sp)
L20:
      lw t1,-12(sp)
      lw t2,-16(sp)
      mul t1, t1, t2
      sw t1,-24(sp)
L21:
      lw t1,-24(sp)
      lw t2,-20(sp)
      mul t1, t1, t2
      sw t1,-28(sp)
L22:
      lw t1,-28(sp)
      lw t0, -8(sp)
      sw t1, 0(t0)
      j L23
L23:
      lw ra, 0(sp)
      jr ra
L24:
      sw ra,-0(sp)
L25:
      lw t1,-16(sp)
      li t2,1
      beq t1, t2, L27
L26:
      j L29
L27:
      lw t1,-12(sp)
      lw t0, -8(sp)
      sw t1, 0(t0)
      j L41
L28:
      j L41
L29:
      lw t1,-16(sp)
      li t2,0
      beq t1, t2, L31
L30:
      j L33
L31:
      li t1,1
      lw t0, -8(sp)
      sw t1, 0(t0)
      j L41
L32:
      j L41
L33:
      addi fp, sp,32
      lw t1,-12(sp)
      sw t1, -12(fp)
L34:
      lw t1,-16(sp)
      li t2,1
      sub t1, t1, t2
      sw t1,-20(sp)
L35:
      lw t1,-20(sp)
      sw t1, -16(fp)
L36:
      addi t0, sp,-24
      sw t0, -8(fp)
L37:
      lw t0, -4(sp)
      sw t0, -4(fp)
      addi sp, sp,32
      sw ra, 0(sp)
      jal L24
      addi sp, sp,-32
L38:
      lw t1,-12(sp)
      lw t2,-24(sp)
      mul t1, t1, t2
      sw t1,-28(sp)
L39:
      lw t1,-28(sp)
      lw t0, -8(sp)
      sw t1, 0(t0)
      j L41
L40:
      j L41
L41:
      lw ra, 0(sp)
      jr ra
L42:
      sw ra,-0(sp)
L43:
      lw t1,-12(sp)
      li t2,0
      beq t1, t2, L47
L44:
      j L45
L45:
      lw t1,-12(sp)
      li t2,1
      beq t1, t2, L47
L46:
      j L49
L47:
      li t1,1
      lw t0, -8(sp)
      sw t1, 0(t0)
      j L56
L48:
      j L56
L49:
      lw t1,-12(sp)
      li t2,1
      sub t1, t1, t2
      sw t1,-16(sp)
L50:
      addi fp, sp,28
      lw t1,-16(sp)
      sw t1, -12(fp)
L51:
      addi t0, sp,-20
      sw t0, -8(fp)
L52:
      lw t0, -4(sp)
      sw t0, -4(fp)
      addi sp, sp,28
      sw ra, 0(sp)
      jal L42
      addi sp, sp,-28
L53:
      lw t1,-12(sp)
      lw t2,-20(sp)
      mul t1, t1, t2
      sw t1,-24(sp)
L54:
      lw t1,-24(sp)
      lw t0, -8(sp)
      sw t1, 0(t0)
      j L56
L55:
      j L56
L56:
      lw ra, 0(sp)
      jr ra
L57:
      sw ra,-0(sp)
L58:
      lw t1,-12(gp)
      li t2,1
      add t1, t1, t2
      sw t1,-28(sp)
L59:
      lw t1,-28(sp)
      sw t1,-12(gp)
L60:
      lw t1,-12(sp)
      lw t2,-16(sp)
      blt t1, t2, L62
L61:
      j L66
L62:
      lw t1,-12(sp)
      lw t2,-20(sp)
      blt t1, t2, L64
L63:
      j L66
L64:
      lw t1,-12(sp)
      sw t1,-24(sp)
L65:
      j L74
L66:
      lw t1,-16(sp)
      lw t2,-12(sp)
      blt t1, t2, L68
L67:
      j L72
L68:
      lw t1,-16(sp)
      lw t2,-20(sp)
      blt t1, t2, L70
L69:
      j L72
L70:
      lw t1,-16(sp)
      sw t1,-24(sp)
L71:
      j L74
L72:
      lw t1,-20(sp)
      sw t1,-24(sp)
L73:
      j L74
L74:
      lw t1,-24(sp)
      lw t0, -8(sp)
      sw t1, 0(t0)
      j L75
L75:
      lw ra, 0(sp)
      jr ra
Lmain:
      addi sp,sp,80
      mv gp,sp
L77:
      li t1,0
      sw t1,-16(sp)
L78:
      li t1,0
      sw t1,-12(sp)
L79:
      lw t1,-16(sp)
      li t2,100
      ble t1, t2, L81
L80:
      j L86
L81:
      addi fp, sp,20
      addi t0, sp,-40
      sw t0, -8(fp)
L82:
      addi fp, sp,20
      sw sp, -4(fp)
      addi sp, sp,20
      sw ra, 0(sp)
      jal L1
      addi sp, sp,-20
L83:
      lw t1,-16(sp)
      lw t2,-40(sp)
      add t1, t1, t2
      sw t1,-44(sp)
L84:
      lw t1,-44(sp)
      sw t1,-16(sp)
L85:
      j L79
L86:
      addi fp, sp,28
      lw t1,-16(sp)
      sw t1, -12(fp)
L87:
      lw t1,-16(sp)
      sw t1, -16(fp)
L88:
      li t1,1
      sw t1, -20(fp)
L89:
      addi t0, sp,-48
      sw t0, -8(fp)
L90:
      sw sp, -4(fp)
      addi sp, sp,28
      sw ra, 0(sp)
      jal L10
      addi sp, sp,-28
L91:
      lw t1,-48(sp)
      sw t1,-20(sp)
L92:
      addi fp, sp,32
      li t1,10
      sw t1, -12(fp)
L93:
      li t1,33
      sw t1, -16(fp)
L94:
      li t1,3
      sw t1, -20(fp)
L95:
      addi t0, sp,-52
      sw t0, -8(fp)
L96:
      sw sp, -4(fp)
      addi sp, sp,32
      sw ra, 0(sp)
      jal L19
      addi sp, sp,-32
L97:
      lw t1,-52(sp)
      sw t1,-24(sp)
L98:
      addi fp, sp,28
      li t1,10
      sw t1, -12(fp)
L99:
      addi t0, sp,-56
      sw t0, -8(fp)
L100:
      sw sp, -4(fp)
      addi sp, sp,28
      sw ra, 0(sp)
      jal L42
      addi sp, sp,-28
L101:
      lw t1,-56(sp)
      sw t1,-28(sp)
L102:
      addi fp, sp,32
      li t1,2
      sw t1, -12(fp)
L103:
      li t1,8
      sw t1, -16(fp)
L104:
      addi t0, sp,-60
      sw t0, -8(fp)
L105:
      sw sp, -4(fp)
      addi sp, sp,32
      sw ra, 0(sp)
      jal L24
      addi sp, sp,-32
L106:
      lw t1,-60(sp)
      sw t1,-32(sp)
L107:
      lw t1,-24(sp)
      li t2,-1
      mul t1, t1, t2
      sw t1,-64(sp)
L108:
      addi fp, sp,32
      lw t1,-64(sp)
      sw t1, -12(fp)
L109:
      lw t1,-28(sp)
      li t2,-1
      mul t1, t1, t2
      sw t1,-68(sp)
L110:
      lw t1,-68(sp)
      sw t1, -16(fp)
L111:
      lw t1,-32(sp)
      li t2,-1
      mul t1, t1, t2
      sw t1,-72(sp)
L112:
      lw t1,-72(sp)
      sw t1, -20(fp)
L113:
      addi t0, sp,-76
      sw t0, -8(fp)
L114:
      sw sp, -4(fp)
      addi sp, sp,32
      sw ra, 0(sp)
      jal L57
      addi sp, sp,-32
L115:
      lw t1,-76(sp)
      sw t1,-36(sp)
L116:
      lw t1,-12(sp)
      li t2,0
      beq t1, t2, L120
L117:
      j L118
L118:
      lw t1,-12(sp)
      li t2,1
      beq t1, t2, L120
L119:
      j L122
L120:
      lw a0,-12(sp)
      li a7, 1
      ecall
      la a0, str_nl
      li a7, 4
      ecall
L121:
      j L122
L122:
      lw a0,-16(sp)
      li a7, 1
      ecall
      la a0, str_nl
      li a7, 4
      ecall
L123:
      lw a0,-20(sp)
      li a7, 1
      ecall
      la a0, str_nl
      li a7, 4
      ecall
L124:
      lw a0,-24(sp)
      li a7, 1
      ecall
      la a0, str_nl
      li a7, 4
      ecall
L125:
      lw a0,-28(sp)
      li a7, 1
      ecall
      la a0, str_nl
      li a7, 4
      ecall
L126:
      lw a0,-32(sp)
      li a7, 1
      ecall
      la a0, str_nl
      li a7, 4
      ecall
L127:
      lw a0,-36(sp)
      li a7, 1
      ecall
      la a0, str_nl
      li a7, 4
      ecall
L128:
      lw a0,-12(sp)
      li a7, 1
      ecall
      la a0, str_nl
      li a7, 4
      ecall
L129:
      li a0,0
      li a7,93
      ecall