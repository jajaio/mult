#!/usr/bin/env python3

#Author: Jackson Martin, Cole Vahey

import user
import save
import os

def question():
    q=input('Is this the first user to be setup on the system? (y/n)').strip().lower()
    if q == 'y':
        print('Adding mult group...')
        os.system('sudo addgroup mult')
    elif q == 'n':
        pass
    else:
        print("Invalid Answer.")
        question()

def run():
    os.system('bash .rmold.sh')
    os.system('rm .rmold.sh')
    print('WARNING! You must have sudo for this setup.')
    prompt = input('What is your terminal username? >>>').strip()
    print('Saving name...')
    user.User.name = prompt
    save.save()
    print('Copying .alert file...')
    os.system('cp .alert ~')
    print('Installing mult funcs. in .bashrc....')
    os.system('bash bh')
    question()
    print('Adding permissions...')
    os.system('cd ~;sudo chown -R '+user.User.name+':mult .mult')
    print('Done!')

if __name__ == '__main__':
    run()
