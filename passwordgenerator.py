# import random
from random import *

# create a list of numbers
num = ['1','2','3','4','5','6','7','8','9','0']
# create a list of letters of the alphabet - in lower case
lower = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
# create a list of letters of the alphebet - in upper case
# i used LIST COMPREHENSION to quickly convert the lower case letters to upper case
upper = [x.upper() for x in lower]
# create a list of symbols
symb = ['!',':','@','%','^','&','*','(',')','+','=','[',']','{','}','?','/','|']

# ask the user for the number of characters he wants the password to be
xter = int (input ("How many characters? "))
# divide the number of characters by 4 and round it up using the floor division operator
# i divided by 4 so that the password to have almost the same number of characters
xter = xter//4

# create an empty list
pass_lst = []
# use the shuffle method to shuffle the lists
shuffle(num)
shuffle(lower)
shuffle(upper)
shuffle(symb)

# create a for loop to loop through the lists the number of times as
# .... the number of characters divided by 4
# in each iteration, add the items of these lists to the new list
for i in range (xter):
    pass_lst.append (num[i-1])
for i in range (xter):
    pass_lst.append (lower[i-1])
for i in range (xter):
    pass_lst.append (upper[i-1])
for i in range (xter):
    pass_lst.append (symb[i-1])
# this should give you about the number of characters the user wants

# shuffle our password list - the one with the newly-added characters
shuffle (pass_lst)

# use join to add these items to form a string
# which is our password
password = ''.join(pass_lst)
print (password)