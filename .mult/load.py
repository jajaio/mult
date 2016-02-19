import user
import json
#Author: Jackson Martin
def load():
    with open('user.json', 'r') as pfile:
        j=json.load(pfile)
        user.User.name=j['name']
if __name__=='__main__':
    load()
    print(user.User.name)
