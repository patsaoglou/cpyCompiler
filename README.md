# CPY Compiler Project
In this repository, we share a compiler project I've made with my mate Ioannis Iatrakis under the Compilers 1 course (Prof. George Manis). This repository demonstrates the process of developing a fully working compiler from ground zero. The goal is to illustrate the end-to-end process of high level code compilation through stages into RISC-V assembly code, one step before machine code

A initial grammar file is what given to us and we had to implement the stages of the compiler, the lexer, the syntax analyzer, a semantic analyzer, an intermediary language that with the help of a symbol table structure is finaly converted to the respective assembly language, the RISC-V Instruction Set in our case. It is clear that with the existance of an intermediary language and the info of the symbol table, final code generation modules of different instruction sets like X86, MIPS etc can be mounted to out code to produce a wide range of executable code :-).

## Stages of our Compiler
1. **Lexer:** recognizes tokens (keywords, identifiers, operators, etc.) from the CPY source code.
2. **Syntax Analyzer:** checks if the token sequence follows the grammar rules of the language.
3. **Semantic Analyzer:** ensures logical correctness, such as type compatibility and valid function calls.
4. **Intermidiary Code Generation:** produces an abstract representation of the program for easier translation to assembly.
5. **Symbol Table Structure:** tracks variable declarations, memory offsets, and function context information.
6. **Final Code Generation (RISC-V):** converts the intermediary code into RISC-V assembly using symbol table data.


## CPY code logic
Below is a summary of the CPY language functionality:
1. **Variable Declaration:** CPY supports basic variable declarations (e.g., int variableName). Variables can store integers and hold values for use throughout the program.
2. **Global Variables:** The language allows the use of global variables, which can be accessed and modified across different functions using the global pointer register that has address of the global stack.
3. **Function Declaration:** 
    - Functions can be defined with parameters (e.g., max3(x, y, z)).
    - Recursive function calls are supported (e.g., fib(x) calls itself).
    - Functions can return values (e.g., return m in max3).
    - Functions can have nested helper functions (e.g., divides inside isPrime).
4. **Conditionals:** CPY supports conditional statements such as if, elif, and else for branching logic.
5. **Loops:** The language supports looping constructs, like while, to repeat code blocks until a condition is met.
6. **Input and Output:** The language supports reading input (int(input())) and printing output (print()), allowing interaction with the user.
7. **Modular Code:** Functions and variables can be organized in a modular fashion, making the code more readable and maintainable.
8. **Arithmetic and Logical Operations:** 
    - Basic arithmetic operations like addition, subtraction, multiplication, and division are supported.
    - Logical operations (e.g., ==, !=, >, <, and, or) are used for comparisons and conditional checks.


## Lexer Overview
The lexical analyzer is a critical component in the process of compiling or interpreting source code. Its main role is to break down the raw source code into a sequence of tokens. Tokens are the smallest units of meaningful code, such as keywords, identifiers, operators, literals, and punctuation. These tokens are then passed on to the syntax analyzer, which processes them according to the language's grammar rules.

Bellow we share a section of the lexer code that recognises known tokens and returns a token code to the syntax analizer routines which call **lex()** to get the next token:

```python
        if new_token=='main':
            return retARRAYTK(MAINTK,token)
        if new_token=='def':
            return retARRAYTK(DEFTK,token)
        if new_token=='#def':
            return retARRAYTK(DEF2TK,token)
        if new_token=='#int':
            return retARRAYTK(INTTYPETK,token)
```

## CPY Grammar Structure - Syntax Analyzer
CPY uses context-free grammar (CFG) to define its structure, which is a type of formal grammar commonly used for programming languages. In a CFG, rules describe how symbols can be replaced with others, allowing for the recursive and hierarchical organization of code. This allows CPY to define complex elements like functions, variables, and program flow in a clear and structured way. The grammar ensures that code can be parsed and understood systematically by a compiler or interpreter.

This top-to-bottom analysation of the CPY source code is how it is described in our code for the syntax analysis. In our code, lex() is called to get the tokens of the source one by one and check each time if the language syntax is followed. If there is a wrong token in the structure then a error is printed informing the programmer that a syntax error 
exists in the code. If a language grammar structure analyzed is completed successfully then the compiler can proceed to the next stages of producing the intermediary and the final code of the structure.

Here is a code section of the logic behind the syntax analysis:
```python

def parse_function_definition():
    global current_token, block_name_list, starting_quad, ending_quad, endblock
    if current_token[0] == DEFTK:
        current_token = lex()

        if current_token[0] == ANAGNORTK:
            ...

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
                            ...                                      
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

```

## Intermediary Code Generation
Intermediary code generation is important because it provides a flexible and simplified representation of the source code,
which can be more easily translated into machine code for different architectures. It allows for optimization and easier debugging before the final code generation.
By separating concerns, it ensures the compiler is more adaptable and efficient.

- Bellow we can check a simple conversion of a CPY code into the intermediary code:
```cpy
    def quad(x):
    #{
        #int y
        
        ## nested function sqr ##
        def sqr(x):
        #{
            ## body of sqr ##
            global counterFunctionCalls
            counterFunctionCalls = counterFunctionCalls + 1
            return x*x
        #}
        
        ## body of quad ##
        global counterFunctionCalls
        counterFunctionCalls = counterFunctionCalls + 1
        y = sqr(x)*sqr(x)
        return y
    #}
```


```int
    80 begin_block quad _ _  
    81 + counterFunctionCalls 1 T_16  
    82 = T_16 _ counterFunctionCalls  
    83 PAR x CV _  
    84 PAR T_17 RET _  
    85 call sqr _ _  
    86 PAR x CV _  
    87 PAR T_18 RET _  
    88 call sqr _ _  
    89 * T_17 T_18 T_19  
    90 = T_19 _ y  
    91 ret y _ _  
    92 end_block quad _ _  
```


We can see from the example above that the purpose of the intermediary code is descriptive of each line of the high level CPY code. The code is just enough to give information to the next compiling stage of what kind of architecture specific code has to be produced :-)! All these not without the symbol table...

## Symbol Table Structure
The symbol table is crucial for managing variable and function information during compilation. 
It tracks where variables are stored in memory, their types, and their scopes. Since CPU registers are limited, the symbol table is there for the compiler to  
allocate memory space on the stack for variables that cannot be loaded in the limited number of used CPU registers since the number of declarations in a source file can be practically infinite. 

It also enables the compiler to restore, modify, and save variables during execution. In intermediary code, each operation might translate to several assembly instructions, which the symbol table helps coordinate. The symbol table holds essential information about variables and functions, such as their offset (memory location), whether they are global or local, their arguments, and the frame length (memory required for local variables in function scopes). It helps manage how variables are stored, accessed, and modified during program execution, especially when variables can't fit into CPU registers and need to be stored in memory.

Symbol Table Information can be summarized below:

- **Offset:** specifies the memory location (e.g., 12 bytes).
- **Global/Local:** indicates if a variable is global or local.
- **Arguments:** lists the function parameters (e.g., x, y, z).
- **Frame Length:** memory used by local variables in a function (e.g., 32 bytes).

Here is an example of our stucture:


```sym
    Scope Name: PROGRAM, Level: 0
    Entities:
        Name: counterFunctionCalls, Offset: 12, Label: None, Arguments: [], Framelength: None, Type: NOT_GLOBAL
        Name: max3, Offset: None, Label: 1, Arguments: ['x', 'y', 'z'], Framelength: 32, Type: NOT_GLOBAL
        Name: fib, Offset: None, Label: 20, Arguments: ['x'], Framelength: 40, Type: NOT_GLOBAL
        Name: isPrime, Offset: None, Label: 55, Arguments: ['x'], Framelength: 32, Type: NOT_GLOBAL
        Name: quad, Offset: None, Label: 80, Arguments: ['x'], Framelength: None, Type: NOT_GLOBAL

    Scope Name: quad, Level: 1
    Entities:
        Name: x, Offset: 12, Label: None, Arguments: [], Framelength: None, Type: NOT_GLOBAL
        Name: y, Offset: 16, Label: None, Arguments: [], Framelength: None, Type: NOT_GLOBAL
        Name: sqr, Offset: None, Label: 74, Arguments: ['x'], Framelength: 24, Type: NOT_GLOBAL
        Name: counterFunctionCalls, Offset: None, Label: None, Arguments: [], Framelength: None, Type: GLOBAL
        Name: T_16, Offset: 20, Label: None, Arguments: [], Framelength: None, Type: NOT_GLOBAL
        Name: T_17, Offset: 24, Label: None, Arguments: [], Framelength: None, Type: NOT_GLOBAL
        Name: T_18, Offset: 28, Label: None, Arguments: [], Framelength: None, Type: NOT_GLOBAL
        Name: T_19, Offset: 32, Label: None, Arguments: [], Framelength: None, Type: NOT_GLOBAL
```


## Final RISC-V Assembly Goodness
The final code generation is a crucial step in the compilation process, where intermediary code is translated into machine code. During this stage, the symbol table plays an essential role in guiding how variables, functions, and operations are mapped to memory locations, registers, and machine instructions. The symbol table helps the compiler determine where to store and retrieve variables, track the scope of variables (whether global or local), and ensure that the correct offsets and labels are used.

The intermediary code provides the logical operations that need to be translated into assembly instructions. Each line of intermediary code is converted into one or more assembly instructions, with the symbol table supplying necessary information about where variables are located in memory (e.g., offsets), whether they are in registers, and the relationships between different variables and functions. As a result, the assembly code properly manipulates the values stored in memory and registers to execute the program.

A section of our compliler code which generates the final quads is shared bellow:
```python
if quad[1] == "JUMP":
        assembly_out("L"+str(quad[0])+":")

        assembly_out("      j L"+str(quad[4]))

    elif quad[1] == '=':
        if is_integer(quad[2]) or quad[2].isalpha() or 'T_' in quad[2]:
            assembly_out("L"+str(quad[0])+":")
            loadvr(quad[2],"t1")
            storerv("t1", quad[4])
    elif quad[1] in ["+","-","%","//","*"]:
        assembly_out("L"+str(quad[0])+":")
             
        loadvr(quad[2],"t1")
        loadvr(quad[3],"t2")
        
        if quad[1] == "+":
            assembly_out("      add t1, t1, t2") 
        elif quad[1] == "-":
            assembly_out("      sub t1, t1, t2")  
        elif quad[1] == "*":
            assembly_out("      mul t1, t1, t2") 
        elif quad[1] == "%":
            assembly_out("      rem t1, t1, t2")  
        elif quad[1] == "//":
            assembly_out("      div t1, t1, t2")  
        storerv("t1",quad[4])
```


Below we breakdown in detail the process of converting the intermidiary code along with the symbol code in the final RISC-V instructions using a few example lines:
Intermediary Code:
```int
    81 + counterFunctionCalls 1 T_16  
    82 = T_16 _ counterFunctionCalls  
```

Into assembly Code:
```s
    L81:
        lw t1,-12(gp)
        li t2,1
        add t1, t1, t2
        sw t1,-20(sp)
    L82:
        lw t1,-20(sp)
        sw t1,-12(gp)
```

Explanation:
**L81:**

- lw t1,-12(gp) - Load the value from the memory location at offset -12(gp) into register t1. This corresponds to counterFunctionCalls stored at offset -12.
- li t2,1 - Load the immediate value 1 into register t2.
- add t1, t1, t2 - Add the value in t1 (the value of counterFunctionCalls) to 1 (stored in t2), storing the result back in t1.
- sw t1,-20(sp) - Store the result from t1 into memory at the location -20(sp). This operation saves the updated counter.

**L82:**

- lw t1,-20(sp) - Load the updated counter value from memory at -20(sp) into t1.
- sw t1,-12(gp) - Store this updated value back into the global memory location -12(gp), updating the counterFunctionCalls.

# Disclaimers
This compiler has no point to be used anywhere. It was just made for educational purposes :-).
