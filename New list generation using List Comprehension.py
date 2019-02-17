numbers = range(10)                          #range takes 3 arguments at max i.e. 'from', 'to-1', 'step'
new_list = [n**2 for n in numbers if n%2==0] #List comprehension usage [condition, iteration, if else statement]
print(new_list)
