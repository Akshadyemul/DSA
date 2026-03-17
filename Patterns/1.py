# Square Pattern
def problem1(n):
    for i in range(n):
        for j in range(n):
            print("*", end='')
        print()


# Right Triangle Pattern
def problem2(n):
    for i in range(n):
        for j in range(i + 1):
            print("*", end='')
        print()


# Increasing Number Triangle
def problem3(n):
    for i in range(n):
        count = 1
        for j in range(i + 1):
            print(count, end=' ')
            count += 1
        print()


# Same Number Triangle
def problem4(n):
    for i in range(n):
        for j in range(i):
            print(i, end='')
        print()


# Inverted Right Triangle
def problem5(n):
    for i in range(n):
        for j in range(n-i):
            print("*", end=' ')
        print()



# Inverted Right Triangle
def problem6(n):
    for i in range(n):
        for j in range(n-i):
            print(j, end=' ')
        print()


# Inverted Number Triangle
def problem7(n):
    for i in range(n):
        for j in range(n-i-1):
            print(" ", end="")

        for j in range(2*i+1):
            print("*", end="")

        for j in range(n-i-1):
            print(" ", end="")
        print()

# Inverted Centered Pyramid
def problem8(n):
    for i in range(n):
        for j in range(i):
            print(" ", end='')
        for j in range(2*n-(2*i+1)):
            print("*", end='')
        for j in range(i):
            print(" ", end='')
        print()


# Diamond Pattern
def problem9(n):
    for i in range(n):
        for j in range(n-i-1):
            print(" ", end='')
        for j in range(2*i+1):
            print("*", end='')
        for j in range(n-i-1):
            print(" ", end='')
        print()

    for i in range(1, n):
        for j in range(i):
            print(" ", end='')
        for j in range(2*(n-i)-1):
            print("*", end='')
        for j in range(i):
            print(" ", end='')
        print()

# Symmetric Star Pattern
def problem10(n):
    for i in range(1, 2*n):
        stars = i
        if i > n:
            stars = 2 * n - i
        for j in range(stars):
            print("*", end='')
        print()


# Binary Alternating Triangle
def problem11(n):
    start = 1
    for i in range(n):
        if i % 2 == 0:
            start = 1
        else:
            start = 0

        for j in range(i + 1):
            print(start, end='')
            start = 1 - start
        print()


# Mirrored Number Pattern
def problem12(n):
    space = 2 * (n - 1)
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end='')
        for j in range(space):
            print(" ", end='')
        for j in range(i, 0, -1):
            print(j, end='')
        print()
        space -= 2


# problem1(4)
# problem2(4)
# problem3(4)
# problem4(4)
# problem5(5)
# problem6(4)
# problem7(5)
# problem8(5)
# problem9(5)
# problem10(5)
# problem11(5)
problem12(5)