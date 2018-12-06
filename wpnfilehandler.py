wpnFile = {}
tempDict = {}

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
        #
        #
        # THINGS WITHIN THINGS SECTION
        # (Yes I know this is largely redundant but I want to get this fucking thing working first thank ya very much)
        #
        if '{' in line and not line[1:].isspace():
            print('oh fuck its a start of a thing within a thing within a thing')
            # grab the first thingomabobby in the line
            line = line.strip()
            line = line.replace('"', '')
            line = line.replace(',', '')
            values = line.split(':')
            tempKey = values[0]
            print('thingKey', tempKey)
            if '"' in line and '[' in line:
                print('thing within thing: start of multi line entry')
                line = line.strip()
                line = line.replace('"', '')
                line = line.replace(',', '')
                values = line.split(':')
                tempKey = values[0]
                tempList = []
                print(values)
                if values[1].isspace():
                    print('thing within thing: There was something immediately after the opening bracket')
                    # don't want to deal with this right now so lets hope it never happens
                while ']' not in line:
                    # take a look at the next line
                    print('thing within thing: Taking a look at the next line:')
                    line = next(file)
                    print(line)
                    # if there is something there, strip all whitespace and other junk, then append to list
                    if len(line) > 0 and ']' not in line:
                        line = line.replace(' ', '')
                        line = line.replace(',', '')
                        line = line.strip()
                        tempList.append(line)
                print('thing within thing: Finished looking at multiple lines:')
                print(tempList)
                tempDict[tempKey] = tempList

            elif '"' in line:
                print('thing within thing: Start of an entry:')
                line = line.strip()
                line = line.replace('"', '')
                line = line.replace(',', '')
                values = line.split(':')
                print(values[0])
                tempDict[values[0]] = values[1]
            print('THING WITHIN A THING DATA:')
            print('THING NAME:')
            print(tempKey)
            print('THING DATA:')
            print(tempDict)

            wpnFile[tempKey] = tempDict
    print(wpnFile)

    return wpnFile
