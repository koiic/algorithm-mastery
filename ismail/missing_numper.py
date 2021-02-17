def missing_number(array:[int]) -> int:
    
    new_list = []
    if len(array) == 1 and array[0] > 1:
        return 1

    if 1 not in array:
        return 1
    for num in array:
        if num < 0:
            del num
        elif num + 1 not in array:
            new_list.append(num + 1)

    return min(new_list)

if __name__ == '__main__':
    missing_number([3,4,-1,1])
    