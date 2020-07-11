from sys import *


# Special characters and keywords in the C- language
keywords = ['else', 'if', 'int', 'return', 'void', 'while']
num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symb = [',', ';', '(', ')', '{', '}', '[', ']']
whitespace = ['\t', '\n', ' ']
ops = ['+', '-', '*', '/', '<', '>', '<=', '>=', '==', '!=', '=']


outLst = []


# Reads input given as an argument from the console
def read_file(filename):
    try:
        lines = open(filename, "r").readlines()
        return lines
    except IOError:
        print("File not found")
        exit()
    except IndexError:
        print("Please enter a filename")
        exit()


# Inserts item into output list
def insert(outLst, key, val):
    outLst.append((key, val))


# Divides each line from the given input into tokens
def tokenize(line):
    tokens = []
    for char_index in range(len(line)):
        tokens += line[char_index]
    return tokens


# Checks if a given character is a letter in the English alphabet
def is_letter(char):
    return 97 <= ord(char) <= 122


# Checks if character is a number
def is_num(char):
    if char in num:
        return True
    else:
        return False


# Checks if character is a valid symbol
def is_symb(char):
    if char in symb:
        return True
    else:
        return False


# Checks if character is an operator symbol
def is_op(char):
    if char in ops:
        return True
    else:
        return False


# Checks if string is a keyword
def is_keyword(tst_str):
    if tst_str in keywords:
        return True
    else:
        return False


# Checks if character is in whitespace
def is_ws(char):
    if char in whitespace:
        return True
    else:
        return False


# Analyzes tokens given by tokenizer, finding keywords and errors
def lexer(filename):
    lines = list(read_file(filename))
#   flag for comments
    cmnt_flag = False
#   stores identifiers
    idnt = ""
#   stores numerical values
    val = ""
#   stores error values
    err = ""
#   flag for errors
    err_flag = False
# stores value for operators
    op = ""
    for line in lines:
        if is_ws(line):
            continue
        else:
            #print "INPUT: {0}".format(line.strip())
            tokens = tokenize(line + " ")
            for char in range(len(tokens)):
                if err_flag:
                    err += tokens[char]
                    if is_ws(tokens[char+1]) or is_symb(tokens[char+1]) or is_op(tokens[char+1]):
                        err_flag = False
                        #print "Error: {0}".format(err)
                        print ("REJECT")
                        err = ""
                        exit()
                else:
                    if tokens[char] == '/' and tokens[char+1] == '/':
                        break
                    elif tokens[char] == '/' and tokens[char+1] == '*':
                        cmnt_flag = True
                        continue
                    elif cmnt_flag and tokens[char] == '/' and tokens[char-1] == '*':
                        cmnt_flag = False
                        continue
                    elif cmnt_flag:
                        continue
                    if is_letter(tokens[char]):
                        idnt += tokens[char]
                        if not is_letter(tokens[char+1]):
                            if is_keyword(idnt):
                                #print 'KW: {0}'.format(idnt)
                                #outLst.append('{0}'.format(idnt))
                                insert(outLst, "", idnt)
                                idnt = ""
                            else:
                                #print 'ID: {0}'.format(idnt)
                                #outLst.append('ID'.format(idnt))
                                insert(outLst, idnt, "ID")
                                idnt = ""
                    if is_num(tokens[char]):
                        val += tokens[char]
                        if is_num(tokens[char+1]):
                            continue
                        elif not is_num(tokens[char+1]):
                            #print "INT: {0}".format(val)
                            #outLst.append("NUM".format(val))
                            insert(outLst, int(val), "NUM")
                            val = ""
                    if is_symb(tokens[char]):
                        #print '{0}'.format(tokens[char])
                        #outLst.append('{0}'.format(tokens[char]))
                        insert(outLst, "", tokens[char])
                        if tokens[char] == ';' or tokens[char] == '{':
                            #print ""
                            pass
                    if is_op(tokens[char]) or tokens[char] == '!':
                        op += tokens[char]
                        temp = op + tokens[char+1]
                        if len(op) == 2 and is_op(tokens[char+1]):
                            err_flag = True
                            err += op
                            op = ""
                            continue
                        elif tokens[char] == '!' and not is_op(temp):
                            #print "Error {0}".format(op)
                            #outLst.append("Error".format(op))
                            print("REJECT")
                            op = ""
                            exit()
                        elif is_op(temp):
                            continue
                        else:
                            #print "{0}".format(op)
                            #outLst.append("{0}".format(op))
                            insert(outLst, "", op)
                            op = ""
                    if (not is_letter(tokens[char]) and not is_num(tokens[char]) and not is_symb(tokens[char])
                            and not is_op(tokens[char]) and not is_keyword(tokens[char])
                            and tokens[char] != '!' and not is_ws(tokens[char])):
                        err_flag = True
                        err += tokens[char]
    #print outLst
    return outLst
