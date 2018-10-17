'''
Created on 2018/10/05

@author: t16cs047
'''
import random

listA = random.randrange(1,4,1)
listB = random.randrange(1,4,1)

print(listA,listB)
a = 'グー'
b = 'チョキ'
c = 'パー'

if listA==1:
    A = a
elif listA==2:
    A = b
elif listA==3:
    A = c
    
if listB==1:
    B = a
elif listB==2:
    B = b
elif listB==3:
    B = c

if listA == listB:
    C ='引き分け'
elif listA > listB:       #後で直して
    C = 'Aの勝ち'
elif listA < listB:
    C = 'Bの勝ち'

print('Aの手：'+ A +':Bの手'+ B +'->'+C)





