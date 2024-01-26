def findZigZagSequence(a, n):
    a.sort()
    mid = n//2
    a[mid], a[n-1] = a[n-1], a[mid]

    st = mid + 1
    ed = n - 1
    while (a[st] <= a[ed]):
        a[st], a[ed] = a[ed], a[st]
        st = st + 1
        ed = ed - 1
        print(f'111111: {a}')

    for i in range (n):
        if i == n-1:
            print(a[i])
        else:
            print(a[i], end = ' ')
    return


test_cases = int(input('Enter # of test cases: '))
for cs in range (test_cases):
    n = int(input('Number of elements: '))
    a = list(map(int, input("Sequence: ").split()))
    findZigZagSequence(a, n)



