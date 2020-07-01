import project1_n00963396
from sys import *


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
fncnt = 0
outlst = []
varcnt = -1


def parser():
    global lh, buff, outlst
    if "Error" in buff:
        print("REJECT")
        exit()
    else:
        program()
    if buff[lh][1] == "$":
        printtable()
        #print("ACCEPT")
    else:
        print("REJECT")
        exit()


def printtable():
    global outlst
    width_col1 = 3
    width_col2 = max([len(str(x)) for x in outlst[1]])
    width_col3 = max([len(str(x)) for x in outlst[2]])
    width_col4 = max([len(str(x)) for x in outlst[3]])
    width_col5 = max([len(str(x)) for x in outlst[4]])
    width_col6 = max([len(str(x)) for x in outlst[5]])

    for i in outlst:
        print("{0:<{col1}}  {1:<{col2}}   {2:<{col3}}   {3:<{col4}}   {4:<{col5}}   {5:<{col6}}".format(i[0],
                                                                                                       i[1], i[2],
                                                                                                       i[3], i[4], i[5],
                                                                                                       col1=width_col1,
                                                                                                       col2=width_col2,
                                                                                                       col3=width_col3,
                                                                                                       col4=width_col4,
                                                                                                       col5=width_col5,
                                                                                                       col6=width_col6))


def match(t):
    global lh, buff
    if buff[lh][1] == t:
        lh += 1
    else:
        print("REJECT")
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
        return


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
        print("REJECT")
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
    global cntr, lh, buff, fncnt, outlst
    if buff[lh][1] in [";", "["]:
        var_declarationp(right)
    elif buff[lh][1] == "(":
        match("(")
        if right == "main":
            outlst.append((len(outlst)+1, "func", right, left, 0, ""))
        else:
            fncnt += 1
            outlst.append((len(outlst)+1, "func", right, left, fncnt, ""))
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
        var_declarationp(right)
        return
    else:
        print("REJECT")
        exit()


def var_declarationp(right):
    global cntr, lh, buff, outlst
    if buff[lh][1] == ";":
        match(";")
        outlst.append((len(outlst)+1, "alloc", 4, "", right, ""))
        return
    elif buff[lh][1] == "[":
        match("[")
        if buff[lh][1] == "NUM":
            num = buff[lh][0] * 4
            match("NUM")
            if buff[lh][1] == "]":
                match("]")
                if buff[lh][1] == ";":
                    match(";")
                    outlst.append((len(outlst)+1, "alloc", num, "", right, ""))
                    return
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
    global cntr, lh, buff, outlst
    if buff[lh][1] == "int":
        left = 'int'
        match("int")
        if buff[lh][1] == "ID":
            right = buff[lh][0]
            match("ID")
            outlst.append((len(outlst)+1, "param", "", "", right, ""))
            outlst.append((len(outlst)+1, "alloc", 4, "", right, ""))
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
        return


def param_listp():
    global cntr, lh, buff
    if buff[lh][1] == ",":
        match(",")
        param()
        param_listp()
    else:
        return


def param():
    global cntr, lh, buff, outlst
    if buff[lh][1] == "int":
        left = 'int'
        match("int")
        if buff[lh][1] == "ID":
            right = buff[lh][0]
            match("ID")
            outlst.append((len(outlst)+1, "param", "", "", right, ""))
            outlst.append((len(outlst)+1, "alloc", 4, "", right, ""))
            paramp(right)
        else:
            print("REJECT")
            exit()
    elif buff[lh][1] == "void":
        left = 'void'
        match("void")
        if buff[lh][1] == "ID":
            right = buff[lh][0]
            match("ID")
            paramp(right)
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


def list_rindex(li, x="func"):
    for i in reversed(range(len(li))):
        if li[i][1] == x:
            return i
    raise ValueError("REJECT")


def compound_stmt():
    global cntr, lh, buff, outlst
    if buff[lh][1] == "{":
        match("{")
        local_declarationsp()
        statement_listp()
        if buff[lh][1] == "}":
            match("}")
            ind = list_rindex(outlst)
            outlst.append((len(outlst)+1, "end", "func", outlst[ind][2], "", ""))
            return
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
        return


def statement_listp():
    global cntr, lh, buff
    if buff[lh][1] in ["(", ";", "ID", "NUM", "if", "return", "while", "{"]:
        statement()
        statement_listp()
    else:
        return


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
            return
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
            return
        else:
            print("REJECT")
            exit()
    elif buff[lh][1] == ";":
        match(";")
        return
    else:
        print("REJECT")
        exit()


def selection_stmt():
    global cntr, lh, buff, outlst
    if buff[lh][1] == "if":
        match("if")
        if buff[lh][1] == "(":
            match("(")
            result = expression()
            if buff[lh][1] == ")":
                match(")")
                if outlst[len(outlst)-1][1] == "BRGEQ":
                    outlst[len(outlst)-1] = ((outlst[len(outlst)-1][0], "compr", outlst[len(outlst)-1][2],
                                              outlst[len(outlst)-1][3], outlst[len(outlst)-1][4],
                                              outlst[len(outlst)-1][5]))
                    outlst.append((len(outlst)+1, "BRGEQ", outlst[len(outlst)-1][4], "", "", ""))
                elif outlst[len(outlst)-1][1] == "BRGT":
                    outlst[len(outlst)-1] = ((outlst[len(outlst)-1][0], "compr", outlst[len(outlst)-1][2],
                                              outlst[len(outlst)-1][3], outlst[len(outlst)-1][4],
                                              outlst[len(outlst)-1][5]))
                    outlst.append((len(outlst)+1, "BRGT", outlst[len(outlst)-1][4], "", "", ""))
                elif outlst[len(outlst)-1][1] == "BRLEQ":
                    outlst[len(outlst)-1] = ((outlst[len(outlst)-1][0], "compr", outlst[len(outlst)-1][2],
                                              outlst[len(outlst)-1][3], outlst[len(outlst)-1][4],
                                              outlst[len(outlst)-1][5]))
                    outlst.append((len(outlst)+1, "BRLEQ", outlst[len(outlst)-1][4], "", "", ""))
                elif outlst[len(outlst)-1][1] == "BRLT":
                    outlst[len(outlst)-1] = ((outlst[len(outlst)-1][0], "compr", outlst[len(outlst)-1][2],
                                              outlst[len(outlst)-1][3], outlst[len(outlst)-1][4],
                                              outlst[len(outlst)-1][5]))
                    outlst.append((len(outlst)+1, "BRLT", outlst[len(outlst)-1][4], "", "", ""))
                elif outlst[len(outlst)-1][1] == "BREQ":
                    outlst[len(outlst)-1] = ((outlst[len(outlst)-1][0], "compr", outlst[len(outlst)-1][2],
                                              outlst[len(outlst)-1][3], outlst[len(outlst)-1][4],
                                              outlst[len(outlst)-1][5]))
                    outlst.append((len(outlst)+1, "BREQ", outlst[len(outlst)-1][4], "", "", ""))
                elif outlst[len(outlst)-1][1] == "BRNEQ":
                    outlst[len(outlst)-1] = ((outlst[len(outlst)-1][0], "compr", outlst[len(outlst)-1][2],
                                              outlst[len(outlst)-1][3], outlst[len(outlst)-1][4],
                                              outlst[len(outlst)-1][5]))
                    outlst.append((len(outlst)+1, "BRNEQ", outlst[len(outlst)-1][4], "", "", ""))
                else:
                    outlst.append((len(outlst) + 1, "BR", result, "", "", ""))
                temp = len(outlst) - 1
                statement()
                outlst[temp] = ((outlst[temp][0], outlst[temp][1], outlst[temp][2], outlst[temp][3],
                                 len(outlst)+2, "bpf = {0}".format(outlst[temp][0])))
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
        outlst.append((len(outlst) + 1, "BR", "", "", "", ""))
        temp = len(outlst) - 1
        statement()
        outlst[temp] = ((outlst[temp][0], outlst[temp][1], outlst[temp][2], outlst[temp][3],
                         len(outlst) + 1, "bpo = {0}".format(outlst[temp][0]+1)))
    else:
        return


def iteration_stmt():
    global cntr, lh, buff, outlst
    bpw = 0
    if buff[lh][1] == "while":
        match("while")
        if buff[lh][1] == "(":
            match("(")
            bpo = len(outlst) + 1
            result = expression()
            outlst[bpo-1] = ((outlst[bpo-1][0], outlst[bpo-1][1], outlst[bpo-1][2], outlst[bpo-1][3],
                              outlst[bpo-1][4], "bpw = {0}".format(bpo)))
            if buff[lh][1] == ")":
                match(")")
                if outlst[len(outlst) - 1][1] == "BRGEQ":
                    outlst[len(outlst) - 1] = ((outlst[len(outlst) - 1][0], "compr", outlst[len(outlst) - 1][2],
                                                outlst[len(outlst) - 1][3], outlst[len(outlst) - 1][4],
                                                outlst[len(outlst) - 1][5]))
                    outlst.append((len(outlst) + 1, "BRGEQ", outlst[len(outlst) - 1][4], "", "", ""))
                elif outlst[len(outlst) - 1][1] == "BRGT":
                    outlst[len(outlst) - 1] = ((outlst[len(outlst) - 1][0], "compr", outlst[len(outlst) - 1][2],
                                                outlst[len(outlst) - 1][3], outlst[len(outlst) - 1][4],
                                                outlst[len(outlst) - 1][5]))
                    outlst.append((len(outlst) + 1, "BRGT", outlst[len(outlst) - 1][4], "", "", ""))
                elif outlst[len(outlst) - 1][1] == "BRLEQ":
                    outlst[len(outlst) - 1] = ((outlst[len(outlst) - 1][0], "compr", outlst[len(outlst) - 1][2],
                                                outlst[len(outlst) - 1][3], outlst[len(outlst) - 1][4],
                                                outlst[len(outlst) - 1][5]))
                    outlst.append((len(outlst) + 1, "BRLEQ", outlst[len(outlst) - 1][4], "", "", ""))
                elif outlst[len(outlst) - 1][1] == "BRLT":
                    outlst[len(outlst) - 1] = ((outlst[len(outlst) - 1][0], "compr", outlst[len(outlst) - 1][2],
                                                outlst[len(outlst) - 1][3], outlst[len(outlst) - 1][4],
                                                outlst[len(outlst) - 1][5]))
                    outlst.append((len(outlst) + 1, "BRLT", outlst[len(outlst) - 1][4], "", "", ""))
                elif outlst[len(outlst) - 1][1] == "BREQ":
                    outlst[len(outlst) - 1] = ((outlst[len(outlst) - 1][0], "compr", outlst[len(outlst) - 1][2],
                                                outlst[len(outlst) - 1][3], outlst[len(outlst) - 1][4],
                                                outlst[len(outlst) - 1][5]))
                    outlst.append((len(outlst) + 1, "BREQ", outlst[len(outlst) - 1][4], "", "", ""))
                elif outlst[len(outlst) - 1][1] == "BRNEQ":
                    outlst[len(outlst) - 1] = ((outlst[len(outlst) - 1][0], "compr", outlst[len(outlst) - 1][2],
                                                outlst[len(outlst) - 1][3], outlst[len(outlst) - 1][4],
                                                outlst[len(outlst) - 1][5]))
                    outlst.append((len(outlst) + 1, "BRNEQ", outlst[len(outlst) - 1][4], "", "", ""))
                else:
                    outlst.append((len(outlst) + 1, "BR", result, "", "", ""))
                temp = len(outlst) - 1
                statement()
                outlst.append((len(outlst) + 1, "BR", "", "", bpo, ""))
                outlst[temp] = ((outlst[temp][0], outlst[temp][1], outlst[temp][2], outlst[temp][3],
                                 len(outlst) + 1, "bpo = {0}".format(outlst[temp][0])))
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
        ret = return_stmtp()
        outlst.append((len(outlst) + 1, "return", "", "", ret, ""))
    else:
        print("REJECT")
        exit()


def return_stmtp():
    global cntr, lh, buff
    if buff[lh][1] == ";":
        match(";")
        return
    elif buff[lh][1] == "ID":
        left = buff[lh][0]
        match("ID")
        return_stmtpp(left)
    elif buff[lh][1] == "(":
        match("(")
        left = expression()
        if buff[lh][1] == ")":
            match(")")
            if buff[lh][1] in ["*", "/"]:
                left = termp(left)
            if buff[lh][1] in ["+", "-"]:
                left = additive_expressionp(left)
            if buff[lh][1] in ["!=", "<", "<=", "==", ">", ">="]:
                left = simple_expressionp(left)
            if buff[lh][1] == ";":
                match(";")
                return left
            else:
                print("REJECT")
                exit()
        else:
            print("REJECT")
            exit()
    elif buff[lh][1] == "NUM":
        left = buff[lh][0]
        match("NUM")
        if buff[lh][1] in ["*", "/"]:
            left = termp(left)
        if buff[lh][1] in ["+", "-"]:
            left = additive_expressionp(left)
        if buff[lh][1] in ["!=", "<", "<=", "==", ">", ">="]:
            left = simple_expressionp(left)
        if buff[lh][1] == ";":
            match(";")
            return left
        else:
            print("REJECT")
            exit()
    else:
        print("REJECT")
        exit()


def return_stmtpp(left):
    global cntr, lh, buff, varcnt, outlst
    if buff[lh][1] == ";":
        match(";")
        return ()
    elif buff[lh][1] in ["!=", "*", "+", "-", "/", "<", "<=", "=", "==", ">", ">=", "["]:
        left = varp(left)
        return_stmtppp(left)
    elif buff[lh][1] == "(":
        match("(")
        args()
        if buff[lh][1] == ")":
            match(")")
            varcnt += 1
            subvar = "_t" + str(varcnt)
            chk = [x[1] for x in outlst].index(left)
            outlst.append((len(outlst)+1, "call", left, outlst[chk][4], subvar, ""))
            if buff[lh][1] in ["*", "/"]:
                subvar = termp(subvar)
            if buff[lh][1] in ["+", "-"]:
                subvar = additive_expressionp(subvar)
            if buff[lh][1] in ["!=", "<", "<=", "==", ">", ">="]:
                subvar = simple_expressionp(subvar)
            if buff[lh][1] == ";":
                match(";")
                return subvar
            else:
                print("REJECT")
                exit()
        else:
            print("REJECT")
            exit()
    else:
        print("REJECT")
        exit()


def return_stmtppp(left):
    global cntr, lh, buff
    if buff[lh][1] == ";":
        match(";")
        return left
    elif buff[lh][1] == "=":
        match("=")
        left = expression()
        if buff[lh][1] == ";":
            match(";")
            return left
        else:
            print("REJECT")
            exit()
    elif buff[lh][1] in ["!=", "*", "+", "-", "/", "<", "<=", "=", "==", ">", ">="]:
        if buff[lh][1] in ["*", "/"]:
            left = termp(left)
        if buff[lh][1] in ["+", "-"]:
            left = additive_expressionp(left)
        if buff[lh][1] in ["!=", "<", "<=", "==", ">", ">="]:
            left = simple_expressionp(left)
        if buff[lh][1] == ";":
            match(";")
            return left
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
        left = expressionp(left)
        return left
    elif buff[lh][1] == "(":
        match("(")
        left = expression()
        if buff[lh][1] == ")":
            match(")")
            if buff[lh][1] in ["*", "/"]:
                left = termp(left)
            if buff[lh][1] in ["+", "-"]:
                left = additive_expressionp(left)
            if buff[lh][1] in ["!=", "<", "<=", "==", ">", ">="]:
                left = simple_expressionp(left)
            return left
        else:
            print("REJECT")
            exit()
    elif buff[lh][1] == "NUM":
        left = buff[lh][0]
        match("NUM")
        if buff[lh][1] in ["*", "/"]:
            left = termp(left)
        if buff[lh][1] in ["+", "-"]:
            left = additive_expressionp(left)
        if buff[lh][1] in ["!=", "<", "<=", "==", ">", ">="]:
            left = simple_expressionp(left)
        return left
    else:
        print("REJECT")
        exit()


def expressionp(left):
    global cntr, lh, buff, varcnt, outlst
    if buff[lh][1] in ["!=", "*", "+", "-", "/", "<", "<=", "=", "==", ">", ">=", "["]:
        left = varp(left)
        return expressionpp(left)
    elif buff[lh][1] == "(":
        match("(")
        args()
        if buff[lh][1] == ")":
            match(")")
            varcnt += 1
            subvar = "_t" + str(varcnt)
            chk = [x[2] for x in outlst].index(left)
            outlst.append((len(outlst)+1, "call", left, outlst[chk][4], subvar, ""))
            if buff[lh][1] in ["*", "/"]:
                subvar = termp(subvar)
            if buff[lh][1] in ["+", "-"]:
                subvar = additive_expressionp(subvar)
            if buff[lh][1] in ["!=", "<", "<=", "==", ">", ">="]:
                subvar = simple_expressionp(left)
            return subvar
        else:
            print("REJECT")
            exit()
    else:
        return left


def expressionpp(left):
    global cntr, lh, buff, outlst
    if buff[lh][1] == "=":
        match("=")
        result = expression()
        outlst.append((len(outlst)+1, "asign", result, " ", left, ""))
    elif buff[lh][1] in ["!=", "*", "+", "-", "/", "<", "<=", "==", ">", ">="]:
        if buff[lh][1] in ["*", "/"]:
            left = termp(left)
        if buff[lh][1] in ["+", "-"]:
            left = additive_expressionp(left)
        if buff[lh][1] in ["!=", "<", "<=", "==", ">", ">="]:
            left = simple_expressionp(left)
        return left
    else:
        return left


def isint(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def varp(left):
    global cntr, lh, buff, varcnt, outlst
    if buff[lh][1] == "[":
        match("[")
        result = expression()
        if buff[lh][1] == "]":
            match("]")
            varcnt += 1
            subvar = "_t"+str(varcnt)
            if isint(result):
                num = 4 * int(result)
                outlst.append((len(outlst) + 1, "disp", left, num, subvar, ""))
            else:
                outlst.append((len(outlst) + 1, "mult", 4, result, subvar, ""))
                temp = subvar
                varcnt += 1
                subvar = "_t" + str(varcnt)
                outlst.append((len(outlst) + 1, "disp", left, temp, subvar, ""))
            return subvar
        else:
            print("REJECT")
            exit()
    else:
        return left


def simple_expressionp(left):
    global cntr, lh, buff, outlst, varcnt
    if buff[lh][1] == "<=":
        match("<=")
        right = additive_expression()
        varcnt += 1
        subvar = "_t" + str(varcnt)
        outlst.append((len(outlst) + 1, "BRGEQ", left, right, subvar, ""))
        return right
    elif buff[lh][1] == "<":
        match("<")
        right = additive_expression()
        varcnt += 1
        subvar = "_t" + str(varcnt)
        outlst.append((len(outlst) + 1, "BRGT", left, right, subvar, ""))
        return right
    elif buff[lh][1] == ">":
        match(">")
        right = additive_expression()
        varcnt += 1
        subvar = "_t" + str(varcnt)
        outlst.append((len(outlst) + 1, "BRLT", left, right, subvar, ""))
        return right
    elif buff[lh][1] == ">=":
        match(">=")
        right = additive_expression()
        varcnt += 1
        subvar = "_t" + str(varcnt)
        outlst.append((len(outlst) + 1, "BRLEQ", left, right, subvar, ""))
        return right
    elif buff[lh][1] == "==":
        match("==")
        right = additive_expression()
        varcnt += 1
        subvar = "_t" + str(varcnt)
        outlst.append((len(outlst) + 1, "BREQ", left, right, subvar, ""))
        return right
    elif buff[lh][1] == "!=":
        match("!=")
        right = additive_expression()
        varcnt += 1
        subvar = "_t" + str(varcnt)
        outlst.append((len(outlst) + 1, "BRNEQ", left, right, subvar, ""))
        return right
    else:
        return left


def additive_expression():
    global cntr, lh, buff
    if buff[lh][1] in ["(", "ID", "NUM"]:
        right = term()
        return additive_expressionp(right)
    else:
        print("REJECT")
        exit()


def additive_expressionp(left):
    global cntr, lh, buff, varcnt, outlst
    if buff[lh][1] in ["+", "-"]:
        center = addop()
        right = term()
        varcnt += 1
        subvar = "_t" + str(varcnt)
        outlst.append((len(outlst)+1, center, left, right, subvar, ""))
        subvar = additive_expressionp(subvar)
        return subvar
    else:
        return left


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
        right = termp(left)
        if right is not None: return right
        else: return left
    else:
        print("REJECT")
        exit()


def termp(left):
    global cntr, lh, buff, varcnt, outlst
    if buff[lh][1] in ["*", "/"]:
        center = mulop()
        right = factor()
        varcnt += 1
        subvar = "_t" + str(varcnt)
        outlst.append((len(outlst)+1, center, left, right, subvar, ""))
        subvar = termp(subvar)
        return subvar
    else:
        return left


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
        result = expression()
        if buff[lh][1] == ")":
            match(")")
            return result
        else:
            print("REJECT")
            exit()
    elif buff[lh][1] == "ID":
        right = buff[lh][0]
        match("ID")
        right = factorp(right)
        return right
    elif buff[lh][1] == "NUM":
        right = buff[lh][0]
        match("NUM")
        return right
    else:
        print("REJECT")
        exit()


def factorp(right):
    global cntr, lh, buff, varcnt, outlst
    if buff[lh][1] == "[":
        right = varp(right)
        return right
    elif buff[lh][1] == "(":
        match("(")
        args()
        if buff[lh][1] == ")":
            match(")")
            varcnt += 1
            subvar = "_t" + str(varcnt)
            chk = [x[1] for x in outlst].index(right)
            outlst.append((len(outlst)+1, "call", right, outlst[chk][4], subvar, ""))
            return subvar
        else:
            print("REJECT")
            exit()
    else:
        return right


def call(left):
    global cntr, lh, buff, varcnt, outlst
    if buff[lh][1] == "ID":
        match("ID")
        if buff[lh][1] == "(":
            match("(")
            args()
            if buff[lh][1] == ")":
                match(")")
                varcnt += 1
                subvar = "_t" + str(varcnt)
                chk = [x[1] for x in outlst].index(left)
                outlst.append((len(outlst)+1, "call", left, outlst[chk][4], subvar, ""))
                return subvar
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
        return


def arg_list():
    global cntr, lh, buff
    if buff[lh][1] == "ID":
        left = buff[lh][0]
        match("ID")
        left = arg_listpp(left)
        outlst.append((len(outlst) + 1, "arg", "", "", left, ""))
    elif buff[lh][1] == "(":
        match("(")
        left = expression()
        if buff[lh][1] == ")":
            match(")")
            if buff[lh][1] in ["*", "/"]:
                left = termp(left)
            if buff[lh][1] in ["+", "-"]:
                left = additive_expressionp(left)
            if buff[lh][1] in ["!=", "<", "<=", "==", ">", ">="]:
                left = simple_expressionp(left)
            outlst.append((len(outlst) + 1, "arg", "", "", left, ""))
            arg_listp()
        else:
            print("REJECT")
            exit()
    elif buff[lh][1] == "NUM":
        left = buff[lh][0]
        match("NUM")
        if buff[lh][1] in ["*", "/"]:
            left = termp(left)
        if buff[lh][1] in ["+", "-"]:
            left = additive_expressionp(left)
        if buff[lh][1] in ["!=", "<", "<=", "==", ">", ">="]:
            left = simple_expressionp(left)
        outlst.append((len(outlst) + 1, "arg", "", "", left, ""))
        arg_listp()
    else:
        print("REJECT")
        exit()


def arg_listp():
    global cntr, lh, buff
    if buff[lh][1] == ",":
        match(",")
        res = expression()
        outlst.append((len(outlst) + 1, "arg", "", "", res, ""))
        arg_listp()
    else:
        return


def arg_listpp(left):
    global cntr, lh, buff, varcnt, outlst
    if buff[lh][1] in ["!=", "*", "+", "-", "/", "<", "<=", "=", "==", ">", ">=", "[", ","]:
        left = varp(left)
        left = arg_listppp(left)
        outlst.append((len(outlst) + 1, "arg", "", "", left, ""))
    elif buff[lh][1] == "(":
        match("(")
        args()
        if buff[lh][1] == ")":
            match(")")
            varcnt += 1
            subvar = "_t" + str(varcnt)
            chk = [x[1] for x in outlst].index(left)
            outlst.append((len(outlst)+1, "call", left, outlst[chk][4], subvar, ""))
            if buff[lh][1] in ["*", "/"]:
                subvar = termp(subvar)
            if buff[lh][1] in ["+", "-"]:
                subvar = additive_expressionp(subvar)
            if buff[lh][1] in ["!=", "<", "<=", "==", ">", ">="]:
                subvar = simple_expressionp(subvar)
            outlst.append((len(outlst) + 1, "arg", "", "", subvar, ""))
            arg_listp()
    else:
        return left


def arg_listppp(left):
    global cntr, lh, buff, outlst
    if buff[lh][1] == "=":
        match("=")
        result = expression()
        outlst.append((len(outlst)+1, "asign", result, "", left, ""))
        outlst.append((len(outlst)+1, "arg", "", "", left, ""))
        arg_listp()
    elif buff[lh][1] in ["!=", "*", "+", "-", "/", "<", "<=", "=", "==", ">", ">=", ","]:
        if buff[lh][1] in ["*", "/"]:
            left = termp(left)
        if buff[lh][1] in ["+", "-"]:
            left = additive_expressionp(left)
        if buff[lh][1] in ["!=", "<", "<=", "==", ">", ">="]:
            left = simple_expressionp(left)
        outlst.append((len(outlst) + 1, "arg", "", "", left, ""))
        arg_listp()
    else:
        return left


parser()
