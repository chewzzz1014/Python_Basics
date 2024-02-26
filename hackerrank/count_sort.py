def countingSort(arr):
    count_arr = [0] * 100
    result = []
    for x in arr:
        count_arr[x] += 1
    for ele, count in enumerate(count_arr):
        for n in range(count):
            result.append(ele)
    return result


if __name__ == '__main__':
    n = int(input('n: ').strip())

    arr = list(map(int, input('list of numbers: ').rstrip().split()))

    result = countingSort(arr)

    print(' '.join(map(str, result)))