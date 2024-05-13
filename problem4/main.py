def find_max_sum_sub_array(k, arr):
    max_sum = sum(arr[:k])
    for i in range(1, len(arr) - k +1):
        max_sum = max(max_sum,sum(arr[i:i+k]))
    return max_sum

if __name__ == '__main__':
    print(find_max_sum_sub_array(3, [2, 1, 5, 1, 3, 2])) # 9
    print(find_max_sum_sub_array(2, [2, 3, 4, 1, 5])) # 7
    print(find_max_sum_sub_array(2, [2, 1, 4, 1, 1])) # 5
    print(find_max_sum_sub_array(3, [2, 1, 4, 1, 1])) # 7
    print(find_max_sum_sub_array(4, [2, 1, 4, 1, 1])) # 8