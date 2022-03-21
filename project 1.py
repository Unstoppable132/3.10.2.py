import random
#随机生成一个整数1-100
randomnumber = random.randint(1, 100)

a = int(input("猜一猜，请输入一个整数："))
flag = False
while flag == False:
        if a <= randomnumber:
            pass
        else:
            print("哈哈，你猜的数太大了！哈哈！请再输入一次")
        elif a < randomnumber:
        print("哈哈！你猜的数太小了！哈哈！请再输入一次")
        a = int(input())
        else:
        print("哈哈哈哈，恭喜你！！！Bingo！你总算猜对了！")
        flag = True