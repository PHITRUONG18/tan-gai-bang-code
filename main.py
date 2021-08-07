import time;

#lam mau
passw = input("Nhập Huy Trinh: ");
while passw!="Huy Trinh":
    passw = input("Vui lòng nhập Huy Trinh: ")
print(passw)

#fake loading
for i in range(0,100,10):
    print("Loading " + str(i+10) +"%")
    time.sleep(0.4)
print("Done")

#in anh
f = open("huytrinh.txt", "r")
lines = f.readlines()

for line in lines:
    print("{}".format(line.strip()))
    time.sleep(0.3)


