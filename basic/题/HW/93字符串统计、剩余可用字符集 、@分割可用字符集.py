"""
a:3,b:5,c:2@a:1,b:2

a:2,b:3,c:2


"""


def _split(s):
    result = {}
    for x in s.split(','):
        k, v = x.split(':')
        result[k] = int(v)
    return result


def main(data):
    _totle, _used = data.split('@')
    totle = _split(_totle)
    used = _split(_used)

    result = []
    for k, v in totle.items():
        if k in used:
            totle[k] = v - used[k]
        result.append(f'{k}:{totle[k]}')
    print(','.join(result))


s = 'a:3,b:5,c:2@a:1,b:2'
main(s)
