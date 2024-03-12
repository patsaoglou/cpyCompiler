# Token codes
INTTYPETK = 1
ALFA = 2
OPENCURLYBRACKET = 3
CLOSECURLYBRACKET = 4
OPERATOR = 5
RETURN = 6
NEWLINE = 7
WHILE = 8
IF = 9
ELSE = 10
ELIF = 11
GLOBAL = 12
INPUT = 13
PRINT = 14
NUMBER = 15

# Global variables to store token information
current_token = None

# Mockup function lex() to get the next token
def lex():
    global current_token
    # Assume some mechanism to get the next token
    # Return token code based on the input code
    current_token = getNextToken()
    return current_token

# Parsing function for #int counterFunctionCalls
def parse_int_declaration():
    global current_token
    if current_token == INTTYPETK:
        lex()  # Consume INTTYPETK token
        if current_token == ALFA:
            lex()  # Consume ALFA token
        else:
            raise SyntaxError("Variable name expected after 'int'")
    else:
        raise SyntaxError("'#int' declaration expected")

# Parsing function for function definition
def parse_function_definition():
    global current_token
    if current_token == ALFA:
        lex()  # Consume function name
        if current_token == OPENCURLYBRACKET:
            lex()  # Consume '{'
            # Parse function body
            while current_token != CLOSECURLYBRACKET:
                parse_statement()
            if current_token == CLOSECURLYBRACKET:
                lex()  # Consume '}'
            else:
                raise SyntaxError("Expected '}' after function body")
        else:
            raise SyntaxError("Expected '{' after function name")
    else:
        raise SyntaxError("Function name expected")

# Parsing function for statements
def parse_statement():
    global current_token
    if current_token == ALFA:
        lex()  # Consume ALFA token
        if current_token == OPERATOR and getCurrentTokenValue() == "=":
            lex()  # Consume OPERATOR token
            parse_expression()  # Parse expression
        elif current_token == OPENCURLYBRACKET:
            parse_function_definition()  # Parse nested function definition
        else:
            raise SyntaxError("Assignment operator '=' or '{' expected after variable/function name")
    elif current_token == WHILE:
        parse_while_loop()
    elif current_token == IF:
        parse_if_statement()
    elif current_token == GLOBAL:
        parse_global_statement()
    elif current_token == INPUT:
        parse_input_statement()
    elif current_token == PRINT:
        parse_print_statement()
    else:
        raise SyntaxError("Unexpected token")

# Parsing function for expressions
def parse_expression():
    global current_token
    # Placeholder for expression parsing logic
    pass

# Parsing function for while loops
def parse_while_loop():
    global current_token
    if current_token == WHILE:
        lex()  # Consume WHILE token
        parse_expression()  # Parse condition expression
        if current_token == OPENCURLYBRACKET:
            lex()  # Consume '{'
            # Parse loop body
            while current_token != CLOSECURLYBRACKET:
                parse_statement()
            if current_token == CLOSECURLYBRACKET:
                lex()  # Consume '}'
            else:
                raise SyntaxError("Expected '}' after while loop body")
        else:
            raise SyntaxError("Expected '{' after while loop condition")
    else:
        raise SyntaxError("Expected 'while'")

# Parsing function for if statements
def parse_if_statement():
    global current_token
    if current_token == IF:
        lex()  # Consume IF token
        parse_expression()  # Parse condition expression
        if current_token == OPENCURLYBRACKET:
            lex()  # Consume '{'
            # Parse if block
            while current_token != CLOSECURLYBRACKET:
                parse_statement()
            if current_token == CLOSECURLYBRACKET:
                lex()  # Consume '}'
            else:
                raise SyntaxError("Expected '}' after if block")
        else:
            raise SyntaxError("Expected '{' after if condition")
        # Check for optional elif and else blocks
        if current_token == ELIF:
            parse_elif_statement()
        elif current_token == ELSE:
            parse_else_statement()
    else:
        raise SyntaxError("Expected 'if'")

# Parsing function for elif statements
def parse_elif_statement():
    global current_token
    if current_token == ELIF:
        lex()  # Consume ELIF token
        parse_expression()  # Parse condition expression
        if current_token == OPENCURLYBRACKET:
            lex()  # Consume '{'
            # Parse elif block
            while current_token != CLOSECURLYBRACKET:
                parse_statement()
            if current_token == CLOSECURLYBRACKET:
                lex()  # Consume '}'
            else:
                raise SyntaxError("Expected '}' after elif block")
        else:
            raise SyntaxError("Expected '{' after elif condition")
    else:
        raise SyntaxError("Expected 'elif'")

# Parsing function for else statements
def parse_else_statement():
    global current_token
    if current_token == ELSE:
        lex()  # Consume ELSE token
        if current_token == OPENCURLYBRACKET:
            lex()  # Consume '{'
            # Parse else block
            while current_token != CLOSECURLYBRACKET:
                parse_statement()
            if current_token == CLOSECURLYBRACKET:
                lex()  # Consume '}'
            else:
                raise SyntaxError("Expected '}' after else block")
        else:
            raise SyntaxError("Expected '{' after else")
    else:
        raise SyntaxError("Expected 'else'")

# Parsing function for global statements
def parse_global_statement():
    global current_token
    if current_token == GLOBAL:
        lex()  # Consume GLOBAL token
        parse_variable_declaration()  # Parse variable declaration
    else:
        raise SyntaxError("Expected 'global'")

# Parsing function for input statements
def parse_input_statement():
    global current_token
    if current_token == INPUT:
        lex()  # Consume INPUT token
        if current_token == ALFA:
            lex()  # Consume variable name
        else:
            raise SyntaxError("Variable name expected after 'input'")
    else:
        raise SyntaxError("Expected 'input'")

# Parsing function for print statements
def parse_print_statement():
    global current_token
    if current_token == PRINT:
        lex()  # Consume PRINT token
        parse_expression()  # Parse expression
    else:
        raise SyntaxError("Expected 'print'")

# Parsing function for variable declarations
def parse_variable_declaration():
    global current_token
    if current_token == INTTYPETK:
        lex()  # Consume INTTYPETK token
        if current_token == ALFA:
            lex()  # Consume ALFA token
        else:
            raise SyntaxError("Variable name expected after 'int'")
    else:
        raise SyntaxError("Expected '#int' declaration")

# Call the parser
def parse():
    global current_token
    current_token = lex()  # Get the first token

    # Start parsing from the main program body
    while current_token is not None:
        parse_statement()  # Parse top-level statements

# Call the parser
parse()
