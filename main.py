import random

randomniy = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
parolL = int(input("длина вашего пароля:"))
rebsda = ""
for i in range (parolL):
    rebsda +=random.choice(randomniy)
    
print(rebsda)
