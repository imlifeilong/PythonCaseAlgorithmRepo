import random

def partaion(data, left, right):
    less = left - 1
    more = right

    while left < more:
        if data[left] < data[right]:
            less += 1
            data[left], data[less] = data[less], data[left]
            left += 1
        elif data[left] > data[right]:
            more -= 1
            data[left], data[more] = data[more], data[left]
        else:
            left += 1
    data[more], data[right] = data[right], data[more]

    return less, more+1

def sort(data, left, right):
    if not data or left > right:
        return
    index = random.randint(left, right)
    data[right], data[index] = data[right], data[index]
    mid = partaion(data, left, right)
    sort(data, left, mid[0])
    sort(data, mid[1], right)
    
    return data


if __name__ == '__main__':
    a = [5, 3, 4, 2, 6, 1, 1, 7, 8, 5, 9, 5, 5, 6, 5]
    # a = [3, 4, 2, 1]
    print(sort(a, 0, len(a)-1))