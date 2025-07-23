monster = 100
weapon1 = 60
weapon2 = 20
weapon3 = 30

gamestart = True
 
while gamestart:
    print("Welcome to คิริตู่ program")
    print("----Chose what you want to do----")
    print("Chose option [1]: Fight!")
    print("CHose option [2]: Hellnah run")
    option = int(input("Your choise is: "))
    if (option == 1):
        attack_times = int(input("How many time do you want to attack monster: "))
        for i in range(attack_times):
            print("------You have Three weapon please choose to attack----")
            print("Choose weapon [1] damage is:",weapon1)
            print("Choose weapon [2] damage is:",weapon2)
            print("Choose weapon [3] damage is:",weapon3)
            print("Monster health: ",monster)
            print("เหลือโอกาศตีอยู่:",attack_times - i)
            weapon = int(input("You weapon this round is: "))
            print("You chose weapon",weapon)
            if (weapon == 1):
                monster -= weapon1
                if (monster < 0):
                    print("!!!!You ตีแรงเกินอ่ะมันเลยฮีลมาเป็น 20")
                    monster = 20
            elif (weapon == 2):
                monster -= weapon2
                if (monster < 0):
                    print("!!!!You ตีแรงเกินอ่ะมันเลยฮีลมาเป็น 20")
                    monster = 20
            elif (weapon == 3):
                monster -= weapon3
                if (monster < 0):
                    print("!!!!You ตีแรงเกินอ่ะมันเลยฮีลมาเป็น 20")
                    monster = 20
            elif (monster == 0):
                print("Monster แตกแล้ว")
                break
        if (monster > 0):
            print("หมดโอกาศแล้วจ่ะน้องรัก")
            print("mon ไม่แตก แต่คนเล่นแตกเอง")
            gamestart = False
        else:
            print("You เก่งมาก ชนะได้แล้วเย่ๆ คิริตู่พุมจัย")
            gamestart = False
    else:
        print("ไปละบาย")
        break
 
 