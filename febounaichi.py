num = int (input("Enter the Number :"))

x =0 
y = 1

for i in range(0,num):
    z = x + y
    print(x)
    x =y
    y = z
