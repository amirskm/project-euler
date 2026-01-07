total = 0

for n in range(1, 1000000):
    binary = format(n, 'b')
    s = str(n)
    b = str(binary)
    x = 0
    palindromic = 'true'

    while x < len(s) - 1:
        if s[x] == s[len(s) - 1 - x]:
            x += 1
        else:
            palindromic = 'false'
            break
    # print(palindromic)
    # print(n)
    x = 0
    while x < len(b) - 1:
        if b[x] == b[len(b) - 1 - x]:
            x += 1
        else:
            palindromic = 'false'
            break
    # print(palindromic)
    # print(b)

    if palindromic == 'true':
        total += n
        print('base 10', n)
        print('binary', b)

print(total)
