from Registration import *
from  project_operation  import *
print("  ________      ________      __________ ")
print(" |        |    |        |    |          |")
print(" |  Try   |    | Never  |    |  Giveup  |")
print(" |        |    |        |    |          |")
print(" |________|    |________|    |__________|")
def mainmenu():
    while True:
        print("                    Hello                    ")
        print("                Enter no 1 to register       ")
        print("                Enter no 2 to login          ")
        print("                Enter no 3 to exit           ")
        choice = input("       please enter your choice ")
        if choice=='1':
           register()
        elif choice=='2':
           login()
        elif choice=='3':
            print("             ====> Good Bye <====   ")
            exit()

mainmenu()

