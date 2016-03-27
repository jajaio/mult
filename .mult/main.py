#!/usr/bin/env python3
#Authors: Jackson Martin, Cole Vahey
import os
import colors as c
import time as t
import user
import load
import shutil

def run():
    option=input(c.yellow+"Would you like to scan for new messages? or send a new message? (1), (2)"+c.reset+" >>>"+c.violet)
    if option == '1':
        os.system('bash receive')
        clean=input(c.yellow+'Would you like to delete their message? (Y/N)'+c.reset+' >>>'+c.violet).strip().lower()
        if clean == 'y':
            os.system('bash cleanup')
            print(c.yellow+'Message deleted!')
        elif clean == 'n':
            print(c.yellow+'Message saved!')
        else:
            print(c.yellow+'No answer provided. Message saved.')
        input('[Press enter to continue]')
        print(c.clear)
        run()
    elif option == '2':
        prompt = input(c.yellow+"What would you like to say?"+c.reset+" >>> "+c.violet)
        os.system('date >> .talk.txt')
        os.system('echo '+user.User.name.title()+': '+prompt+' >> .talk.txt')
        os.system('bash notify')
        input('Message sent! [Press enter]')
        print(c.clear)
    else:
        print('Invalid Response')
        t.sleep(1)
        print(c.clear)
        run()

if __name__ == '__main__':
    print(c.clear)
    print(c.yellow+"Chatting!")
    load.load()
    while True:
        try:
            run()
        except(KeyboardInterrupt):
            print("Goodbye!")
            exit()
        except(EOFError):
            print("Goodbye!")
            exit()

