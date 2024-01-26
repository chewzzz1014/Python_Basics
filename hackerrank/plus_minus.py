def plusMinus(arr):
    # Write your code here
    positive_ele = list(filter(lambda x:x>0, arr))
    negative_ele = list(filter(lambda x:x<0, arr))
    print(f'{len(positive_ele)/len(arr):.6f}\n{len(negative_ele)/len(arr):.6f}\n{(len(arr)-len(negative_ele)-len(positive_ele))/len(arr):.6f}')
