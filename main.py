# import the library
from appJar import gui

acceptableWeaponKeys = ['id', 'animationType', 'barrelMode', 'displayArcRadius', 'fireSoundTwo',
                        'hardpointAngleOffsets', 'hardpointOffsets', 'hardpointSprite', 'hardpointGunSprite']
loadedData = {}

def loadfile(button):
    filename = app.getEntry("f1")
    # print(filename)
    parsewpn(filename)


# todo: Rewrite this again, so it will load properly
# Needs to be able to handle those godawful nested bits { [ etc
def parsewpn(filename):
    with open(filename) as f:
        currentFile = f.read().splitlines()
    currentFile = str(currentFile)
    # print(currentFile)
    currentFile = currentFile.replace("{", " ")
    currentFile = currentFile.replace("}", " ")
    currentFile = currentFile.replace("'", "")
    currentFile = currentFile.replace('"', "")
    currentFile = currentFile.replace(" ", "")
    currentFile = currentFile.replace(",,", ",")

    # print(currentFile)

    cleanFile = currentFile.split(',')
    # Old school iteration, might need it to hack together stuff
    i = 0
    while i < len(cleanFile) - 1:
        i += 1
        # laziness
        each = cleanFile[i]
        values = each.split(':')

        # check if we are dealing with a relevant chunk of information
        # must contain at least one ky and one value
        if len(values) >= 2:
            # Oh jesus it's a multi line value, throw it at the function
            if '[' in values[1]:
                readMultipleValues(values, i, cleanFile)
            # if it aint a multi line value, it's either garbage or a single line value
            else:
                readSingleValue(values)
    print(loadedData)


# appears to work
def readSingleValue(values):
    # print('Okay let us handle this one single value')
    if values[0] in acceptableWeaponKeys:
        print('KEY:', values[0])
        if values[1]:
            print('VALUE:', values[1])
            loadedData[values[0]] = [values[1]]
            # print('Row loading successful')
    return


def readMultipleValues(values, iterator, file):
    # print('multi')
    # empty our list
    valueList = []
    # save the current key
    currentKey = values[0]
    print('KEY: ', values[0])
    # strip the left bracket
    values[1] = values[1].replace("[", "")

    while ']' not in file[iterator]:
        print('Has not closed')

        # todo: fix off by one, usually resulting in a trailing ]

        # split the value, etc
        values = file[iterator + 1]
        valueList += values[0]
        print('current line:')
        print(values)
        iterator += 1
    else:
        print('End of line, line ends here')
        print(valueList)
        loadedData[currentKey] = valueList
    return





def display(button):
    for thing in loadedData:
        thing = str(thing.replace('[', ''))
        thing = str(thing.replace(']', ''))
    for key in acceptableWeaponKeys:
        app.addLabel(key)
        value = loadedData[key]
        app.addEntry(str(value))
        app.setEntry(str(value),str(loadedData[key]))
        #app.addEntry(loadedData[key])
        #print(loadedData[key])
        #app.addLabel(loadedData[key])
#todo: this
def save(button):
    print('no')

# create a GUI variable called app
app = gui(showIcon=0)
app.setTitle("AHHHHHHHHHHHH")

# add & configure widgets - widgets get a name, to help referencing them later
app.addLabel("title", "Starfarer shit editor version: yes okay")
app.addLabel("fileinfo", "Select a .wpn file")
app.addFileEntry("f1")
#app.setLabelBg("title", "")
# start the GUI
app.addButton("LOAD FILE", loadfile)
app.addButton("SHOW THE SHIT TO ME", display)
app.addButton("SAVE THIS SHIT (OH JESUS)", save)



app.go()