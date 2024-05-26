
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
      add t1, t1, t2
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
      lw t1,-24(sp)
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
      add t1, t1, t2
      sw t1,-16(sp)
L22:
      lw t1,-16(sp)
      sw t1,-12(gp)
L23:
      lw t1,-12(sp)
      li t2,0
      ble t1, t2, L25
L24:
      j L27
L25:
      li t1,0
      lw t0, -8(sp)
      sw t1, 0(t0)
      j L42
L26:
      j L42
L27:
      lw t1,-12(sp)
      li t2,1
      beq t1, t2, L29
L28:
      j L31
L29:
      li t1,1
      lw t0, -8(sp)
      sw t1, 0(t0)
      j L42
L30:
      j L42
L31:
      lw t1,-12(sp)
      li t2,1
      sub t1, t1, t2
      sw t1,-20(sp)
L32:
      addi s1, sp,40
      lw t1,-20(sp)
      sw t1, -12(s1)
L33:
      addi t0, sp,-24
      sw t0, -8(s1)
L34:
      lw t0, -4(sp)
      sw t0, -4(s1)
      addi sp, sp,40
      sw ra, 0(sp)
      jal L20
      addi sp, sp,-40
L35:
      lw t1,-12(sp)
      li t2,2
      sub t1, t1, t2
      sw t1,-28(sp)
L36:
      addi s1, sp,40
      lw t1,-28(sp)
      sw t1, -12(s1)
L37:
      addi t0, sp,-32
      sw t0, -8(s1)
L38:
      lw t0, -4(sp)
      sw t0, -4(s1)
      addi sp, sp,40
      sw ra, 0(sp)
      jal L20
      addi sp, sp,-40
L39:
      lw t1,-24(sp)
      lw t2,-32(sp)
      add t1, t1, t2
      sw t1,-36(sp)
L40:
      lw t1,-36(sp)
      lw t0, -8(sp)
      sw t1, 0(t0)
      j L42
L41:
      j L42
L42:
      lw ra, 0(sp)
      jr ra
L43:
      sw ra,-0(sp)
L44:
      lw t1,-12(gp)
      li t2,1
      add t1, t1, t2
      sw t1,-20(sp)
L45:
      lw t1,-20(sp)
      sw t1,-12(gp)
L46:
      lw t1,-16(sp)
      lw t2,-12(sp)
      div t1, t1, t2
      sw t1,-24(sp)
L47:
      lw t1,-24(sp)
      lw t2,-12(sp)
      mul t1, t1, t2
      sw t1,-28(sp)
L48:
      lw t1,-16(sp)
      lw t2,-28(sp)
      beq t1, t2, L50
L49:
      j L52
L50:
      li t1,1
      lw t0, -8(sp)
      sw t1, 0(t0)
      j L54
L51:
      j L54
L52:
      li t1,0
      lw t0, -8(sp)
      sw t1, 0(t0)
      j L54
L53:
      j L54
L54:
      lw ra, 0(sp)
      jr ra
L55:
      sw ra,-0(sp)
L56:
      lw t1,-12(gp)
      li t2,1
      add t1, t1, t2
      sw t1,-20(sp)
L57:
      lw t1,-20(sp)
      sw t1,-12(gp)
L58:
      li t1,2
      sw t1,-16(sp)
L59:
      lw t1,-16(sp)
      lw t2,-12(sp)
      blt t1, t2, L61
L60:
      j L72
L61:
      addi s1, sp,32
      lw t1,-16(sp)
      sw t1, -12(s1)
L62:
      lw t1,-12(sp)
      sw t1, -16(s1)
L63:
      addi t0, sp,-24
      sw t0, -8(s1)
L64:
      sw sp, -4(s1)
      addi sp, sp,32
      sw ra, 0(sp)
      jal L43
      addi sp, sp,-32
L65:
      lw t1,-24(sp)
      li t2,1
      beq t1, t2, L67
L66:
      j L69
L67:
      li t1,0
      lw t0, -8(sp)
      sw t1, 0(t0)
      j L73
L68:
      j L69
L69:
      lw t1,-16(sp)
      li t2,1
      add t1, t1, t2
      sw t1,-28(sp)
L70:
      lw t1,-28(sp)
      sw t1,-16(sp)
L71:
      j L59
L72:
      li t1,1
      lw t0, -8(sp)
      sw t1, 0(t0)
      j L73
L73:
      lw ra, 0(sp)
      jr ra
L74:
      sw ra,-0(sp)
L75:
      lw t1,-12(gp)
      li t2,1
      add t1, t1, t2
      sw t1,-16(sp)
L76:
      lw t1,-16(sp)
      sw t1,-12(gp)
L77:
      lw t1,-12(sp)
      lw t2,-12(sp)
      mul t1, t1, t2
      sw t1,-20(sp)
L78:
      lw t1,-20(sp)
      lw t0, -8(sp)
      sw t1, 0(t0)
      j L79
L79:
      lw ra, 0(sp)
      jr ra
L80:
      sw ra,-0(sp)
L81:
      lw t1,-12(gp)
      li t2,1
      add t1, t1, t2
      sw t1,-20(sp)
L82:
      lw t1,-20(sp)
      sw t1,-12(gp)
L83:
      addi s1, sp,24
      lw t1,-12(sp)
      sw t1, -12(s1)
L84:
      addi t0, sp,-24
      sw t0, -8(s1)
L85:
      sw sp, -4(s1)
      addi sp, sp,24
      sw ra, 0(sp)
      jal L74
      addi sp, sp,-24
L86:
      addi s1, sp,24
      lw t1,-12(sp)
      sw t1, -12(s1)
L87:
      addi t0, sp,-28
      sw t0, -8(s1)
L88:
      sw sp, -4(s1)
      addi sp, sp,24
      sw ra, 0(sp)
      jal L74
      addi sp, sp,-24
L89:
      lw t1,-24(sp)
      lw t2,-28(sp)
      mul t1, t1, t2
      sw t1,-32(sp)
L90:
      lw t1,-32(sp)
      sw t1,-16(sp)
L91:
      lw t1,-16(sp)
      lw t0, -8(sp)
      sw t1, 0(t0)
      j L92
L92:
      lw ra, 0(sp)
      jr ra
L93:
      sw ra,-0(sp)
L94:
      lw t1,-12(gp)
      li t2,1
      add t1, t1, t2
      sw t1,-16(sp)
L95:
      lw t1,-16(sp)
      sw t1,-12(gp)
L96:
      lw t1,-12(sp)
      li t2,4
      rem t1, t1, t2
      sw t1,-20(sp)
L97:
      lw t1,-20(sp)
      li t2,0
      beq t1, t2, L99
L98:
      j L102
L99:
      lw t1,-12(sp)
      li t2,100
      rem t1, t1, t2
      sw t1,-24(sp)
L100:
      lw t1,-24(sp)
      li t2,0
      bne t1, t2, L105
L101:
      j L102
L102:
      lw t1,-12(sp)
      li t2,400
      rem t1, t1, t2
      sw t1,-28(sp)
L103:
      lw t1,-28(sp)
      li t2,0
      beq t1, t2, L105
L104:
      j L107
L105:
      li t1,1
      lw t0, -8(sp)
      sw t1, 0(t0)
      j L109
L106:
      j L109
L107:
      li t1,0
      lw t0, -8(sp)
      sw t1, 0(t0)
      j L109
L108:
      j L109
L109:
      lw ra, 0(sp)
      jr ra
Lmain:
      addi sp,sp,56
      mv gp,sp
L111:
      li t1,0
      sw t1,-12(sp)
L112:
      li a7,5
      ecall
L113:
      lw t1,-20(sp)
      sw t1,-16(sp)
L114:
      lw a0,-16(sp)
      li a7, 1
      ecall
      la a0, str_nl
      li a7, 4
      ecall
L115:
      li t1,1600
      sw t1,-16(sp)
L116:
      lw t1,-16(sp)
      li t2,2000
      ble t1, t2, L118
L117:
      j L125
L118:
      addi s1, sp,32
      lw t1,-16(sp)
      sw t1, -12(s1)
L119:
      addi t0, sp,-24
      sw t0, -8(s1)
L120:
      sw sp, -4(s1)
      addi sp, sp,32
      sw ra, 0(sp)
      jal L93
      addi sp, sp,-32
L121:
      lw a0,-24(sp)
      li a7, 1
      ecall
      la a0, str_nl
      li a7, 4
      ecall
L122:
      lw t1,-16(sp)
      li t2,400
      add t1, t1, t2
      sw t1,-28(sp)
L123:
      lw t1,-28(sp)
      sw t1,-16(sp)
L124:
      j L116
L125:
      addi s1, sp,32
      li t1,2023
      sw t1, -12(s1)
L126:
      addi t0, sp,-32
      sw t0, -8(s1)
L127:
      sw sp, -4(s1)
      addi sp, sp,32
      sw ra, 0(sp)
      jal L93
      addi sp, sp,-32
L128:
      lw a0,-32(sp)
      li a7, 1
      ecall
      la a0, str_nl
      li a7, 4
      ecall
L129:
      addi s1, sp,32
      li t1,2024
      sw t1, -12(s1)
L130:
      addi t0, sp,-36
      sw t0, -8(s1)
L131:
      sw sp, -4(s1)
      addi sp, sp,32
      sw ra, 0(sp)
      jal L93
      addi sp, sp,-32
L132:
      lw a0,-36(sp)
      li a7, 1
      ecall
      la a0, str_nl
      li a7, 4
      ecall
L133:
      addi s1, sp,36
      li t1,3
      sw t1, -12(s1)
L134:
      addi t0, sp,-40
      sw t0, -8(s1)
L135:
      sw sp, -4(s1)
      addi sp, sp,36
      sw ra, 0(sp)
      jal L80
      addi sp, sp,-36
L136:
      lw a0,-40(sp)
      li a7, 1
      ecall
      la a0, str_nl
      li a7, 4
      ecall
L137:
      addi s1, sp,40
      li t1,5
      sw t1, -12(s1)
L138:
      addi t0, sp,-44
      sw t0, -8(s1)
L139:
      sw sp, -4(s1)
      addi sp, sp,40
      sw ra, 0(sp)
      jal L20
      addi sp, sp,-40
L140:
      lw a0,-44(sp)
      li a7, 1
      ecall
      la a0, str_nl
      li a7, 4
      ecall
L141:
      lw t1,-16(sp)
      li t2,12
      ble t1, t2, L143
L142:
      j L150
L143:
      addi s1, sp,32
      lw t1,-16(sp)
      sw t1, -12(s1)
L144:
      addi t0, sp,-48
      sw t0, -8(s1)
L145:
      sw sp, -4(s1)
      addi sp, sp,32
      sw ra, 0(sp)
      jal L55
      addi sp, sp,-32
L146:
      lw a0,-48(sp)
      li a7, 1
      ecall
      la a0, str_nl
      li a7, 4
      ecall
L147:
      lw t1,-16(sp)
      li t2,1
      add t1, t1, t2
      sw t1,-52(sp)
L148:
      lw t1,-52(sp)
      sw t1,-16(sp)
L149:
      j L141
L150:
      lw a0,-12(sp)
      li a7, 1
      ecall
      la a0, str_nl
      li a7, 4
      ecall
L151:
      li a0,0
      li a7,93
      ecall