import os

print('The current working directory is')

os.system('pwd')
#clone, set up origin, upstream, make changes, push to local origin, finally pull request

#init and clone
os.system('git init')
url=input('Enter url of forked repo: ')
clone='git clone '+url
os.system(clone)

#set remote origin, your local copy
orgadd='git remote add origin '+url
os.system(orgadd)
os.system('git remote -v')

#set upstream
upstadd='git remote add upstream '+ input('Enter url to the original repo: ')
os.system(upstadd)
os.system('git remote -v')

print('Time to make some changes!')

#os.system('git remote add origin https://github.com/'+usname+'/'+repo+'.git')