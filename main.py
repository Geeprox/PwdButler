import getpass
import os

from pyDes import *
from transcoding import *
from transform import *
from mainUI import *


pathOfKeyFile = './PwdButlerData/'
nameOfKeyFile = 'pwdButler.dat'

listOfKey = {}


def save():
    saving_data = "password:" + listOfKey["password"] + ";"

    for saving_key, saving_value in listOfKey.items():
        if saving_key != "password":
            saving_data += "{0}:{1};".format(str(saving_key), str(saving_value))

    saving_binary_data = string2binary(saving_data)
    saving_key_file = open(pathOfKeyFile + nameOfKeyFile, "wb")
    saving_key_file.write(pyDesObj.encrypt(saving_binary_data))
    saving_key_file.close()


# At first, check if the storage file exists
if not os.path.isfile(pathOfKeyFile + nameOfKeyFile):
    password = getpass.getpass('Please input a password to sign up: ')
    passwordAgain = getpass.getpass('Please type it again: ')

    while password != passwordAgain:
        password = getpass.getpass('Please input the password again: ')
        passwordAgain = getpass.getpass('Please type it again: ')

    listOfKey['password'] = password
    if not os.path.exists(pathOfKeyFile):
        os.mkdir(pathOfKeyFile)
    keyFile = open(pathOfKeyFile + nameOfKeyFile, "wb+")
    pyDesObj = triple_des(string2binary(transform_key(password)), CBC, b"\0\6\1\0\0\5\1\7", pad=None, padmode=PAD_PKCS5)
    keyFile.write(pyDesObj.encrypt(string2binary('password:' + password + ';')))
    keyFile.close()

    create_ui(listOfKey)
    save()
else:
    incorrectCount = 0
    while incorrectCount < 3:
        passwordInput = getpass.getpass('Please input the password: ')
        keyFile = open(pathOfKeyFile + nameOfKeyFile, 'rb')
        pyDesObj = triple_des(string2binary(transform_key(passwordInput)), CBC, b"\0\6\1\0\0\5\1\7", pad=None, padmode=PAD_PKCS5)
        binaryData = pyDesObj.decrypt(keyFile.read())
        data = binary2string(binaryData)

        for line in data.split(";"):
            try:
                tmpData = line.split(":")
                key, value = tmpData[0], tmpData[1]
                listOfKey[key] = value
            except IndexError:
                pass

        keyFile.close()

        try:
            if listOfKey['password'] == passwordInput:
                create_ui(listOfKey)
                save()
                incorrectCount = 4
        except KeyError:
            incorrectCount += 1
            print("Incorrect password({0}/{1})".format(str(incorrectCount), str(3)))

            if incorrectCount == 3:
                print("Exit")