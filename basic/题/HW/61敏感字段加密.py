def main(s, k):
    cmd = []
    #
    # print(tmp)
    index = 0
    tmp = []
    while index < len(s):
        if s[index] == '"':
            start = index + 1
            end = start + s[index + 1:].find('"')
            cmd.append(f'"{s[start:end]}"')
            index = end

        elif s[index] == '_':
            cmd.append(''.join(tmp))
            tmp = []
        else:
            tmp += s[index]

        index += 1

    if len(tmp) > 0:
        cmd.append(''.join(tmp))

    res = [c for c in cmd if c]
    if k > len(res) - 1:
        print('ERROR')
    else:
        if '"' in res[k]:
            res[k] = '"******"'
        else:
            res[k] = '******'

        print('_'.join(res))


k = 1
s = 'password__a12345678_timeout_100'

# k = 2
# s = 'aaa_password_"a12_45678"_timeout__100_""_'
main(s, k)
