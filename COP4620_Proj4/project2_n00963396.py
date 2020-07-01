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
funlst = []
varlst = [[]]
cntrlst = []
scope = 0
cntr = 0
arglst = []
argflag = False
argFunId = 0
rtrnflg = True


def parser():
    global lh, buff, funlst
    if "Error" in buff:
        print ("REJECT")
        exit()
    if any('main' in i for i in buff):
        program()
    else:
        print("REJECT")
        exit()
    if buff[lh][1] == "$":
        if any('main' in i for i in funlst):
            print ("ACCEPT")
        else:
            print("REJECT")
            exit()
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


def checkscope(id):
    global scope, varlst, funlst, lh, buff
    if any(id in i for i in varlst[scope]):
        if any(id in i for i in varlst[0]):
            chk = [x[0] for x in varlst[scope]].index(id)
            del(varlst[scope][chk])
            return True
        elif any(id in i for i in varlst[scope-1]):
            chk = [x[0] for x in varlst[scope]].index(id)
            del(varlst[scope][chk])
            return True
        else:
            print("REJECT")
            exit()
    else:
        return True


def program():
    declaration_list()


def declaration_list():
    declaration()
    declaration_listp()


def declaration_listp():
    global scope, varlst, funlst, lh, buff
    if buff[lh][1] in ["int", "void"]:
        declaration()
        declaration_listp()
    else:
        return()


def declaration():
    global scope, varlst, funlst, lh, buff
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
    global scope, varlst, funlst, lh, buff
    if buff[lh][1] == "ID":
        right = buff[lh][0]
        match("ID")
        declarationpp(left, right)
    else:
        print("REJECT")
        exit()


def declarationpp(left, right):
    global scope, varlst, funlst, lh, buff, rtrnflg
    if buff[lh][1] in [";", "["]:
        res = var_declarationp(right)
        if left == 'void':
            print("REJECT")
            exit()
        elif any(right in i for i in varlst[0]):
            print("REJECT")
            exit()
        elif any(right in i for i in funlst):
            print("REJECT")
            exit()
        else:
            varlst[0].append(res)
    elif buff[lh][1] == "(":
        match("(")
        if any(right in i for i in funlst):
            print("REJECT")
            exit()
        elif any('main' in i for i in funlst):
            print("REJECT")
            exit()
        elif right == 'main' and left != 'void':
            print("REJECT")
            exit()
        else:
            scope = len(varlst)
            funlst.append((left, right, scope))
            varlst.append([])
            for item in varlst[0]:
                varlst[scope].append(item)
        params(right)
        if buff[lh][1] == ")":
            match(")")
            if left == "int":
                rtrnflg = False
            compound_stmt(len(funlst)-1)
        else:
            print("REJECT")
            exit()
    else:
        print("REJECT")
        exit()


def var_declaration():
    global scope, varlst, funlst, lh, buff
    left = type_specifier()
    if left == 'void':
        print("REJECT")
        exit()
    if buff[lh][1] == "ID":
        right = buff[lh][0]
        match("ID")
        checkscope(right)
        return var_declarationp(right)
    else:
        print ("REJECT")
        exit()


def var_declarationp(right):
    global scope, varlst, funlst, lh, buff
    if buff[lh][1] == ";":
        match(";")
        return right, 0
    elif buff[lh][1] == "[":
        match("[")
        if buff[lh][1] == "NUM":
            match("NUM")
            if buff[lh][1] == "]":
                match("]")
                if buff[lh][1] == ";":
                    match(";")
                    return right, 1
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
    global scope, varlst, funlst, lh, buff
    if buff[lh][1] == "int":
        match("int")
        return 'int'
    elif buff[lh][1] == "void":
        match("void")
        return 'void'
    else:
        print("REJECT")
        exit()


def params(funid):
    global scope, varlst, funlst, lh, buff
    if buff[lh][1] == "int":
        match("int")
        if buff[lh][1] == "ID":
            right = buff[lh][0]
            match("ID")
            if funid == 'main':
                print("REJECT")
                exit()
            if checkscope(right):
                temp = paramp(right)
                varlst[scope].append(temp)
                chk = [x[1] for x in funlst].index(funid)
                funlst[chk] = funlst[chk] + (temp[1],)
            param_listp(funid)
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
    global scope, varlst, funlst, lh, buff
    if buff[lh][1] == "ID":
        match("ID")
        print("REJECT")
        exit()
        #paramp(left, right)
        #param_listp()
    else:
        return()


def param_listp(funid):
    global scope, varlst, funlst, lh, buff
    if buff[lh][1] == ",":
        match(",")
        param(funid)
        param_listp(funid)
    else:
        return()


def param(funid):
    global scope, varlst, funlst, lh, buff
    if buff[lh][1] == "int":
        match("int")
        if buff[lh][1] == "ID":
            right = buff[lh][0]
            match("ID")
            if funid == 'main':
                print("REJECT")
                exit()
            if checkscope(right):
                temp = paramp(right)
                varlst[scope].append(temp)
                chk = [x[1] for x in funlst].index(funid)
                funlst[chk] = funlst[chk] + (temp[1],)
        else:
            print("REJECT")
            exit()
    elif buff[lh][1] == "void":
        match("void")
        if buff[lh][1] == "ID":
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


def compound_stmt(funid):
    global scope, varlst, funlst, lh, buff, rtrnflg
    if buff[lh][1] == "{":
        match("{")
        local_declarationsp()
        statement_listp(funid)
        if buff[lh][1] == "}":
            match("}")
            scope = 0
            if not rtrnflg:
                print("REJECT")
                exit()
            return()
        else:
            print("REJECT")
            exit()
    else:
        print("REJECT")
        exit()


def local_declarationsp():
    global scope, varlst, funlst, lh, buff
    if buff[lh][1] in ["int", "void"]:
        varlst[scope].append(var_declaration())
        local_declarationsp()
    else:
        return()


def statement_listp(funid):
    global scope, varlst, funlst, lh, buff
    if buff[lh][1] in ["(", ";", "ID", "NUM", "if", "return", "while", "{"]:
        statement(funid)
        statement_listp(funid)
    else:
        return()


def statement(funid):
    global scope, varlst, funlst, lh, buff, rtrnflg
    if buff[lh][1] in ["(", ";", "ID", "NUM"]:
        expression_stmt()
    elif buff[lh][1] == "{":
        temp = scope
        match("{")
        scope = len(varlst)
        varlst.append([])
        for item in varlst[temp]:
            varlst[scope].append(item)
        local_declarationsp()
        statement_listp(funid)
        if buff[lh][1] == "}":
            match("}")
            scope = temp
            return()
        else:
            print("REJECT")
            exit()
    elif buff[lh][1] == "if":
        selection_stmt()
    elif buff[lh][1] == "while":
        iteration_stmt()
    elif buff[lh][1] == "return":
        rtrnflg = True
        return_stmt(funid)
    else:
        print("REJECT")
        exit()


def expression_stmt():
    global scope, varlst, funlst, lh, buff
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
    global scope, varlst, funlst, lh, buff
    if buff[lh][1] == "if":
        match("if")
        if buff[lh][1] == "(":
            match("(")
            expression()
            if buff[lh][1] == ")":
                match(")")
                statement(None)
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
    global scope, varlst, funlst, lh, buff
    if buff[lh][1] == "else":
        match("else")
        statement(None)
    else:
        return()


def iteration_stmt():
    global scope, varlst, funlst, lh, buff
    if buff[lh][1] == "while":
        match("while")
        if buff[lh][1] == "(":
            match("(")
            expression()
            if buff[lh][1] == ")":
                match(")")
                statement(None)
            else:
                print("REJECT")
                exit()
        else:
            print("REJECT")
            exit()
    else:
        print("REJECT")
        exit()


def return_stmt(funid):
    global scope, varlst, funlst, lh, buff
    if buff[lh][1] == "return":
        match("return")
        return_stmtp(funid)
    else:
        print("REJECT")
        exit()


def return_stmtp(funid):
    global scope, varlst, funlst, lh, buff
    if funid is not None:
        if funlst[funid][0] == 'void':
            if buff[lh][1] != ";":
                print("REJECT")
                exit()
        if funlst[funid][0] == 'int':
            if buff[lh][1] == ";":
                print("REJECT")
                exit()
    if buff[lh][1] == ";":
        match(";")
        return()
    elif buff[lh][1] == "ID":
        left = buff[lh][0]
        match("ID")
        if any(left in i for i in funlst):
            chk = [x[1] for x in funlst].index(left)
            if funlst[chk][0] == 'void':
                print("REJECT")
                exit()
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
    global scope, varlst, funlst, lh, buff, argflag, arglst
    if any(left in i for i in varlst[scope]):
        chk = [x[0] for x in varlst[scope]].index(left)
        if varlst[scope][chk][1] == 1:
            if buff[lh][1] != "[":
                print("REJECT")
                exit()
    if buff[lh][1] == ";":
        match(";")
        if any(left in i for i in varlst[scope]):
            return()
        else:
            print("REJECT")
            exit()
    elif buff[lh][1] in ["!=", "*", "+", "-", "/", "<", "<=", "=", "==", ">", ">=", "["]:
        varp(left)
        return_stmtppp()
    elif buff[lh][1] == "(":
        match("(")
        argflag = True
        args()
        argFunId = [x[1] for x in funlst].index(left)
        if len(arglst) == len(funlst[argFunId]) - 3:
            for x in range(3, len(funlst[argFunId])):
                if arglst[x - 3] == funlst[argFunId][x]:
                    continue
                else:
                    print("REJECT")
                    exit()
        else:
            print("REJECT")
            exit()
        if buff[lh][1] == ")":
            match(")")
            argflag = False
            arglst *= 0
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
    global scope, varlst, funlst, lh, buff, argflag
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
        argflag = False
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
    global scope, varlst, funlst, lh, buff, argflag, arglst
    if buff[lh][1] == "ID":
        left = buff[lh][0]
        match("ID")
        if any(left in i for i in varlst[scope]):
            expressionp(left)
        elif any(left in i for i in funlst):
            if buff[lh-2][1] not in (';', '{', '}') or buff[lh+2][1] in ["!=", "*", "+", "-", "/", "<", "<=", "=", "==", ">", ">="]:
                chk = [x[1] for x in funlst].index(left)
                if funlst[chk][0] == 'void':
                    print("REJECT")
                    exit()
            if argflag:
                arglst.append(0)
            if buff[lh][1] != "(":
                print("REJECT")
                exit()
            expressionp(left)
        else:
            print("REJECT")
            exit()
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
        match("NUM")
        if argflag:
            arglst.append(0)
        termp()
        additive_expressionp()
        simple_expressionp()
    else:
        print("REJECT")
        exit()


def expressionp(left):
    global scope, varlst, funlst, lh, buff, argflag, arglst
    if any(left in i for i in varlst[scope]):
        chk = [x[0] for x in varlst[scope]].index(left)
        if varlst[scope][chk][1] == 1 and buff[lh][1] not in [';', '{', '}']:
            if argflag:
                arglst.append(1)
            else:
                if buff[lh][1] != "[":
                    print("REJECT")
                    exit()
        elif argflag:
            arglst.append(0)
    if buff[lh][1] in ["!=", "*", "+", "-", "/", "<", "<=", "=", "==", ">", ">=", "["]:
        argflag = False
        varp(left)
        expressionpp(left)
    elif buff[lh][1] == "(":
        match("(")
        if any(left in i for i in funlst):
            argflag = True
            args()
            argFunId = [x[1] for x in funlst].index(left)
            if len(arglst) == len(funlst[argFunId]) - 3:
                for x in range(3, len(funlst[argFunId])):
                    if arglst[x - 3] == funlst[argFunId][x]:
                        continue
                    else:
                        print("REJECT")
                        exit()
            else:
                print("REJECT")
                exit()
        else:
            print("REJECT")
            exit()
        if buff[lh][1] == ")":
            match(")")
            argflag = False
            arglst *= 0
            termp()
            additive_expressionp()
            simple_expressionp()
        else:
            print("REJECT")
            exit()
    else:
        return()


def expressionpp(left):
    global scope, varlst, funlst, lh, buff, argflag
    if buff[lh][1] == "=":
        match("=")
        id = buff[lh][0]
        if buff[lh][1] == "ID":
            if any(id in i for i in varlst[scope]):
                chk = [x[0] for x in varlst[scope]].index(id)
                chk1 = [x[0] for x in varlst[scope]].index(left)
                if varlst[scope][chk][1] != varlst[scope][chk1][1]:
                    if varlst[scope][chk][1] == 1 and buff[lh+1][1] != "[":
                        print("REJECT")
                        exit()
                elif buff[lh-2][1] == "]":
                    if varlst[scope][chk][1] == 1 and buff[lh+1][1] != "[":
                        print("REJECT")
                        exit()
            elif any(id in i for i in funlst):
                chk = [x[1] for x in funlst].index(id)
                if funlst[chk][0] == 'void':
                    print("REJECT")
                    exit()
        expression()
    elif buff[lh][1] in ["!=", "*", "+", "-", "/", "<", "<=", "==", ">", ">="]:
        argflag = False
        termp()
        additive_expressionp()
        simple_expressionp()
    else:
        return()


def var():
    global scope, varlst, funlst, lh, buff
    if buff[lh][1] == "ID":
        left = buff[lh][0]
        match("ID")
        varp(left)
        return left
    else:
        print("REJECT")
        exit()


def varp(left):
    global scope, varlst, funlst, lh, buff, arglst, argflag
    tempflag = False
    if any(left in i for i in varlst[scope]):
        chk = [x[0] for x in varlst[scope]].index(left)
        if varlst[scope][chk][1] == 1:
            if buff[lh][1] == "[":
                match("[")
                if argflag:
                    argflag = False
                    tempflag = True
                expression()
                if tempflag:
                    argflag = True
                if buff[lh][1] == "]":
                    match("]")
                    if argflag:
                        arglst.append(0)
                else:
                    print("REJECT")
                    exit()
            else:
                print("REJECT")
                exit()
        else:
            return()
    else:
        print("REJECT")
        exit()


def simple_expression():
    global scope, varlst, funlst, lh, buff
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
    global scope, varlst, funlst, lh, buff
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
    global scope, varlst, funlst, lh, buff
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
    global scope, varlst, funlst, lh, buff
    if buff[lh][1] in ["(", "ID", "NUM"]:
        term()
        additive_expressionp()
    else:
        print("REJECT")
        exit()


def additive_expressionp():
    global scope, varlst, funlst, lh, buff
    if buff[lh][1] in ["+", "-"]:
        center = addop()
        term()
        additive_expressionp()
    else:
        return()


def addop():
    global scope, varlst, funlst, lh, buff
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
    global scope, varlst, funlst, lh, buff
    if buff[lh][1] in ["(", "ID", "NUM"]:
        left = factor()
        termp()
    else:
        print("REJECT")
        exit()


def termp():
    global scope, varlst, funlst, lh, buff
    if buff[lh][1] in ["*", "/"]:
        center = mulop()
        right = factor()
        termp()
    else:
        return()


def mulop():
    global scope, varlst, funlst, lh, buff
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
    global scope, varlst, funlst, lh, buff
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
        if any(right in i for i in funlst) and buff[lh][1] == "(":
            chk = [x[1] for x in funlst].index(right)
            if funlst[chk][0] == 'void':
                print("REJECT")
                exit()
        factorp(right)
    elif buff[lh][1] == "NUM":
        right = buff[lh][0]
        match("NUM")
        return right
    else:
        print("REJECT")
        exit()


def factorp(right):
    global scope, varlst, funlst, lh, buff, argflag, arglst
    if buff[lh][1] == "[":
        varp(right)
    elif buff[lh][1] == "(":
        match("(")
        argflag = True
        args()
        argFunId = [x[1] for x in funlst].index(right)
        if len(arglst) == len(funlst[argFunId]) - 3:
            for x in range(3, len(funlst[argFunId])):
                if arglst[x - 3] == funlst[argFunId][x]:
                    continue
                else:
                    print("REJECT")
                    exit()
        else:
            print("REJECT")
            exit()
        if buff[lh][1] == ")":
            match(")")
            argflag = False
            arglst *= 0
            return()
        else:
            print("REJECT")
            exit()
    else:
        return()


def call():
    global scope, varlst, funlst, lh, buff, arglst, argflag
    if buff[lh][1] == "ID":
        left = buff[lh][0]
        match("ID")
        if any(left in i for i in funlst):
            if buff[lh][1] == "(":
                match("(")
                argflag = True
                args()
                argFunId = [x[1] for x in funlst].index(left)
                if len(arglst) == len(funlst[argFunId]) - 3:
                    for x in range(3, len(funlst[argFunId])):
                        if arglst[x - 3] == funlst[argFunId][x]:
                            continue
                        else:
                            print("REJECT")
                            exit()
                else:
                    print("REJECT")
                    exit()
                if buff[lh][1] == ")":
                    match(")")
                    argflag = False
                    arglst *= 0
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
    else:
        print("REJECT")
        exit()


def args():
    global scope, varlst, funlst, lh, buff, arglst
    if buff[lh][1] in ["ID", "(", "NUM"]:
        arg_list()
    else:
        return()


def arg_list():
    global scope, varlst, funlst, lh, buff, arglst
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
        arglst.append(0)
        termp()
        additive_expressionp()
        simple_expressionp()
        arg_listp()
    else:
        print("REJECT")
        exit()


def arg_listp():
    global scope, varlst, funlst, lh, buff, arglst, argflag
    if buff[lh][1] == ",":
        match(",")
        argflag = True
        expression()
        arg_listp()
    else:
        return()


def arg_listpp(left):
    global scope, varlst, funlst, lh, buff, arglst, argflag
    if any(left in i for i in varlst[scope]) and buff[lh][1] == ")":
        chk = [x[0] for x in varlst[scope]].index(left)
        if varlst[scope][chk][1] == 0:
            arglst.append(0)
    if buff[lh][1] in ["!=", "*", "+", "-", "/", "<", "<=", "=", "==", ">", ">=", "[", ","]:
        varp(left)
        if any(left in i for i in varlst[scope]):
            chk = [x[0] for x in varlst[scope]].index(left)
            if varlst[scope][chk][1] == 0:
                arglst.append(0)
            elif varlst[scope][chk][1] == 1 and buff[lh-1][1] != ']':
                arglst.append(1)
        arg_listppp()
    elif buff[lh][1] == "(":
        match("(")
        args()
        if buff[lh][1] == ")":
            match(")")
            arglst.append(1)
            termp()
            additive_expressionp()
            simple_expressionp()
            arg_listp()
    else:
        return()


def arg_listppp():
    global scope, varlst, funlst, lh, buff, arglst, argflag
    if buff[lh][1] == "=":
        match("=")
        argflag = False
        expression()
        arg_listp()
    elif buff[lh][1] in ["!=", "*", "+", "-", "/", "<", "<=", "=", "==", ">", ">=", ","]:
        argflag = False
        termp()
        additive_expressionp()
        simple_expressionp()
        arg_listp()
    else:
        return()


parser()
#print varlst
#print funlst
#print arglst
