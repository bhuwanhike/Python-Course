import datetime

a = datetime.datetime.now().strftime("%H")

b = int(a)

if b in range(0, 12):
    print("Good Morning Sir")
    
elif b in range(12, 18):
    print("Good Afternoon Sir")

elif b in range(18, 24):
    print("Good Morning Sir")
