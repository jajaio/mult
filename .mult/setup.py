#!/usr/bin/env python3

#Author: Jackson Martin, Cole Vahey

import user
import save
import os

def run():
    prompt = input('What is your terminal username? >>>').strip()
    print('Saving name...')
    user.User.name = prompt
    save.save()
    print('Copying .alert file...')
    os.system('cp .alert ~')
    print('Installing mult funcs. in .bashrc....')
    os.system('bash bh')
    print('Deleting the old mult directory')
    os.system('bash rmold')
    print('Done!')
if __name__ == '__main__':
    run()
