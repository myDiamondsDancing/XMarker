class dictOfTabs(list):
    def __init__(self):
        self.listOfPaths = list()
        self.listOfEdits = list()
        self.listOfNames = list()
        
    def path(self, edit):
        return self.listOfPaths[self.listOfEdits.index(edit)]

    def addPath(self, path, edit):
        self.listOfPaths.append(path)
        self.listOfEdits.append(edit)

    def removePath(self, edit):
        self.listOfPaths.remove(self.listOfPaths[self.listOfEdits.index(edit)])
        self.listOfEdits.remove(edit)   
        
    def insertPath(self, edit, path):
        self.listOfPaths[self.listOfEdits.index(edit)] = path    