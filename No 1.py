#Ghufron Rafif M

#No 1
import re

username = input("Masukkan username :")

cocok = re.findall(r'@\w+\d+', username)
if cocok:
    print('pass')
else:
    print('failed')

#ver 2
##username = "@rafif123_"
##
##cocok = re.findall(r'(@\w+\d+)(w)', username)
##cocok[0][0]
    
#No 2
a = """We are hiring Test/QA Engineers with 1-3 years of experience in Manual Testing(Web, Mobile & API).
If anyone((Especially who lost the job due to COVID) looking for a change, please share me the resume at
mailmesiva25@gmail.com Company:Open Financial Technologies Location: BangaloreNote: Fintech Experience
would be a higher priority"""

email =re.findall(r'[\w.-]+@[\w.-]+',a)
print(email)

#No 3
class _SimpulPohonBiner(object):
    def __init__(self, data):
        self.data = data
        self.kiri = None
        self.kanan = None

a = _SimpulPohonBiner("")
b = _SimpulPohonBiner("")
c = _SimpulPohonBiner("")
d = _SimpulPohonBiner("")
e = _SimpulPohonBiner("")
f = _SimpulPohonBiner("")
g = _SimpulPohonBiner("")
h = _SimpulPohonBiner("")
i = _SimpulPohonBiner("")
j = _SimpulPohonBiner("")
