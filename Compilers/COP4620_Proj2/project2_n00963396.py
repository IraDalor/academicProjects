import project1_n00963396
from sys import*


def get_file():
    filename = ""
    try:
        filename = argv[1]
        open(filename)
    except IOError:
        print("File not found")
        exit()
    except IndexError:
        print("Please enter a filename")
        exit()

    tokens = project1_n00963396.lexer(filename)
    tokens.append(('', '$'))
    return tokens


buff = get_file()
lh = 0
cntr = 0


def parser():
    global lh, buff
    if "Error" in buff:
        print ("REJECT")
        exit()
    else:
        program()
    if buff[lh][1] == "$":
        print ("ACCEPT")
    else:
        print ("REJECT")
        exit()


def match(t):
    global lh, buff
    if buff[lh][1] == t:
        lh += 1
    else:
        print ("REJECT")
        exit()


def program():
    declaration_list()


def declaration_list():
    declaration()
    declaration_listp()


def declaration_listp():
    global cntr, lh, buff
    if buff[lh][1] in ["int", "void"]:
        declaration()
        declaration_listp()
    else:
        return()


def declaration():
    global cntr, lh, buff
    if buff[lh][1] == "int":
        left = 'int'
        match("int")
        declarationp(left)
    elif buff[lh][1] == "void":
        left = 'void'
        match("void")
        declarationp(left)
    else:
        print ("REJECT")
        exit()


def declarationp(left):
    global cntr, lh, buff
    if buff[lh][1] == "ID":
        right = buff[lh][0]
        match("ID")
        declarationpp(left, right)
    else:
        print("REJECT")
        exit()


def declarationpp(left, right):
    global cntr, lh, buff
    if buff[lh][1] in [";", "["]:
        var_declarationp(right)
    elif buff[lh][1] == "(":
        match("(")
        params()
        if buff[lh][1] == ")":
            match(")")
            compound_stmt()
        else:
            print("REJECT")
            exit()
    else:
        print("REJECT")
        exit()


def var_declaration():
    global cntr, lh, buff
    type_specifier()
    if buff[lh][1] == "ID":
        right = buff[lh][0]
        match("ID")
        return var_declarationp(right)
    else:
        print ("REJECT")
        exit()


def var_declarationp(right):
    global cntr, lh, buff
    if buff[lh][1] == ";":
        match(";")
        return right, 0
    elif buff[lh][1] == "[":
        match("[")
        if buff[lh][1] == "NUM":
            num = buff[lh][0]
            match("NUM")
            if buff[lh][1] == "]":
                match("]")
                if buff[lh][1] == ";":
                    match(";")
                    return right, num
                else:
                    print ("REJECT")
                    exit()
            else:
                print("REJECT")
                exit()
        else:
            print("REJECT")
            exit()
    else:
        print("REJECT")
        exit()


def type_specifier():
    global cntr, lh, buff
    if buff[lh][1] == "int":
        match("int")
        return 'int'
    elif buff[lh][1] == "void":
        match("void")
        return 'void'
    else:
        print("REJECT")
        exit()


def params():
    global cntr, lh, buff
    if buff[lh][1] == "int":
        left = 'int'
        match("int")
        if buff[lh][1] == "ID":
            right = buff[lh][0]
            match("ID")
            param_listp()
        else:
            print("REJECT")
            exit()
    elif buff[lh][1] == "void":
        match("void")
        paramsp()
    else:
        print("REJECT")
        exit()


def paramsp():
    global cntr, lh, buff
    if buff[lh][1] == "ID":
        right = buff[lh][0]
        match("ID")
        paramp(right)
        param_listp()
    else:
        return()


def param_listp():
    global cntr, lh, buff
    if buff[lh][1] == ",":
        match(",")
        param()
        param_listp()
    else:
        return()


def param():
    global cntr, lh, buff
    if buff[lh][1] == "int":
        left = 'int'
        match("int")
        if buff[lh][1] == "ID":
            right = buff[lh][0]
            match("ID")
        else:
            print("REJECT")
            exit()
    elif buff[lh][1] == "void":
        left = 'void'
        match("void")
        if buff[lh][1] == "ID":
            right = buff[lh][0]
            match("ID")
        else:
            print("REJECT")
            exit()
    else:
        print("REJECT")
        exit()


def paramp(right):
    if buff[lh][1] == "[":
        match("[")
        if buff[lh][1] == "]":
            match("]")
            return right, 1
        else:
            print("REJECT")
            exit()
    else:
        return right, 0


def compound_stmt():
    global cntr, lh, buff
    if buff[lh][1] == "{":
        match("{")
        local_declarationsp()
        statement_listp()
        if buff[lh][1] == "}":
            match("}")
            return()
        else:
            print("REJECT")
            exit()
    else:
        print("REJECT")
        exit()


def local_declarationsp():
    global cntr, lh, buff
    if buff[lh][1] in ["int", "void"]:
        var_declaration()
        local_declarationsp()
    else:
        return()


def statement_listp():
    global cntr, lh, buff
    if buff[lh][1] in ["(", ";", "ID", "NUM", "if", "return", "while", "{"]:
        statement()
        statement_listp()
    else:
        return()


def statement():
    global cntr, lh, buff
    if buff[lh][1] in ["(", ";", "ID", "NUM"]:
        expression_stmt()
    elif buff[lh][1] == "{":
        match("{")
        local_declarationsp()
        statement_listp()
        if buff[lh][1] == "}":
            match("}")
            return()
        else:
            print("REJECT")
            exit()
    elif buff[lh][1] == "if":
        selection_stmt()
    elif buff[lh][1] == "while":
        iteration_stmt()
    elif buff[lh][1] == "return":
        return_stmt()
    else:
        print("REJECT")
        exit()


def expression_stmt():
    global cntr, lh, buff
    if buff[lh][1] in ["(", "ID", "NUM"]:
        expression()
        if buff[lh][1] == ";":
            match(";")
            return()
        else:
            print("REJECT")
            exit()
    elif buff[lh][1] == ";":
        match(";")
        return()
    else:
        print("REJECT")
        exit()


def selection_stmt():
    global cntr, lh, buff
    if buff[lh][1] == "if":
        match("if")
        if buff[lh][1] == "(":
            match("(")
            expression()
            if buff[lh][1] == ")":
                match(")")
                statement()
                selection_stmtp()
            else:
                print("REJECT")
                exit()
        else:
            print("REJECT")
    else:
        print("REJECT")
        exit()


def selection_stmtp():
    global cntr, lh, buff
    if buff[lh][1] == "else":
        match("else")
        statement()
    else:
        return()


def iteration_stmt():
    global cntr, lh, buff
    if buff[lh][1] == "while":
        match("while")
        if buff[lh][1] == "(":
            match("(")
            expression()
            if buff[lh][1] == ")":
                match(")")
                statement()
            else:
                print("REJECT")
                exit()
        else:
            print("REJECT")
            exit()
    else:
        print("REJECT")
        exit()


def return_stmt():
    global cntr, lh, buff
    if buff[lh][1] == "return":
        match("return")
        return_stmtp()
    else:
        print("REJECT")
        exit()


def return_stmtp():
    global cntr, lh, buff
    if buff[lh][1] == ";":
        match(";")
        return()
    elif buff[lh][1] == "ID":
        left = buff[lh][0]
        match("ID")
        return_stmtpp(left)
    elif buff[lh][1] == "(":
        match("(")
        expression()
        if buff[lh][1] == ")":
            match(")")
            termp()
            additive_expressionp()
            simple_expressionp()
            if buff[lh][1] == ";":
                match(";")
                return()
            else:
                print("REJECT")
                exit()
        else:
            print("REJECT")
            exit()
    elif buff[lh][1] == "NUM":
        match("NUM")
        termp()
        additive_expressionp()
        simple_expressionp()
        if buff[lh][1] == ";":
            match(";")
            return()
        else:
            print("REJECT")
            exit()
    else:
        print("REJECT")
        exit()


def return_stmtpp(left):
    global cntr, lh, buff
    if buff[lh][1] == ";":
        match(";")
        return()
    elif buff[lh][1] in ["!=", "*", "+", "-", "/", "<", "<=", "=", "==", ">", ">=", "["]:
        varp()
        return_stmtppp()
    elif buff[lh][1] == "(":
        match("(")
        args()
        if buff[lh][1] == ")":
            match(")")
            termp()
            additive_expressionp()
            simple_expressionp()
            if buff[lh][1] == ";":
                match(";")
                return()
            else:
                print("REJECT")
                exit()
        else:
            print("REJECT")
            exit()
    else:
        print("REJECT")
        exit()


def return_stmtppp():
    global cntr, lh, buff
    if buff[lh][1] == ";":
        match(";")
        return()
    elif buff[lh][1] == "=":
        match("=")
        expression()
        if buff[lh][1] == ";":
            match(";")
            return()
        else:
            print("REJECT")
            exit()
    elif buff[lh][1] in ["!=", "*", "+", "-", "/", "<", "<=", "=", "==", ">", ">="]:
        termp()
        additive_expressionp()
        simple_expressionp()
        if buff[lh][1] == ";":
            match(";")
            return()
        else:
            print("REJECT")
            exit()
    else:
        print("REJECT")
        exit()


def expression():
    global cntr, lh, buff
    if buff[lh][1] == "ID":
        left = buff[lh][0]
        match("ID")
        expressionp(left)
    elif buff[lh][1] == "(":
        match("(")
        expression()
        if buff[lh][1] == ")":
            match(")")
            termp()
            additive_expressionp()
            simple_expressionp()
        else:
            print("REJECT")
            exit()
    elif buff[lh][1] == "NUM":
        left = buff[lh][0]
        match("NUM")
        termp()
        additive_expressionp()
        simple_expressionp()
    else:
        print("REJECT")
        exit()


def expressionp(left):
    global cntr, lh, buff
    if buff[lh][1] in ["!=", "*", "+", "-", "/", "<", "<=", "=", "==", ">", ">=", "["]:
        varp()
        expressionpp()
    elif buff[lh][1] == "(":
        match("(")
        args()
        if buff[lh][1] == ")":
            match(")")
            termp()
            additive_expressionp()
            simple_expressionp()
        else:
            print("REJECT")
            exit()
    else:
        return()


def expressionpp():
    global cntr, lh, buff
    if buff[lh][1] == "=":
        match("=")
        expression()
    elif buff[lh][1] in ["!=", "*", "+", "-", "/", "<", "<=", "==", ">", ">="]:
        termp()
        additive_expressionp()
        simple_expressionp()
    else:
        return()


def var():
    global cntr, lh, buff
    if buff[lh][1] == "ID":
        left = buff[lh][0]
        match("ID")
        varp()
        return left
    else:
        print("REJECT")
        exit()


def varp():
    global cntr, lh, buff
    if buff[lh][1] == "[":
        match("[")
        expression()
        if buff[lh][1] == "]":
            match("]")
        else:
            print("REJECT")
            exit()
    else:
        return()


def simple_expression():
    global cntr, lh, buff
    if buff[lh][1] == "(":
        match("(")
        expression()
        if buff[lh][1] == ")":
            match(")")
            termp()
            additive_expressionp()
            simple_expressionp()
        else:
            print("REJECT")
            exit()
    elif buff[lh][1] == "ID":
        left = buff[lh][0]
        match("ID")
        factorp(left)
        termp()
        additive_expressionp()
        simple_expressionp()
    elif buff[lh][1] == "NUM":
        match("NUM")
        termp()
        additive_expressionp()
        simple_expressionp()
    else:
        print("REJECT")
        exit()


def simple_expressionp():
    global cntr, lh, buff
    if buff[lh][1] == "<=":
        match("<=")
        additive_expression()
    elif buff[lh][1] == "<":
        match("<")
        additive_expression()
    elif buff[lh][1] == ">":
        match(">")
        additive_expression()
    elif buff[lh][1] == ">=":
        match(">=")
        additive_expression()
    elif buff[lh][1] == "==":
        match("==")
        additive_expression()
    elif buff[lh][1] == "!=":
        match("!=")
        additive_expression()
    else:
        return()


def relop():
    global cntr, lh, buff
    if buff[lh][1] == "<=":
        match("<=")
        return 'compr'
    elif buff[lh][1] == "<":
        match("<")
        return 'compr'
    elif buff[lh][1] == ">":
        match(">")
        return 'compr'
    elif buff[lh][1] == ">=":
        match(">=")
        return 'compr'
    elif buff[lh][1] == "==":
        match("==")
        return 'compr'
    elif buff[lh][1] == "!=":
        match("!=")
        return 'compr'
    else:
        print("REJECT")
        exit()


def additive_expression():
    global cntr, lh, buff
    if buff[lh][1] in ["(", "ID", "NUM"]:
        term()
        additive_expressionp()
    else:
        print("REJECT")
        exit()


def additive_expressionp():
    global cntr, lh, buff
    if buff[lh][1] in ["+", "-"]:
        center = addop()
        term()
        additive_expressionp()
    else:
        return()


def addop():
    global cntr, lh, buff
    if buff[lh][1] == "+":
        match("+")
        return 'add'
    elif buff[lh][1] == "-":
        match("-")
        return 'sub'
    else:
        print("REJECT")
        exit()


def term():
    global cntr, lh, buff
    if buff[lh][1] in ["(", "ID", "NUM"]:
        left = factor()
        termp()
    else:
        print("REJECT")
        exit()


def termp():
    global cntr, lh, buff
    if buff[lh][1] in ["*", "/"]:
        center = mulop()
        right = factor()
        termp()
    else:
        return()


def mulop():
    global cntr, lh, buff
    if buff[lh][1] == "*":
        match("*")
        return 'mult'
    elif buff[lh][1] == "/":
        match("/")
        return 'div'
    else:
        print("REJECT")
        exit()


def factor():
    global cntr, lh, buff
    if buff[lh][1] == "(":
        match("(")
        expression()
        if buff[lh][1] == ")":
            match(")")
            return()
        else:
            print("REJECT")
            exit()
    elif buff[lh][1] == "ID":
        right = buff[lh][0]
        match("ID")
        factorp(right)
    elif buff[lh][1] == "NUM":
        right = buff[lh][0]
        match("NUM")
        return right
    else:
        print("REJECT")
        exit()


def factorp(right):
    global cntr, lh, buff
    if buff[lh][1] == "[":
        varp()
    elif buff[lh][1] == "(":
        match("(")
        args()
        if buff[lh][1] == ")":
            match(")")
            return()
        else:
            print("REJECT")
            exit()
    else:
        return()


def call():
    global cntr, lh, buff
    if buff[lh][1] == "ID":
        match("ID")
        if buff[lh][1] == "(":
            match("(")
            args()
            if buff[lh][1] == ")":
                match(")")
                return()
            else:
                print("REJECT")
                exit()
        else:
            print("REJECT")
            exit()
    else:
        print("REJECT")
        exit()


def args():
    global cntr, lh, buff
    if buff[lh][1] in ["ID", "(", "NUM"]:
        arg_list()
    else:
        return()


def arg_list():
    global cntr, lh, buff
    if buff[lh][1] == "ID":
        left = buff[lh][0]
        match("ID")
        arg_listpp(left)
    elif buff[lh][1] == "(":
        match("(")
        expression()
        if buff[lh][1] == ")":
            match(")")
            termp()
            additive_expressionp()
            simple_expressionp()
            arg_listp()
        else:
            print("REJECT")
            exit()
    elif buff[lh][1] == "NUM":
        match("NUM")
        termp()
        additive_expressionp()
        simple_expressionp()
        arg_listp()
    else:
        print("REJECT")
        exit()


def arg_listp():
    global cntr, lh, buff
    if buff[lh][1] == ",":
        match(",")
        expression()
        arg_listp()
    else:
        return()


def arg_listpp(left):
    global cntr, lh, buff
    if buff[lh][1] in ["!=", "*", "+", "-", "/", "<", "<=", "=", "==", ">", ">=", "[", ","]:
        varp()
        arg_listppp()
    elif buff[lh][1] == "(":
        match("(")
        args()
        if buff[lh][1] == ")":
            match(")")
            termp()
            additive_expressionp()
            simple_expressionp()
            arg_listp()
    else:
        return()


def arg_listppp():
    global cntr, lh, buff
    if buff[lh][1] == "=":
        match("=")
        expression()
        arg_listp()
    elif buff[lh][1] in ["!=", "*", "+", "-", "/", "<", "<=", "=", "==", ">", ">=", ","]:
        termp()
        additive_expressionp()
        simple_expressionp()
        arg_listp()
    else:
        return()


parser()
