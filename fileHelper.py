import os

def openAndReplace(oldFilePath, newFilePath, toReplace, replaceWith):
    oldFile = open(oldFilePath, "r",encoding=('utf-8'))
    oldText = oldFile.read()
    oldFile.close()
    for x in toReplace:
        for y in replaceWith:
            oldText = oldText.replace(x,y)
    newText = oldText
    newFile = open(newFilePath, "w", encoding=('utf-8'))
    newFile.write(newText)
    newFile.close()

