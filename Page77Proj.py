
def collatz(number):
    val = 0
    if number % 2 == 0:
        val = number // 2
    elif number % 2 == 1:
        val = 3 * number + 1
    print(val)
    return val
        

def enterInt():
    print('Please enter an integer:')
    try:
        num = int(input())
        return num
    except ValueError:
        print('An integer must be entered.')


number = enterInt()
while number and collatz(number) != 1:
    number = enterInt()
