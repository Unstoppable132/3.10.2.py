import random
#随机生成一个整数1-999
randomnumber = random.randint(1, 999)

a = int(input("print a randomnumber you like："))
flag = False
while flag == False:

       if a < randomnumber:
           print("Oh god!so small!Please print another one")
           a = int(input("print a number you like too："))
       elif a > randomnumber:
           print("Oh jesus!it's so big!Please choose another one")
           a = int(input("print a number you like again:"))
       else:
           print("It's unbelievable you choose a accurate one!God appears!")
           a = int(input("amazing luck!"))
           flag = True
