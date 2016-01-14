import os
import platform
import getpass

appTitle = """\
*************************************************
PwdButler  v1.0        By: Geeprox
Usage:
    add [key] [password]
    get [key]
    edit [key] [new password]
    list (To show all items)
    password (To modify the password)
    tactics [level] ('show #n' or 'show *')
    tactics edit [level] ([level] should be #n)
    quit
*************************************************
"""
system = platform.system()
if system == "Windows":
    clearCommand = "cls"
elif system == "Linux":
    clearCommand = "reset"
elif system == "Darwin":
    clearCommand = "clear"
else:
    clearCommand = "clear"


def create_ui(key_list):
    os.system(clearCommand)
    print(appTitle, end='')
    while True:
        print('PwdButler:>', end='')
        command = input()
        if command == "password":               # password
            current_password = ""
            while current_password != key_list['password']:
                current_password = getpass.getpass('Please input current password: ')
            new_password = current_password
            while new_password == current_password:
                new_password = getpass.getpass('Please input new password: ')
            key_list['password'] = new_password
            print("Reset password done!")
        elif command == "list":                 # list
            sorted_list_key = sorted(key_list.keys())
            for key in sorted_list_key:
                if key != "password":
                    print("> {0}".format(str(key)))
        elif command.startswith("add"):         # add [key] [password]
            parameters = command.split(" ")
            try:
                key_list[parameters[1]] = parameters[2]
            except IndexError:
                print("correct usage: add [key] [password]")
        elif command.startswith("get"):         # get [key]
            parameters = command.split(" ")
            try:
                print(key_list[parameters[1]])
            except IndexError:
                print("correct usage: get [key]")
            except KeyError:
                print("key:\"{0}\" not found".format(str(parameters[1])))
        elif command.startswith("edit"):        # edit [key] [new password]
            parameters = command.split(" ")
            try:
                if parameters[1] in key_list:
                    key_list[parameters[1]] = parameters[2]
                else:
                    print("key:\"{0}\" not found".format(str(parameters[1])))
            except IndexError:
                print("correct usage: add [key] [password]")
        elif command.startswith("tactics"):     # tactics #n
            print("Stay tuned...")              # tactics edit #n
        elif command == 'quit':                 # quit
            os.system(clearCommand)
            break
        else:
            os.system(clearCommand)
            print(appTitle, end='')

