import os
import shutil
from tkinter import *

#Returns the index of the last occurence of given substring in given string
def lastOccur(phr, sub):
    exit = False
    currPos = -1    #current pointer position
    lastBegin = 0   #last valid pointer position
    while exit != True:
        currPos = phr.find(sub, currPos+1)
        if currPos == -1:
            exit = True
        else:
            lastBegin = currPos
    return lastBegin

#Reuturns a tuple (name, extension) containing the given fileName split into name and extension
def fileNameSplit(fileName):
    name = ""
    extension = ""
    extBegin = lastOccur(fileName, ".")
    
    name = fileName[:extBegin]
    extension  = fileName[extBegin:]
    return (name, extension)

#Removes the suffix from given name (suffix beginning with '_') and returns the "pure" name (without suffix)
def suffixRem(name):
    cutName = ""
    suffBegin = lastOccur(name, "-")
    if suffBegin == 0:#Suffix not fount -> return name
        return name
        
    cutName = name[:suffBegin]
    return cutName

#Replaces the original model with the custom ones
def applySelection(fileName):
    #Baking path
    fileSplit = fileNameSplit(fileName)
    pureName = suffixRem(fileSplit[0])

    srcPath = "alternate/" + fileName       #Required Model
    destPath = pureName + fileSplit[1]  #Current Model

    print("Old model file: " + destPath)
    print("Required model file: " + srcPath + "\n")

    #Delete current active game file
    if os.path.isfile(destPath) == True:        #Error Handling
        os.remove(destPath)
    else:
        print("File not found: " + destPath)

    #Copy new game file in the main directory
    if os.path.isfile(srcPath) == True:         #Error Handling
        shutil.copyfile(srcPath, destPath)
    else:
        print("File not found: " + srcPath)

#Lynks the checkboxes state with model names then calls applySelection() to switch models
def getFileName():
    if nine_mm.get() == 1:
        applySelection("v_9mmAR.mdl")
    if nine_mm_h.get() == 1:
        applySelection("v_9mmAR-handed.mdl")
    if shotgun.get() == 1:
        applySelection("v_shotgun.mdl")
    if shotgun_gh.get() == 1:
        applySelection("v_shotgun-glockhand.mdl")
    if zombie.get() == 1:
        applySelection("zombie.mdl")
    if zombie_b.get() == 1:
        applySelection("zombie-blue.mdl")
    if bull.get():
        applySelection("bullsquid.mdl")
        applySelection("bullsquid01.mdl")
    if bull_c.get():
        applySelection("bullchik.mdl")
        applySelection("bullchik01.mdl")


#******GRAPHICS*****
#Tk init
window = Tk()
window.geometry("300x300")
window.title("Model Selector")

#Checkbuttons vars
#9mmAR
nine_mm = IntVar()      #Tkinter types
nine_mm_h = IntVar()
#shotgun
shotgun = IntVar()
shotgun_gh = IntVar()
#zombie
zombie = IntVar()
zombie_b = IntVar()
#bullsquid
bull = IntVar()
bull_c = IntVar()

#Checkbuttons
#9mmAR
nine_mm_check = Checkbutton(window, text = "v_9mmAR", variable = nine_mm)
nine_mm_h_check = Checkbutton(window, text = "v_9mmAR-handed", variable = nine_mm_h)
#shotgun
shotgun_check = Checkbutton(window, text = "v_shotgun", variable = shotgun)
shotgun_gh_check = Checkbutton(window, text = "v_shotgun-glockhand", variable = shotgun_gh)
#zombie
zombie_check = Checkbutton(window, text = "zombie", variable = zombie)
zombie_b_check = Checkbutton(window, text = "zombie-blue", variable = zombie_b)
#bullsquid
bull_check = Checkbutton(window, text = "bullsquid", variable = bull)
bull_c_check = Checkbutton(window, text = "bullchik", variable = bull_c)

#Labels
#9mmAR
label_9mm = Label(window, text = "--> v_9mmAR Models:")
#shotgun
label_shotgun = Label(window, text = "--> v_shotgun Models:")
#zombie
label_zombie = Label(window, text = "--> zombie Models:")
#bullsquid
label_bull = Label(window, text = "--> bullsqiud Models:")

#Buttons
applyChanges = Button(window, text = "Apply Models", command = getFileName)

#Building Layout (TOP-DOWN)
#9mmAR
label_9mm.grid(row = 0, column = 0)

nine_mm_check.grid(row = 1, column = 0)
nine_mm_h_check.grid(row = 1, column = 1)
#shotgun
label_shotgun.grid(row = 2, column = 0)

shotgun_check.grid(row = 3, column = 0)
shotgun_gh_check.grid(row = 3, column = 1)
#zombie
label_zombie.grid(row = 4, column = 0)

zombie_check.grid(row = 5, column = 0)
zombie_b_check.grid(row = 5, column = 1)
#bullsquid
label_bull.grid(row = 6, column = 0)

bull_check.grid(row = 7, column = 0)
bull_c_check.grid(row = 7, column = 1)
#apply button
applyChanges.grid(row = 8, column = 0)

#MainLoop
window.mainloop()
#***END_GRAPHICS***