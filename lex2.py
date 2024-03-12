#define TOKENS
EOFTK = -1
ERRORTK=-2
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
def lex():
    state=0
    i=0
    element=' '
    next_element=' '
    token=[]
    array=[[0,1,2,ADDTK,3,MULTK,MODTK,DIVTK,ERRORTK,LETK,LTTK,GETK,GTTK,NOT_EQUALTK,ERRORTK,EQUALTK,ASSIGNTK,COMMATK,UPDOWNDOTTK,CPARTK,OPARTK,CBLOCKTK,OBLOCKTK,
           EOFTK,COMMENTK,DEF2TK,ERRORTK,ERRORTK,INTTYPETK,ERRORTK,ERRORTK,ERRORTK,EOFTK,ERRORTK],
           [K1,1,1,K1,K1,K1,K1,K1,K1,K1,K1,K1,K1,K1,K1,K1,K1,K1,K1,K1,K1,K1,K1,K1,K1,K1,K1,K1,K1,K1,K1,K1,K1,K1],
           [K2,K2,2,K2,K2,K2,K2,K2,K2,K2,K2,K2,K2,K2,K2,K2,K2,K2,K2,K2,K2,K2,K2,K2,K2,K2,K2,K2,K2,K2,K2,K2,K2,K2],
           [MINUSTK,MINUSTK,2,MINUSTK,MINUSTK,MINUSTK,MINUSTK,MINUSTK,MINUSTK,MINUSTK,MINUSTK,MINUSTK,MINUSTK,MINUSTK,MINUSTK,MINUSTK,MINUSTK,MINUSTK,MINUSTK,MINUSTK,MINUSTK,MINUSTK,MINUSTK,MINUSTK,MINUSTK,MINUSTK,MINUSTK,MINUSTK,MINUSTK,MINUSTK,MINUSTK,MINUSTK,MINUSTK,MINUSTK]]
            
    while state>=0 and state<100 and i<=31: #i gia na diabazei mexri 30 char + \0 gia anagnwristiko
        element=file.read(1)
        if element.isspace(): 
            index=0
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
            #print(index)
        elif element=='+':
            index=3
            token.append(element)
            #print(index)
        elif element=='-':
            #pos1 = file.tell()
            index=4
            token.append(element)
            
            #print(index)
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
                token.append(next_element)
                index=7 #komple katastasi // 
            else:
                token.append(next_element)
                index=8 #ERROR
                print("Invalid character ", token[-1], "is not expected after a '/' ")
        elif element=='<': #katastasi 4
            token.append(element)
            pos = file.tell()
            next_element=file.read(1)
            if next_element=='=':
                token.append(next_element)
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
                token.append(next_element)
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
                token.append(next_element)
                index=13 #komple katastasi !=
                 
                #file.seek(pos) den xreiazetai 
                print(index)
            else:
                token.append(next_element)
                index=14 #ERROR
                print("Invalid character ", token[-1], "is not expected after a '!' ")
                print("index",index)
        elif element=='=': #katastasi 7
            token.append(element)
            pos = file.tell()
            next_element=file.read(1)
            if next_element=='=':
                token.append(next_element)
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
                #23
                #pos = file.tell()
                while True:
                    #if file.read(1) (epomeno tou while) ==EOF
                    # index=23 #error
                    #break?
                    
                    next_element=file.read(1)
                    if not next_element: #EOF pianei kai kena
                        index=23
                        print(index)
                        break
                    
                    if next_element=='#':#pame sti katastasi 10 exw brei to ena # apo ta 2 gia to kleisimo sxoliou
                        pos = file.tell()
                        #token.append(next_element)
                        next_next=file.read(1)
                        if next_next=='#':
                            index=24 # exoun ## kleisei ta sxolia
                            print(index)
                            #token.append(next_next)
                            state=0
                            break
                            
                    #else:
                        #array.pop()
                        #file.seek(pos) #axristo but check it
                

            elif next_element=='d':
                token.append(element)
                next_element=file.read(1)
                if next_element=='e':
                    token.append(next_element)
                    next_element=file.read(1)
                    if next_element=='f':
                        token.append(next_element)
                        index=25 # #def
                    else:
                        index=26 #error
                else:
                    index=27 #ERROR
                        
                    
                

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
                        index=29 #error
                else:
                    index=30 #error

            else:
                 index=31 #error den akolouthei meta to # kati apo ta orismena
                 print(index)

        elif not element: #EOF
            index=32
            print(index)
            return EOFTK
        else:
            index=33 #error
        #token.append(element)
        #token.append(next_element)
        if i >=31:
            index=0 #ipervenei ta 30 char
        state=array[state][index]
        
    if state<0:    
        print ("state:",state)
    print(token[:])

    if state==K1 or state==K2:# or state==MINUSTK:
       # if state==K2 and not token[-1].isdigit():
            file.seek(pos1) #epistrefoume stin proigoumeni thesi afou exoume krifokoitaxei to epomeno
         # afairei to epomeno pou exoume dei apo to token
            if (token[-1].isalpha() == False):
                token.pop()


    if state >=100:
        print ("State: (>=100)",state)
        print(token[:])
        return state
    elif state==K1:
        print ("State:",state)
        
        new_token=''.join(token)
        print(new_token)
        print("len",len(new_token))
        if new_token=='main':
            return MAINTK
        if new_token=='def':
            print(DEFTK)
            return DEFTK
        if new_token=='#def':
            return DEF2TK
        if new_token=='#int':
            print(INTTYPETK)
            return INTTYPETK
        if new_token=='global':
            print(GLOBALTK)
            return GLOBALTK
        if new_token=='if':
            return IFTK
        if new_token=='elif':
            return ELIFTK
        if new_token=='else':
            return ELSETK
        if new_token=='while':
            return WHILETK
        if new_token=='print':
            return PRINTTK
        if new_token=='return':
            return RETURNTK
        if new_token=='input':
            return INPUTTK
        if new_token=='int':
            return INTCASTTK
        if new_token=='and':
            return ANDTK
        if new_token=='or':
            return ORTK
        if new_token=='not':
            return NOTTK
        
        return ANAGNORTK

    elif state==K2:
        print((''.join(token)))
        return INTEGERTK
        
# ret = lex()  
# print("TokenCode:", ret)   
# while(ret != EOFTK):
#     input()  
#     ret = lex()
#     print("TokenCode:", ret)   



