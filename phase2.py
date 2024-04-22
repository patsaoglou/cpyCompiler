# PATSAOGLOU PANTELEIMON 5102
# IATRAKIS IOANNIS 5116

import sys

#define TOKENS
EOFTK = -1
ERRORTK=-5
K1=-3 #desmeumenes lekseis kai anagnwristika
K2=-2 #gia akeraies statheres

ADDTK =100  #+
MINUSTK=101 #-
MULTK=102   #*
DIVTK=103   #//
MODTK=104   #%
LTTK=105    #< LESS THAN
GTTK=106    #> GREAT THAN
LETK = 107     # <= LESS EQUAL
GETK = 108     # >= GREAT EQUAL
EQUALTK = 109  # ==
NOT_EQUALTK = 110  # !=
ASSIGNTK = 111 # =
COMMATK = 112  # ,
UPDOWNDOTTK = 113  # :
OPARTK = 114  # ( OPEN PARENTHESIS
CPARTK = 115  # ) CLOSE PARENTHESIS
OBLOCKTK = 116  # #{ OPEN BLOCK
CBLOCKTK = 117  # #} CLOSE BLOCK
COMMENTK = 118  # ## COMMNENT
INTEGERTK = 119  # AKERAIA STATHERA
ANAGNORTK = 120  # ANAGNORISTIKO (GRAMMATA + ARITHMOUS) megethos:30


#define DESMEUMENES LEKSEIS

MAINTK =121 #main
DEFTK=122 #def
DEF2TK=123 # #def
INTTYPETK=124 # #int e.g #int x=3
GLOBALTK=125 #global
IFTK=126 #if
ELIFTK=127 #elif
ELSETK=128 #else
WHILETK=129 #while
PRINTTK=130 #print
RETURNTK=131 #return
INPUTTK=132 #input
INTCASTTK=133 #int for casting
ANDTK=134 #and
ORTK=135 #or
NOTTK=136 #not


token = ""
line=1
retArray=[]
# generally before each call lex() is already called

current_token = None
is_in_function_definition = 0

quadsList = []
quadNum = 1
tempNum = 1

def gen_quad(op, op1, op2, op3):
    global quadsList
    global quadNum

    newQuad = [quadNum, op, op1, op2, op3]

    quadsList.append(newQuad)
    quadNum += 1
    
    print_quad_list()

def new_temp():
    global tempNum

    newTemp = "T_" + str(tempNum)
    tempNum += 1

    return newTemp

def next_quad():
    global quadNum
    
    return quadNum

def empty_list():
    return []

def make_list(x):
    return [x]

def merge(list_1, list_2):
    return list_1 + list_2

def backpatch(quads_with_label_to_backpatch, label):
    global quadsList

    for quad_with_label in quads_with_label_to_backpatch:
        for quad in quadsList:
            if quad_with_label == quad[0]:
                quad[4] = label



def print_quad_list():
    global quadsList

    input()

    for quad in quadsList:
        print(quad)


def retARRAYTK(state,token):
    global retArray
    retArray=[]
    retArray.append(state)
    retArray.append(''.join([char for char in token if not char.isspace()]))
    return retArray

def lex():
    global line
    global retArray
    start_cmd_line = 0
    EOFflag=0
    state=0
    i=0
    element=' '
    next_element=' '
    token=[]
    array=[[0,1,2,ADDTK,MINUSTK,MULTK,MODTK,DIVTK,ERRORTK,LETK,LTTK,GETK,GTTK,NOT_EQUALTK,ERRORTK,EQUALTK,ASSIGNTK,COMMATK,UPDOWNDOTTK,CPARTK,OPARTK,CBLOCKTK,OBLOCKTK,
           ERRORTK,COMMENTK,DEF2TK,ERRORTK,ERRORTK,INTTYPETK,ERRORTK,ERRORTK,ERRORTK,EOFTK,ERRORTK],
           [K1,1,1,K1,K1,K1,K1,K1,K1,K1,K1,K1,K1,K1,K1,K1,K1,K1,K1,K1,K1,K1,K1,K1,K1,K1,K1,K1,K1,K1,K1,K1,K1,K1],
           [K2,K2,2,K2,K2,K2,K2,K2,K2,K2,K2,K2,K2,K2,K2,K2,K2,K2,K2,K2,K2,K2,K2,K2,K2,K2,K2,K2,K2,K2,K2,K2,K2,K2]]           
            
    while state>=0 and state<100 and i<=31: #i gia na diabazei mexri 30 char + \0 gia anagnwristiko
        element=file.read(1)
        if element.isspace(): 
            index=0
            token.append(element) 
            if element=='\n':
                line=line+1
        elif element.isalpha(): #anagnoristiko exei kai digit
            i=i+1
            index=1
            token.append(element)        
            pos1 = file.tell()
        elif element.isdigit():
            i=i+1
            index=2
            token.append(element)
            pos1 = file.tell()
        elif element=='+':
            index=3
            token.append(element)
        elif element=='-':
            #pos1 = file.tell()
            index=4
            token.append(element)
        elif element=='*':
            index=5
            token.append(element) 
        elif element=='%':
            index=6
            token.append(element) 
        elif element=='/': #katastasi 3
            token.append(element)
            pos = file.tell() #thesi mesa sto arxeio prin diabasw to epomeno xaraktira gia na dw se ti katastasi kattaligw
            next_element=file.read(1) #thelei epistrofi?
            if next_element=='/':
                token.pop()
                token.append('//')
                index=7 #komple katastasi // 
            else:
                token.append(next_element)
                index=8 #ERROR
                print("Invalid character ", token[-1], "is not expected after a '/' in line ",line)
        elif element=='<': #katastasi 4
            token.append(element)
            pos = file.tell()
            next_element=file.read(1)
            if next_element=='=':
                token.pop()
                token.append('<=')
                index=9 #<=
                
            else:
                index=10 #<
                file.seek(pos) #xreiazetai gt exw koitaxei to epomeno kai den einai to = opote prepeina epistrafei
                
        elif element=='>': #katastasi 5
            token.append(element)
            pos = file.tell()
            next_element=file.read(1)
            if next_element=='=':
                token.pop()
                token.append('>=')
                index=11 #>=
                
            else:
                index=12 #>
                file.seek(pos) #xreiazetai gt exw koitaxei to epomeno kai den einai to = opote prepeina epistrafei
                
        elif element=='!': #katastasi 6
            token.append(element)
            pos = file.tell() #thesi mesa sto arxeio prin diabasw to epomeno xaraktira gia na dw sw ti katastasi kattaligw
            next_element=file.read(1) #thelei epistrofi
            if next_element=='=':
                token.pop()
                token.append('!=')
                index=13 #komple katastasi !=
                
            else:
                token.append(next_element)
                index=14 #ERROR
                print("Invalid character ", token[-1], "is not expected after a '!' in line ",line)
                
        elif element=='=': #katastasi 7
            token.append(element)
            pos = file.tell()
            next_element=file.read(1)
            if next_element=='=':
                token.pop()
                token.append('==')
                index=15 #==
                
            else:
                index=16 #=
                file.seek(pos) #xreiazetai gt exw koitaxei to epomeno kai den einai to = opote prepeina epistrafei
                
        elif element==',':
            index=17
            token.append(element)
        elif element==':':
            index=18
            token.append(element)
        elif element==')':
            index=19
            token.append(element)
        elif element=='(':
            index=20
            token.append(element)
        elif element=='#': #katastasi 8
            token.append(element)
            next_element=file.read(1)
            if next_element=='}':
                token.append(next_element)
                index=21 # #}
            elif next_element=='{':
                token.append(next_element)
                index=22 # #{
            elif next_element=='#': #katastasi 9
                token.append(next_element)
                start_cmd_line = line
                while True:                    
                    next_element=file.read(1)
                    if not next_element: #EOF pianei kai kena
                        index=23 #array error bazw anti eoftk
                    
                        print("EOF: Open comments and not closed in line",start_cmd_line)
                        fail_exit("Exit")
                        
                        EOFflag=1
                        break
                    
                    if next_element=='#':#pame sti katastasi 10 exw brei to ena # apo ta 2 gia to kleisimo sxoliou
                        pos = file.tell()
                        next_next=file.read(1)
                        if next_next=='#':
                            index=24 # exoun ## kleisei ta sxolia
                            
                            state=0
                            break          

            elif next_element=='d':
                token.append(next_element)
                next_element=file.read(1)
                if next_element=='e':
                    token.append(next_element)
                    next_element=file.read(1)
                    if next_element=='f':
                        token.append(next_element)
                        index=25 # #def
                    else:
                        token.append(next_element)
                        index=26 #error
                        print("Invalid character '", token[-1], "' is not expected after '",''.join(token[:-1]),"' in line ",line)
                else:
                    token.append(next_element)
                    index=27 #ERROR
                    print("Invalid character '", token[-1], "'is not expected after '" ,''.join(token[:-1]),"' in line ",line)                          

            elif next_element=='i': #katastasi 13
                token.append(next_element)
                next_element=file.read(1)
                if next_element=='n':
                    token.append(next_element)
                    next_element=file.read(1)
                    if next_element=='t':
                        token.append(next_element)
                        index=28 # #int
                    else:
                        token.append(next_element)
                        index=29 #error
                        print("Invalid character '", token[-1], "' is not expected after '",''.join(token[:-1]),"' in line ",line)

                else:
                    token.append(next_element)
                    index=30 #error
                    print("Invalid character '", token[-1], "' is not expected after '",''.join(token[:-1]),"' in line ",line)

            else:
                 token.append(next_element)
                 index=31 #error den akolouthei meta to # kati apo ta orismena
                 print("Invalid character ", token[-1], "is not expected after a '#' in line ",line)

        elif not element: #EOF
            index=32
            EOFflag=1
        else:
            token.append(element)
            index=33 #error
            print("Find character '",token[-1],"' that is not in the language in line",line)
            
        if i >=31:
            fail_exit("Found alphanumeric with length >30. Analisis failed.")
            index=0 #ipervenei ta 30 char
        state=array[state][index]
        
    if state==K1 or state==K2:
            if not element.isspace(): #elegxos den einai kenos char na epistrefei stin proigoumeni thesi (an einai kenos apla katanalwnetai kai proxwrame)
                file.seek(pos1) #epistrefoume stin proigoumeni thesi afou exoume krifokoitaxei to epomeno
            token.pop()

    
    if state >=100:
        return retARRAYTK(state,token)
    elif state==K1:
        
        new_token=''.join([char for char in token if not char.isspace()])
        if new_token=='main':
            return retARRAYTK(MAINTK,token)
        if new_token=='def':
            return retARRAYTK(DEFTK,token)
        if new_token=='#def':
            return retARRAYTK(DEF2TK,token)
        if new_token=='#int':
            return retARRAYTK(INTTYPETK,token)
        if new_token=='global':
            return retARRAYTK(GLOBALTK,token)
        if new_token=='if':
            return retARRAYTK(IFTK,token)
        if new_token=='elif':
            return retARRAYTK(ELIFTK,token)
        if new_token=='else':
            return retARRAYTK(ELSETK,token)
        if new_token=='while':
            return retARRAYTK(WHILETK,token)
        if new_token=='print':
            return retARRAYTK(PRINTTK,token)
        if new_token=='return':
            return retARRAYTK(RETURNTK,token)
        if new_token=='input':
            return retARRAYTK(INPUTTK,token)
        if new_token=='int':    
            return retARRAYTK(INTCASTTK,token)
        if new_token=='and':
            return retARRAYTK(ANDTK,token)
        if new_token=='or':
            return retARRAYTK(ORTK,token)
        if new_token=='not':
            return retARRAYTK(NOTTK,token)
        return retARRAYTK(ANAGNORTK,token)

   
    elif state==K2:
        num=int(''.join(token))
        if num <= 32767:
            return retARRAYTK(INTEGERTK,token)
        else:
            return retARRAYTK(ERRORTK,token) #error ektos oriwn arithmos
        
    elif EOFflag==1:
        return retARRAYTK(EOFTK,'EOF')
    else:
        return retARRAYTK(ERRORTK,'ERROR')

def parse_while_loop():
    global current_token

    if current_token[0] == WHILETK:
        current_token = lex()
    
        parse_condition()

        if current_token[0] == UPDOWNDOTTK:
            current_token = lex()

            if current_token[0] == COMMENTK:
                current_token = lex()

            if current_token[0] == OBLOCKTK:
                parse_complex_block()        
            elif current_token[0] == ANAGNORTK:
                parse_simple_block()
            elif current_token[0] == RETURNTK and is_in_function_definition != 0:
                current_token = lex()
                if current_token[0] in [MINUSTK, ADDTK, ANAGNORTK, OPARTK,INTEGERTK]:
                    parse_expression() 
            else:
                fail_exit("Expected '#{' or simple block after ':' but got invalid token.")              
        else:
            fail_exit("Expected ':' after while loop but did not get it.")

def parse_if_statement():
    global current_token
    global is_in_function_definition

    if current_token[0] == IFTK:
        current_token = lex()
    
        parse_condition()

        if current_token[0] == UPDOWNDOTTK:
            current_token = lex()

            if current_token[0] == COMMENTK:
                current_token = lex()

            if current_token[0] == OBLOCKTK:
                parse_complex_block()        
            elif current_token[0] == ANAGNORTK:
                parse_simple_block()  
            elif current_token[0] == RETURNTK and is_in_function_definition != 0:
                current_token = lex()
                if current_token[0] in [MINUSTK, ADDTK, ANAGNORTK, OPARTK,INTEGERTK]:
                    parse_expression()
            else:
                fail_exit("Expected '#{' or simple block after ':' but got invalid token.")              
        else:
            fail_exit("Expected ':' after if statement but did not get it.")

    if current_token[0] == ELIFTK:
        current_token = lex()
    
        parse_condition()

        if current_token[0] == UPDOWNDOTTK:
            current_token = lex()

            if current_token[0] == COMMENTK:
                current_token = lex()

            if current_token[0] == OBLOCKTK:
                parse_complex_block()        
            elif current_token[0] == ANAGNORTK:
                parse_simple_block() 
            elif current_token[0] == RETURNTK and is_in_function_definition != 0:
                current_token = lex()
                if current_token[0] in [MINUSTK, ADDTK, ANAGNORTK, OPARTK,INTEGERTK]:
                    parse_expression()

            else:
                fail_exit("Expected '#{' or simple block after ':' but got invalid token.")           
        else:
            fail_exit("Expected ':' after elif statement but did not get it.")

    
    if current_token[0] == ELSETK:
        current_token = lex()

        if current_token[0] == UPDOWNDOTTK:
            current_token = lex()
            if current_token[0] == COMMENTK:
                current_token = lex()

            if current_token[0] == OBLOCKTK:
                parse_complex_block()        
            elif current_token[0] == ANAGNORTK:
                parse_simple_block()
            elif current_token[0] == RETURNTK and is_in_function_definition != 0:
                current_token = lex()
                if current_token[0] in [MINUSTK, ADDTK, ANAGNORTK, OPARTK,INTEGERTK]:
                    parse_expression()
            else:
                fail_exit("Expected '#{' or simple block after ':' but got invalid token.")

        else:
            fail_exit("Expected ':' after else statement but did not get it.")
    return
   
def parse_simple_block():
    global current_token 
    global is_in_function_definition

    current_token = lex()

    if current_token[0] == OPARTK:
        parse_function_call()
    elif current_token[0] == ASSIGNTK:
        current_token = lex()

        parse_expression()
    else:
        fail_exit("Function call '(' or variable assignment '=' expected after alphanumeric")

    return

def parse_complex_block():
    global current_token 

    current_token = lex()
    
    while current_token[0] != CBLOCKTK and current_token[0] != EOFTK and current_token[0] != ERRORTK:
        if (is_in_function_definition != 0):
            if (current_token[0] == RETURNTK):
                current_token = lex()

                if current_token[0] in [MINUSTK, ADDTK, ANAGNORTK, OPARTK,INTEGERTK]:
                    parse_expression()
                continue

        parse_instance()  

    if current_token[0] != CBLOCKTK:    
        if current_token[0] == EOFTK:
            fail_exit("Expected '#}' but EOF reached")
        elif current_token[0] == ERRORTK:
            fail_exit("Got ERROR token from lexxer. Analysis failed.")
    else:
        current_token = lex()
    return



def parse_code_block():
    global current_token 

def statement_or_block():
    global current_token, line 

    if current_token[0] == OBLOCKTK:
        temp_line = line

        current_token = lex()
        
        while current_token[0] != CBLOCKTK:
            if current_token[0] == EOFTK:
                err = "Code block opened in line "+str(temp_line) +" and did not closed before EOF"
                fail_exit(err)
            parse_statement()
        current_token = lex()
    else:
         parse_statement()

def parse_statement():
    global current_token

    if current_token[0] == ANAGNORTK:

        id = current_token[1]  
        current_token = lex()
        
        if current_token[0] == ASSIGNTK:            
            current_token = lex()

            if current_token[0] == INTCASTTK:
                current_token = lex()

                ePlace = parse_int()
                gen_quad("=", ePlace, "_", id)

            else:
                ePlace = parse_expression()            
                gen_quad("=", ePlace, "_", id)
        else:
            fail_exit("Expected '=' on simple statement structure but did not get it")
    elif current_token[0] == PRINTTK:
        parse_print_call()
    elif current_token[0] == RETURNTK:
        ret()

    elif current_token[0] == IFTK:
        parse_if_stat()
    elif current_token[0] == WHILETK:
        # parse_while
        pass
    else:
        fail_exit("Expected simple statement structure but did not get it")


def parse_if_stat():
    global current_token

    B_cond = parse_condition()

    if current_token[0] == UPDOWNDOTTK:
        current_token = lex()

        p1_quad = next_quad()
        print(B_cond[0])
        
        statement_or_block()

        jumps = make_list(next_quad()) 

        gen_quad("JUMP", "_", "_", "_")

        p2_quad = next_quad()

        backpatch(B_cond[0], p1_quad)
        backpatch(B_cond[1], p2_quad)

        if current_token[0] == ELIFTK:
            parse_if_stat()
            p2_quad = next_quad()
        if current_token[0] == ELSETK:
            parse_else()
            
            jump_else = make_list(next_quad()) 
            gen_quad("JUMP", "_", "_", "_")
            p2_quad = next_quad()
            
            jumps = merge(jumps,jump_else)

        backpatch(jumps, p2_quad)

    else:
        fail_exit("Expected ':' after if statement but did not get it")

def parse_else():
    global current_token

    current_token = lex()
    
    if current_token[0] == UPDOWNDOTTK:
        current_token = lex()

        statement_or_block()
    else:
        fail_exit("Expected ':' after if statement but did not get it")    



def parse_condition():
    global current_token
    
    B1 = bool_term()

    while current_token[0] == ORTK:

        backpatch(B1[1], next_quad())

        B2 = bool_term()

        B1[0] = merge(B1[0], B2[0]) # True
        B1[1] = B2[1] # False

    return B1

def bool_term():
    global current_token

    Q1 = bool_factor()

    while current_token[0] == ANDTK:
        backpatch(Q1[0], next_quad())

        Q2 = bool_factor()

        Q1[1] = merge(Q1[1], Q2[1]) # False
        Q1[0] = Q2[0] # True

    return Q1 

def bool_factor():
    global current_token

    not_flag = False

    current_token = lex()

    if current_token[0] == NOTTK:
        not_flag = True
        current_token = lex()

    e1_place = parse_expression()

    relop = current_token[1]

    if current_token[0] not in [LTTK, GTTK, LETK, GETK, EQUALTK, NOT_EQUALTK]:
        fail_exit("Expected comparison token but didn't get it")

    current_token = lex()

    e2_place = parse_expression()

    R_true = make_list(next_quad())
    gen_quad(relop, e1_place, e2_place, "_")

    R_false = make_list(next_quad())

    gen_quad("JUMP", "_", "_", "_",)

    if (not_flag):
        return [R_false, R_true]

    return [R_true, R_false]


def ret():
    global current_token

    current_token = lex()

    tPlace = parse_expression()

    gen_quad("ret", tPlace, "_", "_")

def parse_expression():
    global current_token
    #1 optional sign
    #2 term check gia pollaplasiasmo
    #3 add operation
    #4 mesa sthn while tis add check gia term
    # x + y*5
    t1Place = term()


    while current_token[0] == ADDTK or current_token[0] == MINUSTK:
        op = current_token[1]

        current_token = lex()

        t2Place = term()

        w = new_temp()

        gen_quad(op, t1Place, t2Place, w)

        t1Place = w

    return t1Place
 
def term():
    global current_token
    t1Place = factor()

    while current_token[0] == MULTK or current_token[0] == DIVTK or current_token[0] == MODTK:
        op = current_token[1]

        current_token = lex()

        t2Place = factor()

        w = new_temp()

        gen_quad(op, t1Place, t2Place, w)

        t1Place = w

    return t1Place

def factor():
    global current_token

    sign = ""
    if current_token[0] == MINUSTK:
        sign = "-"
        current_token = lex()
    if current_token[0] == INTEGERTK:
        integer_factor = sign+current_token[1]
        current_token = lex()
        return  integer_factor # integer factor
    elif current_token[0] == OPARTK:
        current_token = lex()
        expression_factor = parse_expression()

        if current_token[0] != CPARTK:
            fail_exit("Expected close parenthesis on factor")
        current_token = lex()

        return expression_factor
    
    elif current_token[0] == ANAGNORTK:
        id = current_token[1]
        
        current_token = lex()
        if current_token[0] == OPARTK:
            
            w = parse_function_call(id, True)

            if sign == "-":
                w_new = new_temp()

                gen_quad("*", w, "-1", w_new)
                current_token = lex()

                return w_new
            else:
                current_token = lex()

                return w               

        elif (sign == "-"):
            w = new_temp()
            gen_quad("*", id, "-1", w)
            return w
        return id
    
def idtail():
    global current_token

    current_token = lex()

    while current_token[0] != CPARTK:
        t1Place = parse_expression()

        gen_quad("PAR",t1Place,"CV","_")

        if current_token[0] == COMMATK:
            current_token = lex()
        elif current_token[0] != CPARTK:
            fail_exit("Expected close parenthesis")


def parse_function_definition_parameters():
    global current_token
    
    if current_token[0] == ANAGNORTK:
        current_token = lex()

        if current_token[0] == COMMATK:
            current_token = lex()

            # recursive check for more parameters
            parse_function_definition_parameters()
        elif current_token[0] != COMMATK:
            if (current_token[0] != CPARTK):
                if current_token[0] == ANAGNORTK:
                    fail_exit("Function definition parameters not separated by ','.")
                else:
                    fail_exit("Function definition parameters not enclosed in ')'.")
            else:
                return
    else:
        fail_exit("Expected alphanumeric after ',' function definition.") 

def parse_function_call(function_name, ret_needed):
    global current_token

    idtail()
    if ret_needed == True:
        w = new_temp()
        gen_quad("PAR", w, "RET", "_")
        gen_quad("call", function_name, "_","_")
        return w
    else:
        gen_quad("call", function_name, "_","_")

def parse_print_call():
    global current_token

    if current_token[0] == PRINTTK:
        current_token = lex()

        if current_token[0] == OPARTK:
            current_token = lex()

            expression_to_print = parse_expression()

            if current_token[0] == CPARTK:
                if expression_to_print == None:
                    expression_to_print = "_" # print without parameter
                gen_quad("out", expression_to_print, "_", "_")
                
                current_token = lex()
            else:
                fail_exit("Expected ')' after print function call but got invalid token.")


        else:
            fail_exit("Expected '(' after print function call but got invalid token.")

def parse_global_declaration():
    global current_token

    if current_token[0] == GLOBALTK:
        current_token = lex()

        if current_token[0] == ANAGNORTK:
            current_token = lex()
        else:
            fail_exit("Expected arphanumeric on global declaration.")

def parse_int_type_declaration():
    global current_token

    if current_token[0] == INTTYPETK:
        current_token = lex()

        if current_token[0] == ANAGNORTK:
            current_token = lex()

            if current_token[0] == COMMATK:
                current_token = lex()

                if current_token[0] == ANAGNORTK:
                    while current_token[0] == ANAGNORTK:
                        current_token = lex()

                        if current_token[0] == COMMATK:
                            current_token = lex()
                            continue
                        else:
                            break
                else:
                    fail_exit("Expected arphanumeric after ',' on #int declaration but did not get it.")

        else:
            fail_exit("Expected arphanumeric on #int declaration.")
    else:
        # no int type declaration found
        return

def parse_function_definition():
    global current_token
    global is_in_function_definition
    if current_token[0] == DEFTK:
        current_token = lex()

        if current_token[0] == ANAGNORTK:
            current_token = lex()

            if (current_token[0] == OPARTK):
                current_token = lex()

                if(current_token[0] == ANAGNORTK):
                    parse_function_definition_parameters()
                if(current_token[0] == CPARTK):
                    current_token = lex()

                    if (current_token[0] == UPDOWNDOTTK):
                        current_token = lex()

                        if current_token[0] == COMMENTK:
                            current_token = lex()

                        if current_token[0] == OBLOCKTK:
                            is_in_function_definition += 1
                            parse_complex_block()
                            is_in_function_definition -= 1
                    
                        else:
                            fail_exit("Expected '#{' after function definition.")
                    else:
                        fail_exit("Expected ':' after function definition.")
                else:
                    fail_exit("Unexpected token instead of ')' on function definition.")
            else:
                fail_exit("Expected '(' on function definition.")
        else:
            fail_exit("Expected alphanumeric on function definition.")
    else:
        # no function definition found
        return 

def parse_int():
    global current_token

    if current_token[0] == OPARTK:
        current_token = lex()

        if current_token[0] == INPUTTK:
            current_token = lex()
            
            if current_token[0] == OPARTK:
                current_token = lex()

                if current_token[0] == CPARTK:
                    current_token = lex()
                    print(current_token[1])

                    if current_token[0] == CPARTK:
                        w = new_temp()

                        gen_quad("inp", "_", "_", w)

                        current_token = lex()

                        return w  
                    
                    else:
                        fail_exit("Expected ')' after 'int(input()' call but did not get it")

                else:
                    fail_exit("Expected ')' after 'input(' call but did not get it")

            else:
                fail_exit("Expected '(' after input call but did not get it")

        else:
            fail_exit("Expected input call after 'int(' cast but did not get it")

    else:
        fail_exit("Expected '(' after int cast but did not get it")
    


def parse_instance():
    global current_token

    if current_token[0] == INTTYPETK:
        parse_int_type_declaration()
    elif current_token[0] == DEF2TK:
        current_token = lex()

        if current_token[0] == MAINTK:
            current_token = lex()
            
        else:
            fail_exit("Expected 'main' after #def but did not get it.")

    elif current_token[0] == WHILETK:
        parse_while_loop()
    elif current_token[0] == GLOBALTK:
        parse_global_declaration()
    elif current_token[0] == IFTK:
        parse_if_stat()
    elif current_token[0] == DEFTK:
        parse_function_definition()
    elif current_token[0] == COMMENTK:
        current_token = lex()
    elif current_token[0] == PRINTTK:
        parse_print_call()
    elif current_token[0] == ANAGNORTK:
        # current token in this case can be a function call or an assignment 
        
        id = current_token[1]  
        current_token = lex()
        
        if current_token[0] == OPARTK:
            parse_function_call(id, False)
        elif current_token[0] == ASSIGNTK:            
            current_token = lex()

            if current_token[0] == INTCASTTK:
                current_token = lex()

                ePlace = parse_int()
                gen_quad("=", ePlace, "_", id)

            else:
                ePlace = parse_expression()            
                gen_quad("=", ePlace, "_", id)
        else:
            fail_exit("Function call '(' or variable assignment '=' expected after alphanumeric")
    elif current_token[0] == ERRORTK:
        fail_exit("Got ERROR token from lexxer. Analysis failed.")

    else:
        print(current_token)
        fail_exit("Invalid token found. Syntax analysis failed.")

    return

def fail_exit(err):
    global line
    print(err+"\nStopped in line:", line)
    exit(0)

def parse():
    global current_token
    current_token = lex()

    while (current_token[0] != EOFTK):
        parse_instance() 
    
    print("EOF reached. Syntax analysis finised succesfully.")

if __name__ == "__main__":
    if len(sys.argv[1:]) == 0:
        print("Pass a .cpy file as an argument.")
    elif len(sys.argv[1:]) > 1:
        print("Pass one .cpy file as an argument. Not more.")
    else:
        file = open(sys.argv[1], 'r')
        parse()
   