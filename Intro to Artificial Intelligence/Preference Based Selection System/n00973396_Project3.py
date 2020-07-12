import Tkinter as tk
import os

entryTexts = []
entries = []
solveable = False
textBoxes = [0] * 3
boxDesc = ['Attributes', 'Constraints', 'Preferences']


def read_attr_file(fn):
    attribToVar = {}
    attribName = {}
    num_attr = 1
    with open(fn) as f:
        for line in f.readlines():
            line = line.strip()
            if not line:
                continue
            print(line)
            words = line.strip().split(':')
            desc = words[0].strip()
            words = words[1].split(',')
            varPos = words[0].strip()
            varNeg = words[1].strip()
            attribToVar[varPos] = num_attr
            attribToVar[varNeg] = -num_attr
            attribName[num_attr] = varPos
            attribName[-num_attr] = varNeg
            num_attr += 1
    return attribToVar, attribName, num_attr - 1


def read_const_file(fn, attribToVar):
    result = ''
    totalcons = 0
    with open(fn) as f:
        for line in f.readlines():
            words = line.strip().split('OR')
            for literal in words:
                literal = literal.strip().split()
                var = 1
                for lit in literal:
                    if lit == 'NOT':
                        var *= -1
                    else:
                        var *= attribToVar[lit]
                print('{} -> {}'.format(literal, var))
                result += str(var) + ' '
            result += '0\n'
            totalcons += 1
    return result, totalcons


def read_pref_file(fn, attribToVar):
    prefdata = []
    with open(fn) as f:
        for line in f.readlines():
            line = line.strip()
            if not line:
                continue
            words = line.strip().split(',')
            value = float(words[1])  # right is value
            cnf = words[0]  # left is CNF
            clauses = cnf.split('AND')  # CNF is a bunch of AND clauses
            for i in range(len(clauses)):
                clauses[i] = clauses[i].split('OR')
                codedformat = []
                for literal in clauses[i]:
                    literal = literal.strip().split()
                    var = 1
                    for lit in literal:
                        if lit == 'NOT':
                            var *= -1
                        else:
                            var *= attribToVar[lit]
                    codedformat.append(var)
                clauses[i] = codedformat
            prefdata.append((clauses, value))
        print(prefdata)
    return prefdata


def compute_pref(answers, prefdata):
    scores = {}
    # for each answer (dict id->list)
    for k, a in answers.items():
        print('Checking answer {} -> {}'.format(k, a))
        num_attr = len(a)
        scores[k] = 0
        # for each preference
        for j in range(len(prefdata)):
            preflist, prefscore = prefdata[j]
            totalcons = len(preflist) + num_attr
            s = ''
            for l in preflist:
                for n in l:
                    s += str(n) + ' '
                s += '0\n'
            # add this answer k
            s += ' 0\n'.join([str(i) for i in a])
            s += ' 0\n'
            # write file for clasp to read
            with open('tmpcnf.txt', 'w') as f:
                f.write('p cnf ' + str(num_attr) + ' ' + str(totalcons) + '\n')
                f.write(s);
            os.system('clasp 0 < tmpcnf.txt > tmpout.txt')
            feedback = readFromFile('tmpout.txt')
            if feedback.find('UNSATISFIABLE') < 0:
                scores[k] += prefscore
    return scores


def runClasp(num_attr, hardcons, totalcons):
    with open('tmpcnf.txt', 'w') as f:
        f.write('p cnf ' + str(num_attr) + ' ' + str(totalcons) + '\n')
        f.write(hardcons);
    os.system('clasp 0 < tmpcnf.txt > tmpout.txt')
    answers = {}
    with open('tmpout.txt') as f:
        ansflag = False
        anskey = ''
        for line in f.readlines():
            print(line.strip())
            words = line.split(':')
            if ansflag:
                ansflag = False
                answers[anskey] = [int(i) for i in line.split()[1:-1]]
            elif words[0] == 'c Answer':
                ansflag = True
                anskey = int(words[1].strip())
        print(answers)
    return answers


def readFromFile(fn):
    with open(fn) as f:
        return f.read()


def writeToFile(fn, txt):
    with open(fn, 'w') as f:
        f.write(txt)


def show_button():
    try:
        att_txt = readFromFile(entryTexts[0].get())
    except:
        att_txt = ''
    try:
        cons_txt = readFromFile(entryTexts[1].get())
    except:
        cons_txt = ''
    try:
        pref_txt = readFromFile(entryTexts[2].get())
    except:
        pref_txt = ''

    if att_txt:
        textBoxes[0].delete("1.0", END)
        textBoxes[0].insert("1.0", att_txt)
    if cons_txt:
        textBoxes[1].delete("1.0", END)
        textBoxes[1].insert("1.0", cons_txt)
    if pref_txt:
        textBoxes[2].delete("1.0", END)
        textBoxes[2].insert("1.0", pref_txt)

    att_txt = textBoxes[0].get("1.0", END)
    cons_txt = textBoxes[1].get("1.0", END)
    pref_txt = textBoxes[2].get("1.0", END)
    writeToFile('att_tmp.txt', att_txt)
    writeToFile('cons_tmp.txt', cons_txt)
    writeToFile('pref_tmp.txt', pref_txt)
    txt1.delete("1.0", END)
    try:
        attribToVar, attribName, num_attr = read_attr_file('att_tmp.txt')
    except:
        txt1.insert(END, 'Error reading attributes!\n')
    try:
        hardcons, totalcons = read_const_file('cons_tmp.txt', attribToVar)
    except:
        txt1.insert(END, 'Error reading constraints!\n')
    try:
        answers = runClasp(num_attr, hardcons, totalcons)
    except:
        txt1.insert(END, 'Error running clasp!\n')
        answers = []

    if len(answers) > 0:
        solveable = True
        num_attr = len(answers)
        txt1.insert(END, '1. Solvable!\n')
    else:
        txt1.insert(END, '1. Not solvable!\n')

    try:
        print('Reading preferences')
        prefdata = read_pref_file('pref_tmp.txt', attribToVar)
    except:
        txt1.insert(END, 'Error reading preferences!\n')

    try:
        scores = compute_pref(answers, prefdata)
    except:
        txt1.insert(END, 'Error computing preferences!\n')

    if len(answers) > 1:
        for k, v in sorted(scores.items(), key=lambda p: p[1])[:len(answers)]:
            s = '2. Score: {} Solution: '.format(v)
            for l in answers[k]:
                s += attribName[l] + ' '
            if k == len(answers):
                txt1.insert(END, s + '\nmay be less preferable to\n')

        for k, v in sorted(scores.items(), key=lambda p: p[1])[:1]:
            s = 'Score: {} Solution: '.format(v)
            for l in answers[k]:
                s += attribName[l] + ' '
            txt1.insert(END, s + '\n')

        for k, v in sorted(scores.items(), key=lambda p: p[1])[:1]:
            s = '3. Optimal Solution: Score: {} Solution: '.format(v)
            for l in answers[k]:
                s += attribName[l] + ' '
            txt1.insert(END, s + '\n')

        txt1.insert(END, '4. All Optimal Solutions: \n')

        for k, v in sorted(scores.items(), key=lambda p: p[1])[:1]:
            s = 'Score: {} Solution: '.format(v)
            t = s
        for k, v in sorted(scores.items(), key=lambda p: p[1])[:len(answers)]:
            s = 'Score: {} Solution: '.format(v)
            if s == t:
                for l in answers[k]:
                    s += attribName[l] + ' '
                    txt1.insert(END, s + '\n')

    else:
        txt1.insert(END, 'There is only one solution!:\n')
        for k, v in sorted(scores.items(), key=lambda p: p[1])[:1]:
            s = 'Score: {} Solution: '.format(v)
            for l in answers[k]:
                s += attribName[l] + ' '
            txt1.insert(END, s + '\n')


def reset_button():
    for i in range(3):
        entryTexts[i].set('')


from Tkinter import *

m = tk.Tk()
m.title('N00963396 Ethan Paffe Project 3')
m.geometry('900x750')
Label(m, text='Enter filenames below or manually enter text into fields below.').grid(row=1)
Label(m, text='Or you may enter an attribute filename:').grid(row=2)
Label(m, text='Enter an hard constraints filename:').grid(row=3)
Label(m, text='Enter an preferences filename:').grid(row=4)

for i in range(3):
    entryTexts.append(tk.StringVar())
    entries.append(Entry(m, textvariable=entryTexts[i]))
    entries[i].grid(row=i + 2, column=1, columnspan=2)

show = Button(m, text='Show Results', command=show_button)
reset = Button(m, text='reset', command=reset_button)

show.grid(row=5, column=0)
reset.grid(row=6, column=1)

for i in range(3):
    Label(m, text=boxDesc[i]).grid(row=10 * (i + 1) - 1)

    textBoxes[i] = Text(m, height=8, width=40)
    textBoxes[i].grid(row=10 * (i + 1), column=0, rowspan=5, columnspan=10)

    scrollb = Scrollbar(m, command=textBoxes[i].yview)
    scrollb.grid(row=10 * (i + 1), column=1, rowspan=5, sticky='nsew')
    textBoxes[i]['yscrollcommand'] = scrollb.set

Label(m, text='Output').grid(row=9, column=20)
txt1 = Text(m, height=35, width=50)
txt1.grid(row=10, column=20, rowspan=25, columnspan=10)
scrollb = Scrollbar(m, command=txt1.yview)
scrollb.grid(row=10, column=30, rowspan=25, sticky='nsew')
txt1['yscrollcommand'] = scrollb.set
txt1.delete("1.0", END)

m.mainloop()