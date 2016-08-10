with open('roster.txt', 'r') as fin:
    lines = fin.readlines()
    count = 0
    for line in lines:
        name = line.split()[0]
        if 'e' in name:
            count += 1
            print(name)
            with open('rosterresults.txt', 'a') as fresults:
                fresults.write(name + "\n")
                print("good")
