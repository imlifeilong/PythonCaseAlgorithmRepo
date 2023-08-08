def main(s, t):
    result = []
    for line in s.split():
        if line.startswith(t):
            result.append(line)

    if not result:
        print(t)
    else:
        result.sort()
        print(' '.join(result))


s = 'I love you'
t = 'He'

s = "The furthest distance in the world,Is not between life and death,But when I stand in front or you,Yet you don't know that I love you."
t = 'f'
main(s, t)
