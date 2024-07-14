import os
os.system('clear')

A = 80000.0
B = 200000.0
count = 0
while A < B:
    A = A + A * 3 / 100
    B = B + B * 1.5 / 100
    count += 1
else:
    print(count)