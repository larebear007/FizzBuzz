# FizzBuzz
print('Ready to play FizzBuzz? \nEnter in a number! \nWhen you\'re all done, enter \'done\'.\n')

while True:
    x = input('Enter an integer: ')
    try:
        if x == 'done': break
        x = int(x)
        if x % 3 == 0 and x % 5 == 0: print('fizzbuzz')
        elif x % 3 == 0: print('fizz')
        elif x % 5 == 0: print('buzz')
        else:
            print(x)
            continue
    except:
        print('Please enter an integer or type \'done\'.')

print('\nThanks for playing FizzBuzz! Come again soon :) ')
quit()

