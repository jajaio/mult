from os import system as sys

code="echo 'Hello, world!'"

sys('echo '+code+' > test.sh')
sys('bash test.sh')
