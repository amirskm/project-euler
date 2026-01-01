# n = 13
steps = 0
max_steps = 0

for n in range(100, 1000000):
  #  print('start', n)
    start = n
  #  print('---')
    while True:
        if n == 1:
          #  print('done', n)
          #  print('steps', steps)
            if steps > max_steps:
                max_steps = steps
                max_number = start
            steps = 0
         #   print('---')
            break
        elif n % 2 == 0:
            n = n/2
            steps += 1
          #  print('even', n)
        else:
            n = 3*n + 1
           # print('odd', n)
            steps += 1

print('max_number', max_number)
print('max_steps', max_steps)

