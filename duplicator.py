from pywinauto import application
import os
import random
import time

app = None

def main():

    app = application.Application()
    app.start('SharpTona.exe')

    f = open("history.txt", 'r')

    line = f.readline()
    while line != '':
        if line.startswith("Ask: "):
            app.sharpTona['Question:Edit'].SetText(line[5:-1])
            app.sharpTona['Ask'].Click()
        elif line.startswith("Correct: ") and app.sharpTona['Correct'].IsEnabled():
            app.sharpTona['Answer:Edit'].SetText(line[9:-1])
            app.sharpTona['Correct'].Click()
        elif line.startswith("Teach: ") and app.sharpTona['Teach'].IsEnabled():
            app.sharpTona['Answer:Edit'].SetText(line[7:-1])
            app.sharpTona['Teach'].Click()

        line = f.readline()

    ret_val = app.sharpTona['Answer:Edit'].Texts()[0] == "You found bug 4"
    
    app.sharpTona.Close()

    return ret_val


yes_bug = 0
no_bug = 0

for i in range (100):
    if main():
        yes_bug += 1
    else:
        no_bug += 1

print yes_bug / (yes_bug + no_bug)
