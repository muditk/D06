import random

f = open('magicnumbers.txt', 'w')
i = 0
while i < 11:
    f.write(str(random.randint(0, 9000)) + "\n")
    i = i + 1
f.close()
