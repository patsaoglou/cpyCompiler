from lex2 import *

# generally before each call lex() is already called

current_token = None
is_in_function_definition = 0

def parse_while_loop():
    global current_token

    if current_token == WHILETK:
        current_token = lex()
    
        parse_condition()

        if current_token == UPDOWNDOTTK:
            current_token = lex()

            if current_token == OBLOCKTK:
                parse_complex_block()        
            elif current_token == ANAGNORTK:
                parse_simple_block()
            elif current_token == RETURNTK and is_in_function_definition != 0:
                current_token = lex()
                if current_token in [MINUSTK, ADDTK, ANAGNORTK, OPARTK,INTEGERTK]:
                    parse_expression() 
            else:
                fail_exit("Expected '#{' or simple block after ':' but got invalid token.")              
        else:
            fail_exit("Expected ':' after while loop but did not get it.")
        
        print("while statement block close. Current token is: ", current_token)


def parse_if_statement():
    global current_token
    global is_in_function_definition

    if current_token == IFTK:
        current_token = lex()
    
        parse_condition()

        if current_token == UPDOWNDOTTK:
            current_token = lex()

            if current_token == OBLOCKTK:
                parse_complex_block()        
            elif current_token == ANAGNORTK:
                parse_simple_block()  
            elif current_token == RETURNTK and is_in_function_definition != 0:
                current_token = lex()
                if current_token in [MINUSTK, ADDTK, ANAGNORTK, OPARTK,INTEGERTK]:
                    parse_expression()
            else:
                fail_exit("Expected '#{' or simple block after ':' but got invalid token.")              
        else:
            fail_exit("Expected ':' after if statement but did not get it.")
        
        print("if statement block close. Current token is: ", current_token)

    if current_token == ELIFTK:
        current_token = lex()
    
        parse_condition()

        if current_token == UPDOWNDOTTK:
            current_token = lex()

            if current_token == OBLOCKTK:
                parse_complex_block()        
            elif current_token == ANAGNORTK:
                parse_simple_block() 
            elif current_token == RETURNTK and is_in_function_definition != 0:
                current_token = lex()
                if current_token in [MINUSTK, ADDTK, ANAGNORTK, OPARTK,INTEGERTK]:
                    parse_expression()

            else:
                fail_exit("Expected '#{' or simple block after ':' but got invalid token.")           
        else:
            fail_exit("Expected ':' after elif statement but did not get it.")
        print("elif statement block close. Current token is: ", current_token)

    
    if current_token == ELSETK:
        current_token = lex()

        if current_token == UPDOWNDOTTK:
            current_token = lex()

            if current_token == OBLOCKTK:
                parse_complex_block()        
            elif current_token == ANAGNORTK:
                parse_simple_block()
            elif current_token == RETURNTK and is_in_function_definition != 0:
                current_token = lex()
                if current_token in [MINUSTK, ADDTK, ANAGNORTK, OPARTK,INTEGERTK]:
                    parse_expression()
            else:
                fail_exit("Expected '#{' or simple block after ':' but got invalid token.")

        else:
            fail_exit("Expected ':' after else statement but did not get it.")

        print("else statement block close. Current token is: ", current_token)
    return
   

def parse_simple_block():
    global current_token 
    global is_in_function_definition

    current_token = lex()

    if current_token == OPARTK:
        parse_function_call()
    elif current_token == ASSIGNTK:
        current_token = lex()

        parse_expression()
    else:
        fail_exit("Function call '(' or variable assignment '=' expected after alphanumeric")

    return

def parse_complex_block():
    global current_token 

    current_token = lex()
    
    while current_token != CBLOCKTK and current_token != EOFTK and current_token != ERRORTK:
        if (is_in_function_definition != 0):
            if (current_token == RETURNTK):
                current_token = lex()

                if current_token in [MINUSTK, ADDTK, ANAGNORTK, OPARTK,INTEGERTK]:
                    parse_expression()
                continue

        parse_instance()  

    if current_token != CBLOCKTK:    
        if current_token == EOFTK:
            fail_exit("Expected '#}' but EOF reached")
        elif current_token == ERRORTK:
            fail_exit("Got ERROR token from lexxer. Analysis failed.")
    else:
        current_token = lex()
    return

def parse_condition():
    global current_token
    
    if current_token == NOTTK:
        current_token = lex()

    if current_token == ANAGNORTK:
        parse_expression()

        # if current_token == OPARTK:
        #     parse_function_call()

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
    
    if (current_token == INTCASTTK):
            current_token = lex()
            
            if current_token == OPARTK:
                current_token = lex()
                
                if (current_token == INPUTTK):
                    current_token = lex()

                    if (current_token == OPARTK):
                        current_token = lex()

                        if (current_token == CPARTK):
                            current_token = lex()
                            if (current_token == CPARTK):
                                current_token = lex()
                                got_nothing_before_operator = False
                            else:
                                fail_exit("Expected ')' after input but did not get it")
                        else:
                            fail_exit("Expected ')' after Integer casting but did not get it")
                    else:
                        fail_exit("Expected '(' after input but did not get it")
                else:
                    fail_exit("Expected input token after Integer casting but did not get it")
            else:
                fail_exit("Expected ( after Integer casting but did not get it")
    
    
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

def parse_print_call():
    global current_token

    if current_token == PRINTTK:
        current_token = lex()

        if current_token == OPARTK:
            current_token = lex()

            parse_expression()
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
    global is_in_function_definition
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

                        if current_token == COMMENTK:
                            current_token = lex()

                        if current_token == OBLOCKTK:
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
            
def parse_instance():
    global current_token

    if current_token == INTTYPETK:
        parse_int_type_declaration()
    elif current_token == DEF2TK:
        current_token = lex()

        if current_token == MAINTK:
            current_token = lex()
            
        else:
            fail_exit("Expected 'main' after #def but did not get it.")

    elif current_token == WHILETK:
        parse_while_loop()
    elif current_token == GLOBALTK:
        parse_global_declaration()
    elif current_token == IFTK:
        parse_if_statement()
    elif current_token == DEFTK:
        parse_function_definition()
    elif current_token == COMMENTK:
        current_token = lex()
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