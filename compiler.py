import os
import sys

import colorama

##  Location return True if location exist

def find_loc(loc):
    try:
        simple = os.listdir(loc)
        return True;
    except:
        return False;


##  .py files locater
##  return the py file as well ofc
##  no way to optimize more than this
##  I didn't handle one error cuz if the user is so fucking stupid
##  that would be his own problem

def return_all_py(loc):
    py_files = []
    files = os.listdir(loc)
    for file in files:
        if ".py" in file:
            py_files.append(file)
    if len(py_files) == 0:
##  I don't raise exception and I like using colors
        print("  {0}ConsoleERROR{1} ~ No python files detected".format(colorama.Fore.RED,colorama.Fore.RESET))
    elif len(py_files) == 1:
        return py_files[0];
    else:
        print("  ConsoleByHCn1(Output) Please choose one of the following: \n[NUMBERS ONLY]\n")
        for py in range(len(py_files)):
            print(str(py)," - ",py_files[py])
        py_ = py_files[int(input())]
        return py_;


#   last of all is returning icons
#   if icons doesn't exist it return False
#   it will take first icon only
def return_all_icon(loc):
    icon = False
    for file in os.listdir(loc):
        if ".ico" in file:
            icon = file
            break;
    return  icon;

#   this needed a lot of handling | NOT BEAUTIFUL
def import_files():
    try:
        import colorama
    except:
        if "win" in sys.platform:
            os.system("pip install colorama")
            try:
                import colorama
            except:
                print("  ConsoleByHCn1(Output) ~ Please Configure Pip on your Desktop [OR INSTALL COLORAMA and PYINSTALLER]")
                sys.exit()
        else:
            os.system("sudo pip3 install colorama")
            try: import colorama
            except:
                print("  ConsoleByHCn1(Output) ~ Please Configure Pip on your Desktop [OR INSTALL COLORAMA and PYINSTALLER]")
                sys.exit()

    try:
        if "win" in sys.platform:
            os.system("pip install pyinstaller")
        else:
            os.system("sudo pip3 install pyinstaller")
    except Exception as e:
        print(e)


#Converting is the easiest part
#I used cd loc cuz i was tired finding another solution
def converting(python,icon,loc):
    print("  ConsoleByHCn1 ~ Does it have GUI? (y/n)",end=" ")
    gui = (input()=="y")
    print(python,icon,loc)
    if icon is False:
        if gui is True:
            os.system("cd '{1}' && pyinstaller --windowed --noconsole {0}".format(python,loc))
        else:
            os.system("cd '{1}' && pyinstaller {0}".format(python,loc))
    else:
        if gui is True:
            os.system("cd '{1}' && pyinstaller --windowed --noconsole --icon {2} {0}".format(python,loc,icon))
        else:
            os.system("cd '{1}' && pyinstaller --icon {2} {0}".format(python, loc, icon))
    print("See you")
#   Main. Comment to make it look a cool part
#   While it is not of course
#   Useless tool ~_~
if __name__=="__main__":
    print("  ConsoleByHCn1(Output) ~ Checking needs")
    import_files()
    location = False
    while location is False:
        print("  ConsoleByHCn1(Output)Please upload path ~ {0}".format(colorama.Fore.YELLOW),end="")
        loc = input()
        print(colorama.Fore.RESET)
        location = find_loc(loc)
    icon = return_all_icon(loc)
    python = return_all_py(loc)
    converting(python,icon,loc)
