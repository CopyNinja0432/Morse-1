from tkinter import *
from tkinter import ttk

a = "O " + "- "
b = "- " + "O " + "O " + "O "
c = "- " + "O " + "- " + "O "
d = "- " + "O " + "O "
e = "O "
f = "O " + "O " + "- " + "O "
g = "- " + "- " + "O "
h = "O " + "O " + "O " + "O "
i = "O " + "O"
j = "O " + "- " + "- " + "- "
k = "- " + "O " + "- "
l = "O " + "- " + "O " + "O "
m = "- " + "- "
n = "- " + "O "
o = "- " + "- " + "- "
p = "O " + "- " + "- " + "O "
q = "- " + "- " + "O " + "- "
r = "O " + "- " + "O "
s = "O " + "O " + "O "
t = "- "
u = "O " + "O " + "- "
v = "O " + "O " + "O " + "- "
w = "O " + "- " + "- "
x  = "- " + "O " + "O " + "- "
y = "- " + "O " + "- " + "- "
z = "- " + "- " + "O " + "O "

space = "/"

n1 = "O " + "- " + "- " + "- " + "- "
n2 = "O " + "O " + "- " + "- " + "- "
n3 = "O " + "O " + "O " + "- " + "- "
n4 = "O " + "O " + "O " + "O " + "- "
n5 = "O " + "O " + "O " + "O " + "O "
n6 = "- " + "O " + "O " + "O " + "O "
n7 = "- " + "- " + "O " + "O " + "O "
n8 = "- " + "- " + "- " + "O " + "O "
n9 = "- " + "- " + "- " + "- " + "O "
n0 = "- " + "- " + "- " + "- " + "- "

spaceCounter = 0

def translator():
    button.pack_forget()
    choice1.pack()
    choice2.pack()

def translateE():
    choice1.pack_forget()
    choice2.pack_forget()
    wordE.pack()
    submitE.pack()

def resultM():
    global wordE
    string = wordE.get()
    print([*string])
    zeroString = ""
    for X in [*string]:
        if "a" in X or "A" in X:
            global a
            zeroString = zeroString + a
            answer.config(text=zeroString)
            answer.pack()
        elif "b" in X or "B" in X:
            global b
            zeroString = zeroString + b
            answer.config(text=zeroString)
            answer.pack()
        elif "c" in X or "C" in X:
            global c
            zeroString = zeroString + c
            answer.config(text=zeroString)
            answer.pack()
        elif "d" in X or "D" in X:
            global d
            zeroString = zeroString + d
            answer.config(text=zeroString)
            answer.pack()
        elif "e" in X or "E" in X:
            global e
            zeroString = zeroString + e
            answer.config(text=zeroString)
            answer.pack()
        elif "f" in X or "F" in X:
            global f
            zeroString = zeroString + f
            answer.config(text=zeroString)
            answer.pack()
        elif "g" in X or "G" in X:
            global g
            zeroString = zeroString + g
            answer.config(text=zeroString)
            answer.pack()
        elif "h" in X or "H" in X:
            global h
            zeroString = zeroString + h
            answer.config(text=zeroString)
            answer.pack()
        elif "i" in X or "I" in X:
            global i
            zeroString = zeroString + i
            answer.config(text=zeroString)
            answer.pack()
        elif "j" in X or "J" in X:
            global j
            zeroString = zeroString + j
            answer.config(text=zeroString)
            answer.pack()
        elif "k" in X or "K" in X:
            global k
            zeroString = zeroString + k
            answer.config(text=zeroString)
            answer.pack()
        elif "l" in X or "L" in X:
            global l
            zeroString = zeroString + l
            answer.config(text=zeroString)
            answer.pack()
        elif "m" in X or "M" in X:
            global m
            zeroString = zeroString + m
            answer.config(text=zeroString)
            answer.pack()
        elif "n" in X or "N" in X:
            global n
            zeroString = zeroString + n
            answer.config(text=zeroString)
            answer.pack()
        elif "o" in X or "O" in X:
            global o
            zeroString = zeroString + o
            answer.config(text=zeroString)
            answer.pack()
        elif "p" in X or "P" in X:
            global p
            zeroString = zeroString + p
            answer.config(text=zeroString)
            answer.pack()
        elif "q" in X or "Q" in X:
            global q
            zeroString = zeroString + q
            answer.config(text=zeroString)
            answer.pack()
        elif "r" in X or "R" in X:
            global r
            zeroString = zeroString + r
            answer.config(text=zeroString)
            answer.pack()
        elif "s" in X or "S" in X:
            global s
            zeroString = zeroString + s
            answer.config(text=zeroString)
            answer.pack()
        elif "t" in X or "T" in X:
            global t
            zeroString = zeroString + t
            answer.config(text=zeroString)
            answer.pack()
        elif "u" in X or "U" in X:
            global u
            zeroString = zeroString + u
            answer.config(text=zeroString)
            answer.pack()
        elif "v" in X or "V" in X:
            global v
            zeroString = zeroString + v
            answer.config(text=zeroString)
            answer.pack()
        elif "w" in X or "W" in X:
            global w
            zeroString = zeroString + w
            answer.config(text=zeroString)
            answer.pack()
        elif "x" in X or "X" in X:
            global x
            zeroString = zeroString + x
            answer.config(text=zeroString)
            answer.pack()
        elif "y" in X or "Y" in X:
            global y
            zeroString = zeroString + y
            answer.config(text=zeroString)
            answer.pack()
        elif "z" in X or "Z" in X:
            global z
            zeroString = zeroString + z
            answer.config(text=zeroString)
            answer.pack()
        elif " " in X:
            global space
            zeroString = zeroString + space
            answer.config(text=zeroString)
            answer.pack()
        elif "1" in X:
            global n1
            zeroString = zeroString + n1
            answer.config(text=zeroString)
            answer.pack()
        elif "2" in X:
            global n2
            zeroString = zeroString + n2
            answer.config(text=zeroString)
            answer.pack()
        elif "3" in X:
            global n3
            zeroString = zeroString + n3
            answer.config(text=zeroString)
            answer.pack()
        elif "4" in X:
            global n4
            zeroString = zeroString + n4
            answer.config(text=zeroString)
            answer.pack()
        elif "5" in X:
            global n5
            zeroString = zeroString + n5
            answer.config(text=zeroString)
            answer.pack()
        elif "6" in X:
            global n6
            zeroString = zeroString + n6
            answer.config(text=zeroString)
            answer.pack()
        elif "7" in X:
            global n7
            zeroString = zeroString + n7
            answer.config(text=zeroString)
            answer.pack()
        elif "8" in X:
            global n8
            zeroString = zeroString + n8
            answer.config(text=zeroString)
            answer.pack()
        elif "9" in X:
            global n9
            zeroString = zeroString + n9
            answer.config(text=zeroString)
            answer.pack()
        elif "0" in X:
            global n0
            zeroString = zeroString + n0
            answer.config(text=zeroString)
            answer.pack()

def translateM():
    choice1.pack_forget()
    choice2.pack_forget()
    wordM.pack()
    submitM.pack()
    touchE.pack()
    touchDot.place(x=25, y = 150)
    touchDash.place(x = 215, y = 150)
    touchSpace.place(x=25, y=275)
    touchDelete.place(x = 215, y = 275)

def decodeE(ans):
    zeroString = ""
    for X in ans:
        if "O-" == X:
            zeroString = zeroString + "a"
            answer.config(text = zeroString)
            answer.pack()
        elif "-OOO" == X:
            global b
            zeroString = zeroString + "b"
            answer.config(text=zeroString)
            answer.pack()
        elif "-O-O" == X:
            global c
            zeroString = zeroString + "c"
            answer.config(text=zeroString)
            answer.pack()
        elif "-OO" == X:
            global d
            zeroString = zeroString + "d"
            answer.config(text=zeroString)
            answer.pack()
        elif "O" == X:
            global e
            zeroString = zeroString + "e"
            answer.config(text=zeroString)
            answer.pack()
        elif "OO-O" == X:
            global f
            zeroString = zeroString + "f"
            answer.config(text=zeroString)
            answer.pack()
        elif "--O" == X:
            global g
            zeroString = zeroString + "g"
            answer.config(text=zeroString)
            answer.pack()
        elif "OOOO" == X:
            global h
            zeroString = zeroString + "h"
            answer.config(text=zeroString)
            answer.pack()
        elif "OO" == X:
            global i
            zeroString = zeroString + "i"
            answer.config(text=zeroString)
            answer.pack()
        elif "O---" == X:
            global j
            zeroString = zeroString + "j"
            answer.config(text=zeroString)
            answer.pack()
        elif "-O-" == X:
            global k
            zeroString = zeroString + "k"
            answer.config(text=zeroString)
            answer.pack()
        elif "O-OO" == X:
            global l
            zeroString = zeroString + "l"
            answer.config(text=zeroString)
            answer.pack()
        elif "--" == X:
            global m
            zeroString = zeroString + "m"
            answer.config(text=zeroString)
            answer.pack()
        elif "-O" == X:
            global n
            zeroString = zeroString + "n"
            answer.config(text=zeroString)
            answer.pack()
        elif "---" == X:
            global o
            zeroString = zeroString + "o"
            answer.config(text=zeroString)
            answer.pack()
        elif "O--O" == X:
            global p
            zeroString = zeroString + "p"
            answer.config(text=zeroString)
            answer.pack()
        elif "--O-" == X:
            global q
            zeroString = zeroString + "q"
            answer.config(text=zeroString)
            answer.pack()
        elif "O-O" == X:
            global r
            zeroString = zeroString + "r"
            answer.config(text=zeroString)
            answer.pack()
        elif "OOO" == X:
            global s
            zeroString = zeroString + "s"
            answer.config(text=zeroString)
            answer.pack()
        elif "-" == X:
            global t
            zeroString = zeroString + "t"
            answer.config(text=zeroString)
            answer.pack()
        elif "OO-" == X:
            global u
            zeroString = zeroString + "u"
            answer.config(text=zeroString)
            answer.pack()
        elif "OOO-" == X:
            global v
            zeroString = zeroString + "v"
            answer.config(text=zeroString)
            answer.pack()
        elif "O--" == X:
            global w
            zeroString = zeroString + "w"
            answer.config(text=zeroString)
            answer.pack()
        elif "x-OO-" == X:
            global x
            zeroString = zeroString + "x"
            answer.config(text=zeroString)
            answer.pack()
        elif "-O--" == X:
            global y
            zeroString = zeroString + "y"
            answer.config(text=zeroString)
            answer.pack()
        elif "--OO" == X:
            global z
            zeroString = zeroString + "z"
            answer.config(text=zeroString)
            answer.pack()
        elif "/" == X:
            global space
            zeroString = zeroString + " "
            answer.config(text=zeroString)
            answer.pack()
        elif "1" == X:
            global n1
            zeroString = zeroString + "1"
            answer.config(text=zeroString)
            answer.pack()
        elif "2" == X:
            global n2
            zeroString = zeroString + "2"
            answer.config(text=zeroString)
            answer.pack()
        elif "3" == X:
            global n3
            zeroString = zeroString + "3"
            answer.config(text=zeroString)
            answer.pack()
        elif "4" == X:
            global n4
            zeroString = zeroString + "4"
            answer.config(text=zeroString)
            answer.pack()
        elif "5" == X:
            global n5
            zeroString = zeroString + "5"
            answer.config(text=zeroString)
            answer.pack()
        elif "6" == X:
            global n6
            zeroString = zeroString + "6"
            answer.config(text=zeroString)
            answer.pack()
        elif "7" == X:
            global n7
            zeroString = zeroString + "7"
            answer.config(text=zeroString)
            answer.pack()
        elif "8" == X:
            global n8
            zeroString = zeroString + "8"
            answer.config(text=zeroString)
            answer.pack()
        elif "9" == X:
            global n9
            zeroString = zeroString + "9"
            answer.config(text=zeroString)
            answer.pack()
        elif "0" == X:
            global n0
            zeroString = zeroString + "0"
            answer.config(text=zeroString)
            answer.pack()
def resultE():
    global wordM
    input = wordM.get()
    symbol_split_index = input.split(" ")
    print(symbol_split_index)
    decodeE(symbol_split_index)
def dotTouch():
    global wordM
    codeList.append('O')
    global spaceCounter
    spaceCounter = 0
    codeString = ''.join(map(str, codeList))
    symbol_split_index = codeString.split(" ")
    print(symbol_split_index)
    decodeE(symbol_split_index)

def dashTouch():
    global wordM
    global spaceCounter
    spaceCounter = 0
    codeList.append('-')
    codeString = ''.join(map(str, codeList))
    symbol_split_index = codeString.split(" ")
    print(symbol_split_index)
    decodeE(symbol_split_index)

def spaceTouch():
    global wordM
    global spaceCounter
    spaceCounter += 1
    if (spaceCounter == 1):
        codeList.append(' ')
        codeString = ''.join(map(str, codeList))
        symbol_split_index = codeString.split(" ")
        print(symbol_split_index)
        decodeE(symbol_split_index)
def deleteTouch():
    global wordM
    global spaceCounter
    spaceCounter = 0
    range = len(codeList)
    if (range >= 2):
        codeList.pop(range - 1)
        codeString = ''.join(map(str, codeList))
        symbol_split_index = codeString.split(" ")
        print(symbol_split_index)
        decodeE(symbol_split_index)
    else:
        answer.pack_forget()

window = Tk()
window.geometry('420x420')
button = Button(window, text = "Translator", command = translator)
button.pack()
choice1 = Button(window, text = 'To Morse', command = translateE)
choice2 = Button(window, text= 'To English', command = translateM)
wordE = Entry()
wordE.focus_set()
wordM = Entry()
wordM.focus_set()
submitE = Button(window, text = "Submit", command = resultM)
submitM = Button(window, text = "Submit", command = resultE)
codeList = []
touchE = Label(window, text = "OR TOUCH/CLICK THE MORSE CODE")
style = ttk.Style()
style.configure("TButton", padding=(12, 40))
touchDot = ttk.Button(window, text = "O", width = 25, command = dotTouch, style = "TButton")
touchDash = ttk.Button(window, text = "-", width = 25, command = dashTouch, style = 'TButton')
touchSpace = ttk.Button(window, text = "SPACE", width = 25, command = spaceTouch, style = "TButton")
touchDelete = ttk.Button(window, text = "BACKSPACE", width = 25, command = deleteTouch, style = "TButton")
answer = Label(window, text = "")
window.mainloop()