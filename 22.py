alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' 
score = 0
name_score = 0
total_score = 0

with open("Names Scores Problem 22.txt", "r") as f:
    names = f.read()

names = names.replace('"', '').split(',')
names.sort()


#print(names.split('","')[0])

#print(len(names.split('","')))

for i in range(0, len(names)): 
    print(names[i])
    for n in range(0, len(names[i])):
        print(names[i][n])
        print(alphabet.find(names[i][n]) + 1)
        name_score += alphabet.find(names[i][n]) + 1
    overall_score = name_score * (i + 1) 
    print('position', i + 1)
    print('name_score', name_score)
    print('overall_score', overall_score)
    total_score += overall_score
    name_score = 0
print('total_score', total_score)