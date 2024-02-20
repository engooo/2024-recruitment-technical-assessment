from dataclasses import dataclass
from collections import Counter

@dataclass
class File:
    id: int
    name: str
    categories: list[str]
    parent: int
    size: int


"""
Task 1
"""
def leafFiles(files: list[File]) -> list[str]:
    hasChildren = set()
    noChildren = []

    # retrieve list of files with children
    for file in testFiles:
        if file.parent != -1:
            hasChildren.add(file.parent)

    # find complement to the hasChildren list of files
    for file in testFiles:
        if file.id not in hasChildren:
            noChildren.append(file.name)

    return noChildren


"""
Task 2
"""
def kLargestCategories(files: list[File], k: int) -> list[str]:
    # list of all categories
    categoriesList = []
    for file in files:
        categoriesList += file.categories
    
    # count occurrences of categories
    categoriesCounter = Counter(categoriesList)
    
    # sort in descending order (-categoriesCounter[x]) then alphabetically (x)
    categoriesSorted = sorted(categoriesCounter, key=lambda x: (-categoriesCounter[x], x))
    
    return categoriesSorted[:k]
    


"""
Task 3
"""
def largestFileSize(files: list[File]) -> int:
    if not files:
        return 0
    
    # dictionary to store each files id and size (inc its children)
    sizeDict = {}
    for file in files:
        sizeDict[file.id] = calculateFileSize(file, files, sizeDict)

    return max(sizeDict.values())

# helper function to calc the total size of a file and its children
def calculateFileSize(file, files, sizeDict):
    # base case: file size has already been calculated
    if file.id in sizeDict:
        return sizeDict[file.id]
    
    # calculate the size of the file including its own size
    totalSize = file.size
    
    # list of current file's children's file sizes
    childrenSizes = []
    for child in files:
        if child.parent == file.id:
            childrenSizes.append(calculateFileSize(child, files, sizeDict))
        
    totalSize += sum(childrenSizes)        
    sizeDict[file.id] = totalSize
    return totalSize
        
if __name__ == '__main__':
    testFiles = [
        File(3, "Folder", ["Folder"], -1, 0),
        File(1, "Document.txt", ["Documents"], 3, 1024),
        File(2, "Image.jpg", ["Media", "Photos"], 34, 2048),
        File(5, "Spreadsheet.xlsx", ["Documents", "Excel"], 3, 4096),
        File(8, "Backup.zip", ["Backup"], 233, 8192),
        File(13, "Presentation.pptx", ["Documents", "Presentation"], 3, 3072),
        File(21, "Video.mp4", ["Media", "Videos"], 34, 6144),
        File(34, "Folder2", ["Folder"], 3, 0),
        File(55, "Code.py", ["Programming"], -1, 1536),
        File(89, "Audio.mp3", ["Media", "Audio"], 34, 2560),
        File(144, "Spreadsheet2.xlsx", ["Documents", "Excel"], 3, 2048),
        File(233, "Folder3", ["Folder"], -1, 4096),
    ]

    assert sorted(leafFiles(testFiles)) == [
        "Audio.mp3",
        "Backup.zip",
        "Code.py",
        "Document.txt",
        "Image.jpg",
        "Presentation.pptx",
        "Spreadsheet.xlsx",
        "Spreadsheet2.xlsx",
        "Video.mp4"
    ]

    assert kLargestCategories(testFiles, 3) == [
        "Documents", "Folder", "Media"
    ]

    assert largestFileSize(testFiles) == 20992
