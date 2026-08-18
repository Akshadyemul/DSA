'''
https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem?isFullScreen=true
'''

if __name__ == '__main__':
    # n = int(input())
    arr = list(map(int, input().split()))

    # Solution
    # arr.sort()
    # print(arr[-2])

    largest = arr[0]
    for num in arr:
        if num > largest:
            largest = num

    print(largest)

    second_smallest = None
    for num in arr:
        if num < largest:
            if second_smallest == None:
                second_smallest = num
            elif num > second_smallest:
                second_smallest = num

    print(second_smallest)