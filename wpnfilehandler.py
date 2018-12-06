wpnFile = {}


def loadWpnFile(filename):
    print('Attempting to load:', filename)
    file = open(filename, 'r')
    for line in file:
        line = line.replace(' ', '')

        if '{' in line and line[1:].isspace():
            print('Found Start')
        elif '"' in line and '[' in line:
            print('start of multi line entry')
            line = line.strip()
            line = line.replace('"', '')
            line = line.replace(',', '')
            values = line.split(':')
            tempKey = values[0]
            tempList = []
            print(values)
            if values[1].isspace():
                print('There was something immediately after the opening bracket')
                # don't want to deal with this right now so lets hope it never happens
            while ']' not in line:
                # take a look at the next line
                print('Taking a look at the next line:')
                line = next(file)
                print(line)
                # if there is something there, strip all whitespace and other junk, then append to list
                if len(line) > 0 and ']' not in line:
                    line = line.replace(' ', '')
                    line = line.replace(',', '')
                    line = line.strip()
                    tempList.append(line)
            print('Finished looking at multiple lines:')
            print(tempList)
            wpnFile[tempKey] = tempList

        elif '"' in line:
            print('Start of an entry:')
            line = line.strip()
            line = line.replace('"', '')
            line = line.replace(',', '')
            values = line.split(':')
            print(values[0])
            wpnFile[values[0]] = values[1]
        print(line)

    return wpnFile
