start = True
while start:
    print("เลือกข้อที่ต้องการเล่น")
    print("ข้อที่ [1] โจทย์แรก")
    print("ข้อที่ [2] โจทย์สอง")
    x = int(input("กรุณากรอกเลข: "))
    if (x == 1):
        print("ทำโจทย์ที่ 1")
    elif (x == 2):
        print("ทำโจทย์ที่ 2")
    start = False
