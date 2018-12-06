# import the library
import json

from appJar import gui

loadedData = {}

acceptableWeaponKeys = ['id', 'animationType', 'barrelMode', 'displayArcRadius', 'fireSoundTwo',
                        'hardpointAngleOffsets', 'hardpointOffsets', 'hardpointSprite', 'hardpointGunSprite']
print(loadedData)

def loadfile(button):
    global loadedData
    filename = app.getEntry("f1")
    # print(filename)
    # loadedData = loadWpnFile(filename)
    with open(filename, 'r') as content_file:
        file = content_file.read()
    # weird erroneous shit to handle:
    file = file.replace('ROUGH', '"ROUGH"')

    file = file.replace('\n', ' ').replace('\r', '')
    file = file.replace(' ', '')

    loadedData = eval(file)
    print(loadedData)
    print(type(loadedData))


# todo: this
def save(button):
    global loadedData
    filename = app.getEntry("f1")
    file = open(filename, 'w')
    loadedData['textureType'] = loadedData['textureType'].replace('"ROUGH"', 'ROUGH')
    json.dump(loadedData, file)

    print('FUCK')


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