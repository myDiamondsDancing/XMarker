import os

def getFileName(file):
    if file is None: return 'Empty'
    return os.path.basename(file)
    
def getFormat(file):
    if file is None: return 'Empty'
    return os.path.splitext(file)[1]
   
