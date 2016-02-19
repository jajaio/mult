import user
import json
#Author: Jackson Martin

def save():
	with open('user.json', 'w') as pfile:
		pfile.write(json.dumps({
            "name":user.User.name
            }))
        
if __name__=='__main__':
    save()
