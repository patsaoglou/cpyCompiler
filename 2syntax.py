from lex2 import *

# generally before each call lex() is already called

current_token = None

def parse_variable_assignment():
    pass

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
        
        parse_function_call_expression()
        
        while current_token == COMMATK:
            current_token = lex()

            parse_function_call_expression()
        
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
            
        else:
            fail_exit("Expected '(' after print call but got invalid token.")


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
        pass
    elif current_token == DEFTK:
        parse_function_definition()
    elif current_token == COMMENTK:
        pass
    elif current_token == PRINTTK:
        parse_print_call()
    elif current_token == ANAGNORTK:
        # this can be a function call or an assignment 
        current_token = lex()
        
        if current_token == OPARTK:
            parse_function_call()
        elif current_token == ASSIGNTK:
            # assignment
            pass
        else:
            fail_exit("Function call '(' or variable assignment '=' expected after alphanumeric")

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