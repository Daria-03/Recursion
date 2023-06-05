a = int(input('Введи первое число '))
b = int(input('Введи второе число '))
 
 
def sum(a, b):
    if b == 0:
        return a
    return sum(a+1, b-1)
 
 
print(sum(a, b))