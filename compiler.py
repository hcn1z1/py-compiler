#!/bin/python3.9

import os
import sys
import shutil

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

        print("  {0}ConsoleERROR{1} ~ No python files detected".format(colorama.Fore.RED,colorama.Fore.RESET))
    elif len(py_files) == 1:
        return py_files[0];
    else:
        print("  ConsoleByHCn1(Output) Please choose one of the following: \n[NUMBERS ONLY]\n")
        for py in range(len(py_files)):
            print(str(py)," - ",py_files[py])
        py_ = py_files[int(input())]
        return py_;
##  I don't raise exception and I like using colors



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
    return  colorama;

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


#   After converting i was like
#   Q: Hi Z1, Why don't you make a copy func that copy all files and folder to dist ?
#   A: Mmm, Tired? 1:34 A.M ! People studying and me making a useless script.

def copy_all_files_to_dist(loc,python):
    loc += "/" #   if you waiting an explaination I am not going to do that
    if "win" not in sys.platform:loc = os.path.dirname(loc)+"/"; not_explaining = "/"
    else: loc = os.path.dirname(loc)+"\\"; not_explaining ="\\"
    for file in os.listdir(loc):
        if file == python or file =="dist" or file == "build":pass
        else:
            try: shutil.copytree(loc+file,loc+"dist"+not_explaining+file)
            except NotADirectoryError:print(file);shutil.copy(loc+file,loc+"dist"+not_explaining+file)\


#   Main. Comment to make it look a cool part
#   While it is not of course
#   Useless tool ~_~

if __name__=="__main__":
    print("  ConsoleByHCn1(Output) ~ Checking needs")
    colorama = import_files()
    location = False
    while location is False:
        print("  ConsoleByHCn1(Output)Please upload path ~ {0}".format(colorama.Fore.YELLOW),end="")
        loc = input()
        print(colorama.Fore.RESET)
        location = find_loc(loc)
    icon = return_all_icon(loc)
    python = return_all_py(loc)
    converting(python,icon,loc)
    copy_all_files_to_dist(loc,python)


#   in function copy_all_file_to_dist
#   i honestly wasn't going to explain but i was afraid that someone would say that it was very complicated.

#   well, no ! their is no way python can copy a folder to another. that's not how it works.
#   os.path.dirname returns location without any path's slash at the end that's why i added that.

#   something else about this function. if the folder is a  seperated name, it will return the procedding
#   path. using a slash at the end will help python detecting it hopefully. still i see that python 3 has a
#   bug when it comes to adding this slashes to pathes especially on double back slach. like wth x ="\\" is \\ not \ :(

#   _list_ = os.listdir(loc).remove(python) apparently this doesn't work anymore on python 3.9 or maybe linux i dunno
