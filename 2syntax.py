from lex2 import *

# generally before each call lex() is already called

current_token = None

def parse_if_statement():
    global current_token

    if current_token == IFTK:
        current_token = lex()
    
        parse_condition()

        if current_token == UPDOWNDOTTK:
            current_token = lex()

            if current_token == OBLOCKTK:

                current_token = lex()
                
                while current_token != CBLOCKTK:
                    parse_instance()
                    current_token = lex()   
            elif current_token == ANAGNORTK:
           
                current_token = lex()
                
                if current_token == OPARTK:
                    parse_function_call()
                elif current_token == ASSIGNTK:
                    current_token = lex()

                    parse_expression()
                else:
                    fail_exit("Function call '(' or variable assignment '=' expected after alphanumeric")
                print("basic if block finished")

        else:
            fail_exit("Expected ':' after if statement but did not get it.")
    
def parse_condition():
    global current_token

    if current_token == ANAGNORTK:
        current_token = lex()

        if current_token in [LTTK, GTTK, LETK, GETK, EQUALTK, NOT_EQUALTK]:
            current_token = lex()
            
            parse_expression()
            if current_token == UPDOWNDOTTK:
                return
        else:
            fail_exit("Expected comparison token token but did not get it.")
        if current_token in [ANDTK, ORTK]: #not 
            while current_token in [ANDTK, ORTK]:
                current_token = lex()
                parse_condition()

    elif current_token == OPARTK:
        current_token = lex()
        
        parse_condition()
        
        if current_token != CPARTK:
            fail_exit("Expected ')' on condition but did not get it")
        else: 
            current_token = lex()
    else:
        fail_exit("Expected comparison or '(' on condition but did not get it")


def parse_expression():
    global current_token
    
    got_nothing_before_operator = True
    if current_token == MINUSTK or current_token == ADDTK:
        current_token = lex()

    if current_token == ANAGNORTK:
        current_token = lex()

        got_nothing_before_operator = False

        if current_token == OPARTK:
            parse_function_call()      

    elif current_token == OPARTK:
        current_token = lex()

        got_nothing_before_operator = False

        parse_expression()
            
        if current_token == CPARTK:
            current_token = lex()
        else:
            fail_exit("Expected ')' after '(' in expression.")


    elif current_token == INTEGERTK:
        current_token = lex()

        got_nothing_before_operator = False

    if got_nothing_before_operator == False:
        print("In operator check:", current_token)
        if current_token in [ADDTK, MINUSTK, MULTK, DIVTK, MODTK]:
            current_token = lex()
            parse_expression()
        else:
            print("Return from parse_expression")
            return
        
    
    else:
       fail_exit("Expected AlphaNumeric, '(' or Integer after operator but got invalid token.")


def parse_function_definition_parameters():
    global current_token
    
    if current_token == ANAGNORTK:
        current_token = lex()

        if current_token == COMMATK:
            current_token = lex()

            # recursive check for more parameters
            parse_function_definition_parameters()
        elif current_token != COMMATK:
            if (current_token != CPARTK):
                if current_token == ANAGNORTK:
                    fail_exit("Function definition parameters not separated by ','.")
                else:
                    fail_exit("Function definition parameters not enclosed in ')'.")
            else:
                return
    else:
        fail_exit("Expected alphanumeric after ',' function definition.") 

def parse_function_call():
    global current_token

    if current_token == OPARTK:
        current_token = lex()
        
        if (current_token == CPARTK):
            current_token = lex()
            return
        parse_expression()
        
        while current_token == COMMATK:
            current_token = lex()

            parse_expression()
            print("ret")
        
        if current_token == CPARTK:
            current_token = lex()
        else:
            fail_exit("Function call expressions not enclosed in ')'.")
        
    else:
        fail_exit("Expected '(' after alphanumeric on function call.")

def parse_function_call_expression():
    global current_token

    if current_token == ANAGNORTK:
        current_token = lex()
        
        if current_token == OPARTK:
            parse_function_call()
    elif current_token == INTEGERTK:
        current_token = lex()
    elif current_token != CPARTK:
        fail_exit("Expected alphanumeric/fuction call/integer but got invalid token.")

def parse_print_call():
    global current_token

    if current_token == PRINTTK:
        current_token = lex()

        if current_token == OPARTK:
            current_token = lex()

            parse_function_call_expression()
            if current_token == CPARTK:
                current_token = lex()

                return
            else:
                fail_exit("Expected ')' after print function call but got invalid token.")


        else:
            fail_exit("Expected '(' after print function call but got invalid token.")


def parse_global_declaration():
    global current_token

    if current_token == GLOBALTK:
        current_token = lex()

        if current_token == ANAGNORTK:
            current_token = lex()
        else:
            fail_exit("Expected arphanumeric on global declaration.")


def parse_int_type_declaration():
    global current_token

    if current_token == INTTYPETK:
        current_token = lex()

        if current_token == ANAGNORTK:
            current_token = lex()
        else:
            fail_exit("Expected arphanumeric on #int declaration.")
    else:
        # no int type declaration found
        return

def parse_function_definition():
    global current_token

    if current_token == DEFTK:
        current_token = lex()

        if current_token == ANAGNORTK:
            current_token = lex()

            if (current_token == OPARTK):
                current_token = lex()

                if(current_token == ANAGNORTK):
                    parse_function_definition_parameters()
                if(current_token == CPARTK):
                    current_token = lex()

                    if (current_token == UPDOWNDOTTK):
                        current_token = lex()

                        if current_token == OBLOCKTK:
                            current_token = lex()
                            
                            while current_token != CBLOCKTK:
                                input()
                                parse_instance()
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
            
def parse_instance():
    global current_token

    if current_token == INTTYPETK:
        parse_int_type_declaration()
    elif current_token == WHILETK:
        pass
    elif current_token == GLOBALTK:
        parse_global_declaration()
    elif current_token == IFTK:
        parse_if_statement()
    elif current_token == DEFTK:
        parse_function_definition()
    elif current_token == COMMENTK:
        pass
    elif current_token == PRINTTK:
        parse_print_call()
    elif current_token == ANAGNORTK:
        # current token in this case can be a function call or an assignment 
        current_token = lex()
        
        if current_token == OPARTK:
            parse_function_call()
        elif current_token == ASSIGNTK:
            current_token = lex()

            parse_expression()
        else:
            fail_exit("Function call '(' or variable assignment '=' expected after alphanumeric")
    elif current_token == ERRORTK:
        fail_exit("Got ERROR token from lexxer. Analysis failed.")

    else:
        fail_exit("Invalid token found. Syntax analysis failed.")

    return

def fail_exit(err):
    print(err)
    exit(0)

def parse():
    global current_token
    current_token = lex()

    while (current_token != EOFTK):
        input()
        parse_instance() 
    
    print("EOF reached. Syntax analysis finised succesfully.")

parse()