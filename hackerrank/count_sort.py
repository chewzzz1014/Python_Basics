def countingSort(arr):
    count_arr = [0] * 100
    result = []
    for x in arr:
        count_arr[x] += 1
    for ele, count in enumerate(count_arr):
        for n in range(count):
            result.append(ele)
    return result


def countSort(arr):
    mid = len(arr) // 2
    count_arr = [[] for _ in range(mid + 1)]

    for idx, x in enumerate(arr):
        if idx >= mid:
            count_arr[int(x[0])].append(x[1])
        else:
            count_arr[int(x[0])].append('-')
    print(' '.join([' '.join(x) for x in count_arr]).strip())


if __name__ == '__main__':
    n = int(input('n: ').strip())
    arr = []
    for _ in range(n):
        arr.append(input('input: ').rstrip().split())
    countSort(arr)


# if __name__ == '__main__':
#     n = int(input('n: ').strip())
#     arr = list(map(int, input('list of numbers: ').rstrip().split()))
#     result = countingSort(arr)
#     print(' '.join(map(str, result)))