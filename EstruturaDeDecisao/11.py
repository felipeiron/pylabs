import os
os.system('cls')

print('##### AJUSTE DE SALÁRIO #####\n')

salario = float(input('Digite seu salário atual: '))

if salario <= 280.00:
    print('\n- Salário atual: {}\n- Percentual de aumento: 20%\n- Aumento: {}\n- Novo Salário: {}\n'.format(salario, salario * 0.2, salario + (salario * 0.2)))
elif salario > 280.00 and salario <= 700.000:
    print('\n- Salário atual: {}\n- Percentual de aumento: 15%\n- Aumento: {}\n- Novo Salário: {}\n'.format(salario, salario * 0.15, salario + (salario * 0.15)))
elif salario > 700.00 and salario <= 1500.00:
    print('\n- Salário atual: {}\n- Percentual de aumento: 10%\n- Aumento: {}\n- Novo Salário: {}\n'.format(salario, salario * 0.1, salario + (salario * 0.1)))
else:
    print('\n- Salário atual: {}\n- Percentual de aumento: 5%\n- Aumento: {}\n- Novo Salário: {}\n'.format(salario, salario * 0.2, salario + (salario * 0.05)))