#------------------------------------------#
# Title: CDInventory.py
# Desc: Script for Assignment 05
# Change Log: (Who, When, What)
# Bill McG… (name truncated for public internet post), 2022-Feb-27, Created File
#------------------------------------------#

# declare variables
# replaced list of lists with list of dicts
strChoice = "" # User input
lstTbl = []  # list of lists to hold data
dicRow = {}  # dictionary (replaced List lstRow)
#declare dictionary data types
intID = 0
strTitle = ""
strArtist = ""

rowToDelete = 0 # counter for delete functionality

strFileName = "CDInventory.txt"  # data storage file
objFile = None  # file object

# Get user Input
print("The Magic CD Inventory\n")
while True:
    # Menu allowing the user to choose:
    print("[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory")
    print("[d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit")
    strChoice = input("l, a, i, d, s or x: ").lower()
    print()
    # Program exit
    if strChoice == "x":
        break
    # Load from text file
    if strChoice == "l":
        lstTbl.clear()
        objFile = open(strFileName, "r") # open text file as read only
        for row in objFile:
            lstRow = row.strip().split(",")
            dicRow = {"ID": int(lstRow[0]), "CD Title": lstRow[1], "CD Artist": lstRow[2]}
            lstTbl.append(dicRow) 
        objFile.close() # close text file
    # Append to existing data within program variables not text file
    elif strChoice == "a":
        strID = input("Enter an ID (Integer Only!): ")
        strTitle = input("Enter the CD\"s Title: ")
        strArtist = input("Enter the Artist\"s Name: ")
        intID = int(strID)
        dicRow = {"ID": int(intID), "CD Title": strTitle, "CD Artist": strArtist}
        lstTbl.append(dicRow)
    # Display current inventory in memory (not text file)
    elif strChoice == "i":
        print("ID", "Artist, Title")
        for row in lstTbl:
            print(*row.values(), sep = ", ")
        print("\n")
    # Allow user to input the ID they wish to delete
    elif strChoice == "d":
        intIDtoDelete = input("Enter ID of CD that you want to delete: ")
        deleteID = int(intIDtoDelete)
        rowToDelete = 0        
        for row in lstTbl:
            if lstTbl[rowToDelete]["ID"] == deleteID:
                lstTbl.pop(rowToDelete)
            rowToDelete += 1
    # Save to text file
    elif strChoice == "s":
        objFile = open(strFileName, "w") # open text file write mode
        for row in lstTbl:
            strRow = ""
            for item in row.values():
                strRow += str(item) + ","
            strRow = strRow[:-1] + "\n"
            objFile.write(strRow)
        objFile.close() # close text file
        print("Data saved to text file!\n")
    else:
        print("Please choose either l, a, i, d, s or x!\n")

