import random
#随机生成一个整数1-100
randomnumber = random.randint(1, 100)

a = int(input("猜一猜，请输入一个整数："))
flag = False
while flag == False:

        if a < randomnumber:
            print("哈哈哈！太小了再输入一个整数")
            a = int(input("猜一猜，请输入一个整数："))
        elif a > randomnumber:
            print("哈哈哈，太大了再输入一个整数")
            a = int(input("猜一猜，请输入一个整数："))
        else:
            print("Bingo!")
            a = int(input("good job!"))
            flag == True
            import random





