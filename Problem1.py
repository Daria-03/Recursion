
def power(base, exp):
    if (exp == 1):
        return (base)
    if (exp != 1):
        return (base * power(base, exp - 1))
base = int(input("Введи число: "))
exp = int(input("Введи его степень: "))
print("Результат возведения в степень равен:", power(base, exp))