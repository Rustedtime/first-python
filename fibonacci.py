n = input("How many numbers? ")
x = 0
y = 1
i = 0
while i < int(n):
    print(str(y) + '\n')
    z = y
    y += x
    x = z
    i += 1