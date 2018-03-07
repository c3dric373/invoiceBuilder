import os

def openAndReplace(oldFilePath, newFilePath, toReplace, replaceWith):
    oldFile = open(oldFilePath, "r",encoding=('utf-8'))
    oldText = oldFile.read()
    oldFile.close()
    for x in range(0,len(toReplace)):
        oldText = oldText.replace(toReplace[x],replaceWith[x])
    newText = oldText
    print(newText.encode('utf-8'))
    newFile = open(newFilePath, "w", encoding=('utf-8'))
    newFile.write(newText)
    newFile.close()

