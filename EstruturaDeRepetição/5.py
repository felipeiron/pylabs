import os, time

while True:
    os.system('clear')
    pop_a = int(input('How many people are there in A now? '))
    if pop_a > 0:
        g_rateA = float(input('What is the A growth rate? '))
        if g_rateA > 0:
            pop_b = int(input('How many people are there in B now? '))
            if pop_b > 0:
                g_rateB = float(input('What is the B growth rate? '))
                if g_rateB > 0:
                    count = 0
                    while pop_a <= pop_b:
                        pop_a = pop_a + pop_a * g_rateA / 100
                        pop_b = pop_b + pop_b * g_rateB / 100
                        count += 1
                    else:
                        print('\n"A" population will surpass "B" in',count,'years.')
                        ask = input('\nDo you want to repeat? s/n ')
                        if ask == 's':
                            print('Ok! The program you start in some seconds.')
                            time.sleep(5)
                        else:
                            break    
                else:
                    print('Input invalid!')
                    time.sleep(2)
            else:
                print('Input invalid!')
                time.sleep(2)
        else:
            print('Input invalid!')
            time.sleep(2)
    else:
        print('Input invalid!')
        time.sleep(2)