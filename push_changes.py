import os
from os import path

os.system('git status')

while True:
	fname='git add '+input('Enter filename to add : ')
	if path.exists(fname) == False:
		break
	else:
		print('Enter valid filename!!!')
	
os.system(fname)
cmsg='git commit -m '+input('Enter commit message: ')
os.system(cmsg)
os.system('git push -u origin master')

print('Pushed Changes! Make a Pull request!')
