import os, time

while True:
    os.system('clear')
    print('### DATA VALIDATION ###\n')
    name = input('Your name: ')
    if len(name) > 3:
        age = int(input('Your age: '))
        if age >= 0 and age <= 150:
            wage = float(input('Your wage: '))
            if wage > 0.0:
                sex = input('Your sex: ')
                if sex == "f" or sex == "m":
                    m_status = input('Your matrial status: ')
                    if m_status == "s" or m_status == "c" or m_status == "v" or m_status == "d":
                        print('You passed all requirements!!!')
                        break
                    else:
                        print('Matrial status invalid')
                        time.sleep(2)
                else:
                    print('Sex invalid')
                    time.sleep(2)
            else:
                print('Wage invalid')
                time.sleep(2)
        else:
            print('Age invalid')
            time.sleep(2)
    else:
        print('Name invalid')
        time.sleep(2)