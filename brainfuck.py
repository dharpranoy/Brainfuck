#!/usr/bin/env python
import os
from colorama import Fore,Back
os.system("figlet Brainfuck")
print("\033[1;31mBrainfuck interpreter [>+<-]")
print(" \033[1;37mAuthor : Pranoy Dhar@2022")
print(Fore.GREEN)
class Parser:
    def __init__(self):
        self.size=30000
        self.memory=[0]*self.size
        self.ptr=0
    def evalualate(self,symbol):
        goto=[]
        i=0
        while i<len(symbol):
            if symbol[i]=='>':
                self.ptr+=1
                if self.ptr>=self.size:
                    self.ptr=0
            elif symbol[i]=='<':
                self.ptr-=1
                if self.ptr<0:
                    self.ptr=self.size-1
            elif symbol[i]=='+':
                self.memory[self.ptr]+=1
                if self.memory[self.ptr]>255:
                    self.memory[self.ptr]=0
            elif symbol[i]=='-':
                self.memory[self.ptr]-=1
                if self.memory[self.ptr]<0:
                    self.memory[self.ptr]=255
            elif symbol[i]=='^':
                print(self.memory[self.ptr],end="")
            elif symbol[i]=='.':
                print(chr(self.memory[self.ptr]),end="")
            elif symbol[i]==',':
                userin=int(input('... '))
                if userin>255:
                    userin=userin-255
                elif userin<0:
                    userin=255+userin
                self.memory[self.ptr]=userin
            elif symbol[i]=='[':
                if self.memory[self.ptr]==0:
                    if bool(goto):goto.pop()
                    while symbol[i]!=']':
                        i+=1
                else:
                    goto.append(i)
            elif symbol[i]==']':
                if self.memory[self.ptr]==0:
                    goto.pop()
                else:
                    i=goto[-1]
            i+=1
while True:
    Interpreter=Parser()
    x=input("\n>>> ")
    if x=="exit":
        exit(1)
    if x=="clear":
        os.system("clear")
    try:
        Interpreter.evalualate(x)
    except:
        print("error")
