import time
import datetime
def askforstring(message):
    while True:
        instr = input(message)
        if instr.isalpha():
            return  instr
        print("----Error --> please enter it again-----")


def askforInt(message):
    while True:
        intnum = input(message)
        if intnum.isdigit():
            return  int(intnum)
        print("----Error --> please enter it again-----")


def generate_id():
    # print(round(time.time()))
    return round(time.time())