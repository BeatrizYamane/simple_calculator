""""" Calculadora com while """

while True:
    number_1 = input('Enter a number: ')
    number_2 = input('Enter a secord number: ')
    operator = input('Choice a operator(+-/*): ')

    valid_numbers = None # flag
    num_1_float = 0
    num_2_float = 0

    try:
       num_1_float = float(number_1)
       num_2_float = float(number_2)
       valid_numbers = True
    except Exception: # Aqui mesmo que o usuraio digite um valor invalido, o codigo ainda vai continaur rodando, passanndo assim para o (if)
       valid_numbers = None

    if valid_numbers is None:
        print('One or both of entered numbers are invalid ')
        continue

    valid_operator = '+-/*'
    
    if operator not in valid_operator:
        print('Invalid operator') 
        continue

    if len(operator) > 1:
        print('Enter just one operator')
        continue

    print('See the result below')

    if operator == '+':
       result = num_1_float + num_2_float
       print(result)
    elif operator == '-':
        print(num_1_float - num_2_float)
    elif operator == '*':
        print(num_1_float * num_2_float)
    elif operator == '/':
        print(num_1_float / num_2_float)
    else:
        print('It should never get here')
         
    end = input('Dou you want to finish? [y]es: ').lower().startswith('y') 

    if end is True:
        break

    




