username = input("Username: ")
password = input("Password: ")

if username == "admin":
    if password == "admin123":
        print("You're admin")
    else:
        print("wrong")
elif username == "user":
    if password == "user123":
        print("You're user")
    else:
        print("wrong")
else:
    print("Not found")





x = "ตะแน่ว"

x += "เดอะมอลบางกะปิิ"

print(x)