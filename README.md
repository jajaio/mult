# Quick Notice.
Mult is still in development. We advise that you download at another time
for a stable release.

# Mult.    
Mult is an Instant Message program written in python and bash. It
takes a bit of setup, but works fine.                                          

# Requirements.
Mult runs on Mac(OSX) and Linux. Make sure you have Python3 installed
on your system. A text editor like Vim or Nano will be needed for the install.
You also need to be on a system with multiple users for this to have any
use.

# Installing Mult.
For the sake of this
installation, you will be <strong>user1</strong> and the person you chat with will 
be called 'user2'. First, open the /etc/group file as an admin. 'vi
/etc/group'. Put 'user1' and 'user2' together. 'user1:x:1000:user2' 'user2:x:1001:user1'.
Next, go back to .mult and edit the 'bh' file 'vi bh'. Once you're 
inside, edit the part that says 'user2' to say their user name. 
Next, edit the 'receive' file to do the same thing. After that, 
vi the 'cleanup' file to change the last user2 part to the user you 
will be communicating with. Then, run the 'setup.py' file. 'python3 setup.py'. 
Once this is done, go back to your home directory. 'cd ~' and edit the '.alert' 
file so you can change the final 'user2' part. Once these steps are done for both users, you're set! 
Have both users exit and sign into their accounts and you can run mult.
Type 'mult' from the command line to access the chat.
