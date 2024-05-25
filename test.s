
L0:
     j Lmain
L1:
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
L19:
      lw ra, 0(sp)
      jr ra
L20:
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
      j L27
L26:
      j L44
L27:
      lw t1,-12(sp)
      li t2,0
      beq t1, t2, L31
L28:
      j L29
L29:
      lw t1,-12(sp)
      li t2,1
      beq t1, t2, L31
L30:
      j L33
L32:
      j L44
L33:
      lw t1,-12(sp)
      li t2,1
      sub t1, t2, t1
      sw t1,-20(sp)
L34:
      addi fp, sp,None
      lw t1,-20(sp)
      sw t1, -12(fp)
L35:
      add t0, sp,-24
      sw t0, -8(fp)
L36:
      lw t0, -4(sp)
      sw t0, -4(fp)
      addi sp, sp,None
      sw ra, (sp)
      jal L21
      addi sp, sp,-None
L37:
      lw t1,-12(sp)
      li t2,2
      sub t1, t2, t1
      sw t1,-28(sp)
L38:
      addi fp, sp,None
      lw t1,-28(sp)
      sw t1, -12(fp)
L39:
      add t0, sp,-32
      sw t0, -8(fp)
L40:
      lw t0, -4(sp)
      sw t0, -4(fp)
      addi sp, sp,None
      sw ra, (sp)
      jal L21
      addi sp, sp,-None
L41:
      lw t1,-24(sp)
      lw t2,-32(sp)
      add t1, t2, t1
      sw t1,-36(sp)
L43:
      j L44
L44:
      lw ra, 0(sp)
      jr ra
L45:
L46:
L47:
      lw t1,-12(gp)
      li t2,1
      add t1, t2, t1
      sw t1,-20(sp)
L48:
      lw t1,-20(sp)
      sw t1,-12(gp)
L49:
      lw t1,-16(sp)
      lw t2,-12(sp)
      div t1, t2, t1
      sw t1,-24(sp)
L50:
      lw t1,-24(sp)
      lw t2,-12(sp)
      mul t1, t2, t1
      sw t1,-28(sp)
L51:
      lw t1,-16(sp)
      lw t2,-28(sp)
      beq t1, t2, L53
L52:
      j L55
L54:
      j L57
L56:
      j L57
L57:
      lw ra, 0(sp)
      jr ra
L58:
      lw t1,-12(gp)
      li t2,1
      add t1, t2, t1
      sw t1,-20(sp)
L59:
      lw t1,-20(sp)
      sw t1,-12(gp)
L60:
      li t1,2
      sw t1,-16(sp)
L61:
      lw t1,-16(sp)
      lw t2,-12(sp)
      blt t1, t2, L63
L62:
      j L74
L63:
      addi fp, sp,32
      lw t1,-16(sp)
      sw t1, -12(fp)
L64:
      lw t1,-12(sp)
      sw t1, -16(fp)
L65:
      add t0, sp,-24
      sw t0, -8(fp)
L66:
      sw sp, -4(fp)
      addi sp, sp,32
      sw ra, (sp)
      jal L47
      addi sp, sp,-32
L67:
      lw t1,-24(sp)
      li t2,1
      beq t1, t2, L69
L68:
      j L71
L70:
      j L71
L71:
      lw t1,-16(sp)
      li t2,1
      add t1, t2, t1
      sw t1,-28(sp)
L72:
      lw t1,-28(sp)
      sw t1,-16(sp)
L73:
      j L61
L75:
      lw ra, 0(sp)
      jr ra
L76:
L77:
L78:
      lw t1,-12(gp)
      li t2,1
      add t1, t2, t1
      sw t1,-16(sp)
L79:
      lw t1,-16(sp)
      sw t1,-12(gp)
L80:
      lw t1,-12(sp)
      lw t2,-12(sp)
      mul t1, t2, t1
      sw t1,-20(sp)
L82:
      lw ra, 0(sp)
      jr ra
L83:
      lw t1,-12(gp)
      li t2,1
      add t1, t2, t1
      sw t1,-20(sp)
L84:
      lw t1,-20(sp)
      sw t1,-12(gp)
L85:
      addi fp, sp,24
      lw t1,-12(sp)
      sw t1, -12(fp)
L86:
      add t0, sp,-24
      sw t0, -8(fp)
L87:
      sw sp, -4(fp)
      addi sp, sp,24
      sw ra, (sp)
      jal L78
      addi sp, sp,-24
L88:
      addi fp, sp,24
      lw t1,-12(sp)
      sw t1, -12(fp)
L89:
      add t0, sp,-28
      sw t0, -8(fp)
L90:
      sw sp, -4(fp)
      addi sp, sp,24
      sw ra, (sp)
      jal L78
      addi sp, sp,-24
L91:
      lw t1,-24(sp)
      lw t2,-28(sp)
      mul t1, t2, t1
      sw t1,-32(sp)
L92:
      lw t1,-32(sp)
      sw t1,-16(sp)
L94:
      lw ra, 0(sp)
      jr ra
L95:
L96:
      lw t1,-12(gp)
      li t2,1
      add t1, t2, t1
      sw t1,-16(sp)
L97:
      lw t1,-16(sp)
      sw t1,-12(gp)
L98:
      lw t1,-12(sp)
      li t2,4
      rem t1, t2, t1
      sw t1,-20(sp)
L99:
      lw t1,-20(sp)
      li t2,0
      beq t1, t2, L101
L100:
      j L104
L101:
      lw t1,-12(sp)
      li t2,100
      rem t1, t2, t1
      sw t1,-24(sp)
L102:
      lw t1,-24(sp)
      li t2,0
      bne t1, t2, L107
L103:
      j L104
L104:
      lw t1,-12(sp)
      li t2,400
      rem t1, t2, t1
      sw t1,-28(sp)
L105:
      lw t1,-28(sp)
      li t2,0
      beq t1, t2, L107
L106:
      j L109
L108:
      j L111
L110:
      j L111
L111:
      lw ra, 0(sp)
      jr ra
Lmain:
      addi sp,sp,56
      mv gp,sp
L113:
      li t1,0
      sw t1,-12(sp)
L115:
      lw t1,-20(sp)
      sw t1,-16(sp)
L116:
      lw a0,-16(sp)
      li a7, 1
      ecall
      la a0, str_nl
      li a7, 4
      ecall
L117:
      li t1,1600
      sw t1,-16(sp)
L118:
      lw t1,-16(sp)
      li t2,2000
      ble t1, t2, L120
L119:
      j L127
L120:
      addi fp, sp,32
      lw t1,-16(sp)
      sw t1, -12(fp)
L121:
      add t0, sp,-24
      sw t0, -8(fp)
L122:
      sw sp, -4(fp)
      addi sp, sp,32
      sw ra, (sp)
      jal L96
      addi sp, sp,-32
L123:
      lw a0,-24(sp)
      li a7, 1
      ecall
      la a0, str_nl
      li a7, 4
      ecall
L124:
      lw t1,-16(sp)
      li t2,400
      add t1, t2, t1
      sw t1,-28(sp)
L125:
      lw t1,-28(sp)
      sw t1,-16(sp)
L126:
      j L118
L127:
      addi fp, sp,32
      li t1,2023
      sw t1, -12(fp)
L128:
      add t0, sp,-32
      sw t0, -8(fp)
L129:
      sw sp, -4(fp)
      addi sp, sp,32
      sw ra, (sp)
      jal L96
      addi sp, sp,-32
L130:
      lw a0,-32(sp)
      li a7, 1
      ecall
      la a0, str_nl
      li a7, 4
      ecall
L131:
      addi fp, sp,32
      li t1,2024
      sw t1, -12(fp)
L132:
      add t0, sp,-36
      sw t0, -8(fp)
L133:
      sw sp, -4(fp)
      addi sp, sp,32
      sw ra, (sp)
      jal L96
      addi sp, sp,-32
L134:
      lw a0,-36(sp)
      li a7, 1
      ecall
      la a0, str_nl
      li a7, 4
      ecall
L135:
      addi fp, sp,36
      li t1,3
      sw t1, -12(fp)
L136:
      add t0, sp,-40
      sw t0, -8(fp)
L137:
      sw sp, -4(fp)
      addi sp, sp,36
      sw ra, (sp)
      jal L77
      addi sp, sp,-36
L138:
      lw a0,-40(sp)
      li a7, 1
      ecall
      la a0, str_nl
      li a7, 4
      ecall
L139:
      addi fp, sp,40
      li t1,5
      sw t1, -12(fp)
L140:
      add t0, sp,-44
      sw t0, -8(fp)
L141:
      sw sp, -4(fp)
      addi sp, sp,40
      sw ra, (sp)
      jal L21
      addi sp, sp,-40
L142:
      lw a0,-44(sp)
      li a7, 1
      ecall
      la a0, str_nl
      li a7, 4
      ecall
L143:
      lw t1,-16(sp)
      li t2,12
      ble t1, t2, L145
L144:
      j L152
L145:
      addi fp, sp,32
      lw t1,-16(sp)
      sw t1, -12(fp)
L146:
      add t0, sp,-48
      sw t0, -8(fp)
L147:
      sw sp, -4(fp)
      addi sp, sp,32
      sw ra, (sp)
      jal L46
      addi sp, sp,-32
L148:
      lw a0,-48(sp)
      li a7, 1
      ecall
      la a0, str_nl
      li a7, 4
      ecall
L149:
      lw t1,-16(sp)
      li t2,1
      add t1, t2, t1
      sw t1,-52(sp)
L150:
      lw t1,-52(sp)
      sw t1,-16(sp)
L151:
      j L143
L152:
      lw a0,-12(sp)
      li a7, 1
      ecall
      la a0, str_nl
      li a7, 4
      ecall
L153:
      li a0,0
      li a7,93
      ecall