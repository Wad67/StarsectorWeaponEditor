# import the library
from appJar import gui
import csv
acceptableWeaponKeys = ['animationType','barrelMode','displayArcRadius','fireSoundTwo','hardpointAngleOffsets','hardpointOffsets','hardpointSprite','hardpointGunSprite']
loadedData = {}

def loadfile(button):
    filename = app.getEntry("f1")
    #print(filename)
    parsewpn(filename)
#    for key in data:
#        print(key)
#        for entry in key:
#            print(entry)
#todo: throw this away and do it again
def parsewpn(filename):
    print('parsing:',filename)
    with open(filename,'rt') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in reader:
            for each in row:
                each = each.replace("{","")
                each = each.replace("'", "")
                each = each.replace('"', "")
                each = each.replace(" ", "")
                if len(each) == 0:
                    break

                value = each.split(':')
                print(value)
                if len(value) == 2:
                    print('Current row has a length of two, continuing')
                    if value[0] in acceptableWeaponKeys:
                        print('key matched:',value[0])

                        if value[1]:
                            print('There was a value, lettuce continue:',value[1])
                            loadedData[value[0]] = [value[1]]
                            print('Row loading successful \n')
                else:
                    print('found some fuckin garbage',value[0])

def display(button):
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