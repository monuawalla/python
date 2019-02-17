x = int(input('please enter an integer number to check whether it is odd or even: '))
if x%2 == 0: #checking the remainder using modulo operator, if remainder is '0' then no. must be even
    print(x, "is an even number.") #we can also use string formating print(f"{x} is an even number") used in python 3.7
else:
    print(x, "is an odd number.")
