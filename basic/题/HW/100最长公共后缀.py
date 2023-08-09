"""

"""


def main(data):
    min_length = min(map(len, data))
    target = data[0]

    count = 0
    for i in range(1, min_length + 1):
        flag = True
        for row in data[1:]:
            if target[-i] != row[-i]:
                flag = False
        if flag:
            count += 1

    print(count)
    if count > 0:
        print(target[-count:])
    else:
        print("@Zero")


# data = ["abc", "bbc", "bc"]
data = ["abc", "bbc", "c"]
# data = ["aa", "bb", "cc"]
data = ['baba', 'aba', 'cba', 'a']
data = ['aa', 'cc']

main(data)
