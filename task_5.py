def factorial(n):
    acc = 1
    for i in range(1, n + 1):
        acc *= i
    return acc

def report():
    acc = 1
    print(f"{0 : >3}! is {1 : >3} digits long")
    for i in range(1, 101):
        acc *= i
        print(f"{i : >3}! is {len(str(acc)) : >3} digits long")
