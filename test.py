import os



print('The current working directory is')
os.system('pwd')
#clone, set up origin, upstream, make changes, push to local origin, finally pull request
#init and clone

os.system('git init')
url=input('Enter url of forked repo if not configured, else press enter: ')
clone='git clone '+url
os.system(clone)

#set remote origin, your local copy
orgadd='git remote add origin '+url
os.system(orgadd)
os.system('git remote -v')
print("======================================================================================================================\n")

#set upstream
upstadd='git remote add upstream '+ input('Enter url to the original repo if not configured, else press enter:: ')
os.system(upstadd)
os.system('git remote -v')
print("======================================================================================================================\n")

#branch and make changes
branch_name=input('Enter branch-name')
branch='git checkout -b '+branch_name
os.system(branch)
print('Time to make some changes!')
