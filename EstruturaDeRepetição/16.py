import os, time
os.system('clear')

print('### FIBONACCI UNTIL +500 ###\n')

fibo = [0,1]
i = 2
while fibo[-1] < 500:
    fibo.append(fibo[i-1]+fibo[i-2])
    i += 1
else:
    print(fibo)
