import parser
import os

path=os.getcwd()
os.chdir(path[0:path.index("/test")]+"/e9-pair-parentheses")
f=open("sample2.py","r")
fileList=f.readlines()

for st in fileList:
    print(st)
    try:
        parser.suite(st)
    except SyntaxError as se:
        print(se.lineno)
        print(se.offset)
        print(se.msg)
        print(se.text)
        
