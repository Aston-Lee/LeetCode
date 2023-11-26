class Folder:
    def __init__(self):
        self.childfolder = defaultdict(set)
        self.files = defaultdict(str)
        # self.files = ""
        
    

class FileSystem:

    def __init__(self):
        self.root = Folder()
        

    def ls(self, path: str) -> List[str]:
        root = path[0]
        currentfolder = self.root
        tmpPath = ""
        for char in path[1:]:
            # print(char, tmpPath, list(currentfolder.childfolder))
            if char == '/':
                if tmpPath not in currentfolder.childfolder:
                    return []
                currentfolder = currentfolder.childfolder[tmpPath]
                tmpPath = ""
            else:
                tmpPath += char
        
        last_part = tmpPath
        if last_part in currentfolder.files:  # If the last part is a file
            return [last_part]
        elif last_part in currentfolder.childfolder:  # If the last part is a directory
            target_folder = currentfolder.childfolder[last_part]
            return sorted(list(target_folder.childfolder) + list(target_folder.files.keys()))
        else:
            return []  # Return empty list if the path is invalid
    def ls(self, path: str) -> List[str]:
        if path == "/":  # Handle the root directory
            # Combine and sort the names of child folders and files in the root
            return sorted(list(self.root.childfolder.keys()) + list(self.root.files.keys()))

        parts = path.split('/')[1:]  # Split the path and ignore the leading '/'
        currentfolder = self.root

        for part in parts[:-1]:  # Traverse through the path to reach the target folder
            if part not in currentfolder.childfolder:
                return []  # Return empty list if a directory in the path does not exist
            currentfolder = currentfolder.childfolder[part]

        last_part = parts[-1]
        if last_part in currentfolder.files:  # If the last part is a file
            return [last_part]
        elif last_part in currentfolder.childfolder:  # If the last part is a directory
            target_folder = currentfolder.childfolder[last_part]
            return sorted(list(target_folder.childfolder.keys()) + list(target_folder.files.keys()))
        elif last_part == "":  # If the last part is empty, it's the end of a directory path
            return sorted(list(currentfolder.childfolder.keys()) + list(currentfolder.files.keys()))
        else:
            return []  # Return empty list if the path is invalid
      
        

    def mkdir(self, path: str) -> None:
        if path[-1] != '/':
            path += '/'
        root = path[0]
        currentfolder = self.root
        tmpPath = ""
        for char in path[1:]:
            if char == '/':
                if tmpPath not in currentfolder.childfolder:
                    currentfolder.childfolder[tmpPath] = Folder()
                currentfolder = currentfolder.childfolder[tmpPath]
                tmpPath = ""
            else:
                tmpPath += char
        return None
        

    def addContentToFile(self, filePath: str, content: str) -> None:
        path = filePath
        root = path[0]
        currentfolder = self.root
        tmpPath = ""
        for char in path[1:]:
            # print(char, tmpPath, list(currentfolder.childfolder))
            if char == '/':
                if tmpPath not in currentfolder.childfolder:
                    currentfolder.childfolder[tmpPath] = Folder()
                currentfolder = currentfolder.childfolder[tmpPath]
                tmpPath = ""
            else:
                tmpPath += char

        currentfolder.files[tmpPath] += content
        return None
        

    def readContentFromFile(self, filePath: str) -> str:
        path = filePath
        root = path[0]
        currentfolder = self.root
        tmpPath = ""
        for char in path[1:]:
            if char == '/':
                if tmpPath not in currentfolder.childfolder:
                    return []
                currentfolder = currentfolder.childfolder[tmpPath]
                tmpPath = ""
            else:
                tmpPath += char
        
        return currentfolder.files[tmpPath]

'''
["FileSystem","mkdir","ls","ls","mkdir","ls","ls","addContentToFile","ls","ls","ls"]

[[],["/goowmfn"],["/goowmfn"],["/"],["/z"],["/"],["/"],["/goowmfn/c","shetopcy"],["/z"],["/goowmfn/c"],["/goowmfn"]]

'''
                    


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)