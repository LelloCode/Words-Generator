
import string
import random
from datetime import datetime
lunghezzaminimaparola= 1
filename=raw_input("Save to file name? ")
pathname=raw_input("Insert path to save? ")
numeroparole=raw_input("How many password do you want to generate? ")
# start-there i manage the min lenght
lunghezzaminimaparola=raw_input("Whats the min lenght of the string? ")
if (int(lunghezzaminimaparola)<=1)or(int(lunghezzaminimaparola)>=50):
   while (int(lunghezzaminimaparola)<1)or(int(lunghezzaminimaparola)>50):
      lunghezzaminimaparola=raw_input("the string must be between 1 and  50, insert the correct min lenght: ")
# end-there i manage the min lenght
# start-there i manage the max lenght
lunghezzamaxparola=raw_input("Whats the max lenght of the string? ")
if (int(lunghezzamaxparola)<=1)or(int(lunghezzamaxparola)>=100):
   while (int(lunghezzamaxparola)<1)or(int(lunghezzamaxparola)>100):
      lunghezzamaxparola=raw_input("the string must be between 1 and  100, insert the correct min lenght: ")
# end-there i manage the max lenght
scelta=raw_input("do you want to select the special characters? (y/n) ")
carattereascii=raw_input("the string must contain ascii characters? (y/n) ")
caratterenumero=raw_input("the string must be contain numbers? (y/n) ")
if scelta=='y':
   simboliscelti=raw_input("digit the special characters that you choise ")
else:
   caratteresimbolo=raw_input("the string must be contain symbols? (y/n)  ")

caratteriscelti=''

if carattereascii=='y':
   caratteriscelti=caratteriscelti+string.ascii_letters
if caratterenumero=='y':
   caratteriscelti=caratteriscelti+string.digits
if scelta=='y':
   caratteriscelti=caratteriscelti+simboliscelti
elif caratteresimbolo=='y':
   caratteriscelti=caratteriscelti+string.punctuation

file_uno = open(pathname + filename, "w")
for x in range(int(numeroparole)):
   parola=''.join(random.choice(caratteriscelti) for _ in range(random.randint(int(lunghezzaminimaparola),int(lunghezzamaxparola))))
   file_uno.write("\n"+ "Password " + str(x) + ": " + parola)
file_uno.close()
print("Completed")



