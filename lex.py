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

FILEPATH = "test.cpy"
file = open(FILEPATH,"r")
token = ""
line=1
retArray=[]

def retARRAYTK(state,token):
    global retArray
    retArray=[]
    retArray.append(state)
    retArray.append(''.join([char for char in token if not char.isspace()]))
    return retArray

def lex():
    global line
    global retArray
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
                print(index)
            else:
                index=10 #<
                file.seek(pos) #xreiazetai gt exw koitaxei to epomeno kai den einai to = opote prepeina epistrafei
                print(index)
        elif element=='>': #katastasi 5
            token.append(element)
            pos = file.tell()
            next_element=file.read(1)
            if next_element=='=':
                token.pop()
                token.append('>=')
                index=11 #>=
                print(index)
            else:
                index=12 #>
                file.seek(pos) #xreiazetai gt exw koitaxei to epomeno kai den einai to = opote prepeina epistrafei
                print(index)
        elif element=='!': #katastasi 6
            token.append(element)
            pos = file.tell() #thesi mesa sto arxeio prin diabasw to epomeno xaraktira gia na dw sw ti katastasi kattaligw
            next_element=file.read(1) #thelei epistrofi
            if next_element=='=':
                token.pop()
                token.append('!=')
                index=13 #komple katastasi !=
                print(index)
            else:
                token.append(next_element)
                index=14 #ERROR
                print("Invalid character ", token[-1], "is not expected after a '!' in line ",line)
                print("index",index)
        elif element=='=': #katastasi 7
            token.append(element)
            pos = file.tell()
            next_element=file.read(1)
            if next_element=='=':
                token.pop()
                token.append('==')
                index=15 #==
                print(index)
            else:
                index=16 #=
                file.seek(pos) #xreiazetai gt exw koitaxei to epomeno kai den einai to = opote prepeina epistrafei
                print(index)
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
                while True:                    
                    next_element=file.read(1)
                    if not next_element: #EOF pianei kai kena
                        index=23 #array error bazw anti eoftk
                        print(index)
                        print("EOF: Open comments and not closed ")
                        EOFflag=1
                        break
                    
                    if next_element=='#':#pame sti katastasi 10 exw brei to ena # apo ta 2 gia to kleisimo sxoliou
                        pos = file.tell()
                        next_next=file.read(1)
                        if next_next=='#':
                            index=24 # exoun ## kleisei ta sxolia
                            print(index)
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
            
        print('line',line)
        if i >=31:
            index=0 #ipervenei ta 30 char
        state=array[state][index]
        
    if state==K1 or state==K2:# or state==MINUSTK:
            if not element.isspace(): #elegxos den einai kenos char na epistrefei stin proigoumeni thesi (an einai kenos apla katanalwnetai kai proxwrame)
                file.seek(pos1) #epistrefoume stin proigoumeni thesi afou exoume krifokoitaxei to epomeno
            token.pop() ########################################################################################################################

    
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
        if abs(num) <= 32767: #den thelei abs
            return retARRAYTK(INTEGERTK,token)
        else:
            return retARRAYTK(ERRORTK,token) #error ektos oriwn arithmos
        
    elif EOFflag==1:
        return retARRAYTK(EOFTK,'EOF')
    else:
        return retARRAYTK(ERRORTK,'ERROR') # itan ERRORTK

        
ret = lex()  
print("TokenCode:", ret)   
while(ret != EOFTK and ret != ERRORTK):
     input()  
     ret = lex()
     print("TokenCode:", ret)   




    