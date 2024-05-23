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

# ---------------------- Pinakas Sym ---------------------- #
assembly_file = None
sym_file = None
scope_list = []
current_scope_level = 0

class Entity:
    def __init__(self, name, offset = None, label = None, arguments = None, framelength = None, type = "NOT_GLOBAL"):
        self.name = name
        self.offset = offset
        self.label = label
        self.arguments = arguments if arguments is not None else []
        self.framelength = framelength
        self.type = type

    def __str__(self):
        return f"Name: {self.name}, Offset: {self.offset}, Label: {self.label}, Arguments: {self.arguments}, Framelength: {self.framelength}, Type: {self.type}"

class Scope:
    def __init__(self, name, level = 0):
        self.name = name
        self.level = level
        self.entities = []
        self.previous_offset = 0

    def add_entity(self, entity):
        self.entities.append(entity)

    def __str__(self):
        entity_list = "\n".join([f"\t{entity}" for entity in self.entities])
        return f"\n\nScope Name: {self.name}, Level: {self.level}\nEntities:\n{entity_list}"

def create_scope(name):
    global current_scope_level
    scope = Scope(name, current_scope_level)
    scope_list.append(scope)
    current_scope_level += 1
    return scope

def close_scope():
    global current_scope_level, scope_list 

    if scope_list:
        sym_out(scope_list)
        last_scope = scope_list.pop()

        last_entity_with_offset = len(last_scope.entities) - 1
        while(last_scope.entities[last_entity_with_offset].offset == None):
            last_entity_with_offset-=1

            if(last_entity_with_offset<0):
                current_scope_level -= 1        

                scope_list[current_scope_level-1].entities[-1].framelength = 12
                return

        framelength = last_scope.entities[last_entity_with_offset].offset + 4
        current_scope_level -= 1        

        scope_list[current_scope_level-1].entities[-1].framelength = framelength

def add_entity(newEntity, isFuction = False, isGlobal = False):
    global current_scope_level, scope_list

    scope_entity_list = scope_list[current_scope_level-1].entities

    if isFuction == False and isGlobal == False:
        
        if len(scope_entity_list) == 0:
            scope_list[current_scope_level-1].previous_offset = 12
            newEntity.offset = scope_list[current_scope_level-1].previous_offset
        else:
            if scope_list[current_scope_level-1].previous_offset == 0:
                scope_list[current_scope_level-1].previous_offset = 12
            else:
                scope_list[current_scope_level-1].previous_offset += 4
            newEntity.offset = scope_list[current_scope_level-1].previous_offset

    if isGlobal:
        newEntity.type = "GLOBAL"
        
    scope_entity_list.append(newEntity)  


# -----------------------Voithitikes----------------------- #
block_name_list = []
endblock = []

# --------------------------Telikos------------------------ #
assembly_quads = []
assembly_label_counter = 0
starting_quad = 0
ending_quad = 0
function_par = []
is_in_main_block = False
# Do something in case of Globals
def gnlvcode(v):
    global current_scope_level, scope_list, assembly_quads 
    
    check_scope = current_scope_level - 2
    entity_found = None
    
    assembly_out("      lw t0,-4(sp)")

    while (check_scope >=0):
        for entity in scope_list[check_scope].entities:
            if entity.offset == None:
                break
            if entity.name == v:
                entity_found = entity
                break
        check_scope -= 1
        assembly_out("      lw t0,-4(t0)")
    
    if entity_found:
        assembly_out("      addi t0,t0,-"+str(entity_found.offset))
    else:
        int_out()
        fail_exit("Variable '"+v+"' not found in parent scopes")

def gnlvcode_local(v, reg, is_storing = False):
    global current_scope_level,scope_list,assembly_quads 
    entity_found = None
    check_scope = current_scope_level - 1
    # print(check_scope)
    
    for entity in scope_list[check_scope].entities:
        if entity.offset == None and entity.type == "GLOBAL":
            break
        if entity.name == v:
            entity_found = entity
            break
    
    if entity_found:
        if is_storing:
            assembly_out("      sw "+reg+",-"+str(entity_found.offset)+"(sp)")
        else:
            assembly_out("      lw "+reg+",-"+str(entity_found.offset)+"(sp)")

    return entity_found

def gnlvcode_global(v, reg, is_storing = False):
    global current_scope_level,scope_list,assembly_quads 
    entity_found = None
    check_scope = current_scope_level - 1
    
    for entity in scope_list[check_scope].entities:
        if entity.name == v and entity.type == "GLOBAL":
            entity_found = entity
            break
    
    if entity_found:
        if is_storing:
            assembly_out("      sw "+reg+",-"+str(entity_found.offset)+"(gp)")
        else:
            assembly_out("      lw "+reg+",-"+str(entity_found.offset)+"(gp)")

    return entity_found

def loadvr(v, reg):
    global assembly_quads
    
    if v.isdigit():
        assembly_out("      li "+reg+","+str(v))

    elif gnlvcode_local(v, reg) != None:
        return
    elif gnlvcode_global(v, reg) != None:
        return
    else: # progonous
        gnlvcode(v)
        assembly_out("      lw "+reg+",(t0)")

def storerv(reg, v):
    if gnlvcode_local(v, reg, True) != None:
        return
    elif gnlvcode_global(v, reg, True) != None:
        return
    else:
        gnlvcode(v)
        assembly_out("      sw "+reg+",(t0)")

def assembly_quad_from_quad(quad):
    global starting_quad, function_par, endblock
    
    if quad[1] == "JUMP":
        assembly_out("L"+str(quad[0])+":")

        assembly_out("      j L"+str(quad[4]))

    elif quad[1] == '=':
        if quad[2].isdigit() or quad[2].isalpha() or 'T_' in quad[2]:
            assembly_out("L"+str(quad[0])+":")
            loadvr(quad[2],"t0")
            storerv("t0", quad[4])
    elif quad[1] in ["+","-","%","//","*"]:
        assembly_out("L"+str(quad[0])+":")
        loadvr(quad[2],"t1")
        loadvr(quad[3],"t2")
        
        if quad[1] == "+":
            assembly_out("      add t1, t2, t1") 
        elif quad[1] == "-":
            assembly_out("      sub t1, t2, t1")  
        elif quad[1] == "*":
            assembly_out("      mul t1, t2, t1") 
        elif quad[1] == "%":
            assembly_out("      rem t1, t2, t1")  
        elif quad[1] == "//":
            assembly_out("      div t1, t2, t1")  
        storerv("t1",quad[4])
    elif quad[1] in ["<","<=",">=",">","==","!="]:
        assembly_out("L" + str(quad[0]) + ":")
        loadvr(quad[2], "t1")
        loadvr(quad[3], "t2")

        if quad[1] == "<":
            assembly_out("      blt t1, t2, L" + str(quad[4]))
        elif quad[1] == "<=":
            assembly_out("      ble t1, t2, L" + str(quad[4]))
        elif quad[1] == ">":
            assembly_out("      bgt t1, t2, L" + str(quad[4]))
        elif quad[1] == ">=":
            assembly_out("      bge t1, t2, L" + str(quad[4])) 
        elif quad[1] == "==":
            assembly_out("      beq t1, t2, L" + str(quad[4])) 
        elif quad[1] == "!=":
            assembly_out("      bne t1, t2, L" + str(quad[4]))

    elif quad[1] == "call":
        if len(endblock)> 0 and endblock[-1] == quad[2]:
            function_entity = search_function(quad[2], True)
            print(scope_list[-1].__str__())
        else:
            function_entity = search_function(quad[2], False)

        actual_par_len = len(function_entity[0].arguments)
        par_len = len(function_par)

        if function_par[-1][3] == "RET":
            par_len -= 1

        if par_len != actual_par_len:
            fail_exit("Funtion call parameter number not same as in declaration")

        call_function(quad, function_entity)


    elif quad[1] == "PAR":
        function_par.append(quad)            


def call_function(quad, function_entity):
    global function_par, endblock, is_in_main_block
    caller_scope = 0

    if len(endblock)>0:
        caller_scope = search_function(endblock[-1], True)[1]


    if len(function_par) != 0:
        initial_par_offset = 12
        idx = 0

        for par in function_par:
            if idx == 0:
                assembly_out("L" + str(par[0]) + ":")
                assembly_out("      addi fp, sp,"+str(function_entity[0].framelength))
            if par[3] == "CV":
                if idx != 0:
                    assembly_out("L" + str(par[0]) + ":")
                loadvr(par[2], "t1")
                assembly_out("      sw t1, -"+str(initial_par_offset)+"(fp)")
                initial_par_offset+=4
            elif par[3] == "RET":
                if idx != 0:
                    assembly_out("L" + str(par[0]) + ":")
                assembly_out("      add t0, sp,-"+str(ret_offset(par[2])))
                assembly_out("      sw t0, -8(fp)")                
            idx+=1
        assembly_out("L" + str(quad[0]) + ":")
        

    else:
        assembly_out("L" + str(quad[0]) + ":")
        assembly_out("      addi fp, sp,"+str(function_entity[0].framelength))

    if (caller_scope == function_entity[1]) and is_in_main_block == False: # if entities are brothers in the same scope
        assembly_out("      lw t0, -4(sp)")
        assembly_out("      sw t0, -4(fp)")
    else:    
        assembly_out("      sw sp, -4(fp)")
    assembly_out("      addi sp, sp,"+str(function_entity[0].framelength))
    assembly_out("      jal L"+str(function_entity[0].label))
    assembly_out("      addi sp, sp,-"+str(function_entity[0].framelength))
    
    function_par = []
    
    return function_entity[0]

def ret_offset(v):
    global current_scope_level, scope_list, assembly_quads 
    
    check_scope = current_scope_level - 1
    entity_found = None

    for entity in scope_list[check_scope].entities[::-1]:
        if entity.name == v:
            entity_found = entity
            break
    
    if entity_found:
        return entity_found.offset
    else:
        fail_exit("Variable '"+v+"' not found in parent scopes")


def search_function(function_name, is_from_scope_check = False):
    global current_scope_level, scope_list
    starting_scope = current_scope_level - 1
    function_entity = None

    while starting_scope >= 0 and function_entity== None:
        for entity in scope_list[starting_scope].entities[::-1]:
            if entity.name == function_name and is_from_scope_check:
                function_entity = entity
                break 
            if entity.name == function_name and entity.framelength != None:
                function_entity = entity
                break 
        if function_entity == None:
            starting_scope-=1

    if function_entity == None:
        fail_exit("Function that is called cannot be found in known scopes."+ str(is_from_scope_check))
    
    return [function_entity, starting_scope]



def gen_assembly_fuction_quads():
    global quadsList, starting_quad # global because issue in case of nested function declaration
    # print(starting_quad)          # starting quad of parent not the initial quad 
                                    # we dont want start again regenarating child function
    while(quadsList[starting_quad][1] != "end_block"):
        assembly_quad_from_quad(quadsList[starting_quad])
        starting_quad +=1
    starting_quad += 1  # begin quad of parent fuction (end_block child + 1 quad for parent's)
    

def gen_assembly_main_quads(starting_quad):
    global quadsList
    
    assembly_out("Lmain:")
    assembly_out("      addi sp,sp,"+ str(get_main_framelength()))
    assembly_out("      mv gp,sp")
    
    while(quadsList[starting_quad][1] != "end_main"):
        assembly_quad_from_quad(quadsList[starting_quad])
        starting_quad +=1
    
    assembly_out("L"+str(quadsList[starting_quad][0]) +":")
    assembly_out("      li a0,0")
    assembly_out("      li a7,93")
    assembly_out("      ecall")

    
    

def get_main_framelength():
    global scope_list

    return scope_list[0].entities[-1].offset + 4




# --------------------------------------------------------- #
# ---------------------- Symasiologikos ---------------------- #


# --------------------------------------------------------- #
# ------------------------------------------------------------------- #
def gen_quad(op, op1, op2, op3):
    global quadsList
    global quadNum

    newQuad = [quadNum, op, op1, op2, op3]

    quadsList.append(newQuad)
    quadNum += 1
    
    # print(newQuad)

def new_temp():
    global tempNum

    newTemp = "T_" + str(tempNum)
    tempNum += 1
    
    temp_entity = Entity(newTemp)
    add_entity(temp_entity)

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
        parse_while_stat()
    else:
        err = "Expected statement structure but did not get it. Got '" + current_token[1] + "'."
        fail_exit(err)

def parse_while_stat():
    global current_token

    B_quad = next_quad()

    B_cond = parse_condition()

    if current_token[0] == UPDOWNDOTTK:
        current_token = lex()
        
        backpatch(B_cond[0], next_quad())

        statement_or_block() 

        gen_quad("JUMP", "_", "_", B_quad)

        backpatch(B_cond[1], next_quad())
    else:
        fail_exit("Expected ':' after while statement but did not get it")

def parse_if_stat():
    global current_token

    B_cond = parse_condition()

    if current_token[0] == UPDOWNDOTTK:
        current_token = lex()

        p1_quad = next_quad()
        
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
    else:
        fail_exit("Expected factor after operator but did not get it. Got '" + current_token[1] +"'.")
    
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

        parse_id_list(isGlobal = True)

def parse_int_type_declaration():
    global current_token

    if current_token[0] == INTTYPETK:
        current_token = lex()
        
        parse_id_list()

def parse_id_list(isParam = False, isGlobal = False):
    global current_token, current_scope_level, scope_list
    if current_token[0] == ANAGNORTK:
        
        entity = Entity(current_token[1])
        
        add_entity(entity, isGlobal = isGlobal)
        if isParam == True:
            last_entity = scope_list[current_scope_level-2].entities[-1]
            last_entity.arguments.append(entity.name)
        current_token = lex()

        if current_token[0] == COMMATK:
            current_token = lex()

            if current_token[0] == ANAGNORTK:
                while current_token[0] == ANAGNORTK:

                    entity = Entity(current_token[1])

                    add_entity(entity, isGlobal = isGlobal)
                    if isParam == True:
                        last_entity = scope_list[current_scope_level-2].entities[-1]
                        last_entity.arguments.append(entity.name)
        
                    current_token = lex()

                    if current_token[0] == COMMATK:
                        current_token = lex()
                        continue
                    else:
                        break
            else:
                fail_exit("Expected arphanumeric after ',' on declaration but did not get it (ID_LIST).")

    else:
        fail_exit("Expected arphanumeric on declaration (ID_LIST).")

def parse_function_definition():
    global current_token, block_name_list, starting_quad, ending_quad, endblock

    if current_token[0] == DEFTK:
        current_token = lex()

        if current_token[0] == ANAGNORTK:
            block_name_list.append(current_token[1])
            endblock.append(current_token[1])
            gen_quad("begin_block",current_token[1],"_","_")
            
            starting_quad = next_quad() - 1
            assembly_out("L" + str(starting_quad) + ":")

            entity = Entity(current_token[1])
            entity.label = next_quad()
            add_entity(entity, True)

            create_scope(current_token[1])

            current_token = lex()

            if (current_token[0] == OPARTK):
                current_token = lex()
                
                if current_token[0] != CPARTK:
                    parse_id_list(True)

                if(current_token[0] == CPARTK):
                    current_token = lex()

                    if (current_token[0] == UPDOWNDOTTK):
                        current_token = lex()

                        check_for_comment()

                        if current_token[0] == OBLOCKTK:
                            current_token = lex()
                            check_for_comment()

                            parse_function_block()
                            
                            ending_quad = next_quad()
                            
                            gen_quad("end_block",block_name_list.pop(),"_","_")
    
                            gen_assembly_fuction_quads()
                            assembly_out("L" + str(next_quad()-1) + ":")
                            
                            endblock.pop()
                            close_scope()
                            
                                                        
                            current_token = lex()

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

    # no function definition found

def parse_function_block():
    global current_token

    # DECLARATIONS #INT
    while current_token[0] == INTTYPETK:
        parse_int_type_declaration()
        check_for_comment()

    check_for_comment()

    # FUNCTIONS
    while current_token[0] == DEFTK:
        parse_function_definition()
        check_for_comment()

    check_for_comment()
    # DECLARATIONS GLOBALS
    while current_token[0] == GLOBALTK and current_token[0] != INTTYPETK and current_token[0] != DEFTK:
        parse_global_declaration()
        check_for_comment()

    if current_token[0] == INTTYPETK:
        fail_exit("Int variables must be declared first in function definitions.")
    elif current_token[0] == DEFTK:
        fail_exit("Nested function definitions must be declared before global variables.")
    check_for_comment()
    parse_statement()

    # CODE BLOCK - STATEMENTS
    while current_token[0] != CBLOCKTK and current_token[0] != INTTYPETK and current_token[0] != DEFTK and current_token[0] != GLOBALTK:
        parse_statement()
        check_for_comment()

    if current_token[0] == INTTYPETK:
        fail_exit("Int variables must be declared first in function definitions.")
    elif current_token[0] == DEFTK:
        fail_exit("Nested function definitions must be declared before code block in function definitions.")
    elif current_token[0] == GLOBALTK:
        fail_exit("Global variables must be declared before code block in function definitions.")

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

def check_for_comment():
    global current_token   

    if current_token[0] == COMMENTK:
        current_token = lex()

def parse_main():
    global current_token
    
    if current_token[0] == MAINTK:
        current_token = lex()
        
        check_for_comment()
        
        # DECLARATIONS #INT
        while current_token[0] == INTTYPETK:
            parse_int_type_declaration()
            check_for_comment()

        check_for_comment()

        parse_statement()
        while current_token[0] != EOFTK:
            parse_statement()
            check_for_comment()
    else:
        fail_exit("Expected 'main' after #def but did not get it. Got '" + current_token[1]+ "'.")

def parse_program():
    global current_token, scope_list, current_scope_level, assembly_label_counter, is_in_main_block
    
    create_scope("PROGRAM")
    
    assembly_out("L0:\n     j Lmain")
    
    # DECLARATIONS #INT
    while current_token[0] == INTTYPETK:
        parse_int_type_declaration()
        check_for_comment()

    check_for_comment()

    # FUNCTIONS
    while current_token[0] == DEFTK:
        parse_function_definition()
        check_for_comment()

    check_for_comment()
    
    if current_token[0] == DEF2TK:
        current_token = lex()

        is_in_main_block = True
        gen_quad("begin_main","_","_","_")
        main_starting_quad = next_quad() - 1

        parse_main()

        gen_quad("halt","_","_","_")

        gen_quad("end_main","_","_","_")
        
        gen_assembly_main_quads(main_starting_quad)

    else:
        fail_exit("Did not found main declaration. Got '" + current_token[1] + "'.")

def fail_exit(err):
    global line
    print(err+"\nStopped in line:", line)
    exit(0)

def parse():
    global current_token, assembly_file
    current_token = lex()

    parse_program()

    if current_token[0] == ERRORTK:
        fail_exit("Got ERROR token from lexxer. Analysis failed.")
       
    int_out()
    sym_out(scope_list)
    print("\nEOF reached. Syntax analysis finised succesfully.")


def assembly_out(assembly_quad):
    global assembly_file
    
    if assembly_file is None:
        name = sys.argv[1].split(".")[0]
        assembly_file = open(name+".s", "w")
  
    assembly_file.write("\n"+assembly_quad)    
    
def sym_out(scopelist_state):
    global sym_file

    if sym_file is None:
        name = sys.argv[1].split(".")[0]
        sym_file = open(name+".sym", "w")

    sym_file.write("\n\n################################################################\n\n")

    for scope in scope_list:
        sym_file.write(scope.__str__())

    if current_scope_level == 1:
        sym_file.close()

def int_out():
    global quadsList

    name = sys.argv[1].split(".")[0]
    int_file = open(name+".int", "w")

    for quad in quadsList:
        line = str(quad[0])+" "+quad[1]+" "+quad[2]+" "+quad[3]+" "+str(quad[4])
        # print(line)
        int_file.write(line+"  \n")

    int_file.close()

if __name__ == "__main__":
    if len(sys.argv[1:]) == 0:
        print("Pass a .cpy file as an argument.")
    elif len(sys.argv[1:]) > 1:
        print("Pass one .cpy file as an argument. Not more.")
    else:
        file = open(sys.argv[1], 'r')
        parse()
   