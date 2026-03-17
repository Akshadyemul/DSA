def problem1(n):
    for i in range(n):
        for j in range(n):
            print("*", end='')
        print()

def problem2(n):
    for i in range(n):
        for j in range(i + 1):
            print("*", end='')
        print()


def problem3(n):
    for i in range(n):
        count = 1
        for j in range(i + 1):
            print(count, end=' ')
            count += 1
        print()

# problem1(4)
# problem2(4)
problem3(4)