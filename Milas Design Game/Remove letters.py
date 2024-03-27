with open('Easylevel.py', 'r') as f:
    linelist = f.readlines()

with open('Easylevel.py', 'w') as f2:
    for line in linelist:
        words = line.split()
        words = [word for word in words if len(word) > 3]
        line = ' '.join(words) + '\n'
        f2.write(line)












