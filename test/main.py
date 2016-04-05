from os import system as sys
#Author: Jackson Martin
code="echo 'Hello, world!'"

sys('echo '+code+' > test.sh')
sys('bash test.sh')
