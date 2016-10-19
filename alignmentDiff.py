# alignDiffs Version 2

# Edie Espejo
# 14 July 2016

# Goal: Make a program that reads in two species from some alignment
#         We want to know if these species are likely the same species
#         We want to know which alignment has the most information

### Libraries
import os

### Informative Characters
## ATCG atcg
def getInfoChar(alignment):
    informativeSet=("A", "T", "C", "G", "a", "t", "c", "g")
    totalInfo=0
    
    for i in range(0, len(alignment)):
        if alignment[i] in informativeSet:
            totalInfo = totalInfo + 1

    return totalInfo

### Uninformative Characters
def getUninfoChar():
    informativeSet=("A", "T", "C", "G", "a", "t", "c", "g")
    totalUninfo=0
    questionMarks=0
    dashes=0
    other=0
    
    ## Dashes
    for i in range(0, len(alignment)):
        if alignment[i]=="-":
            dashes = dashes + 1
    
    ## Question Marks
    for i in range(0, len(alignment)):
        if alignment[i]=="?":
            questionMarks = questionMarks + 1

    ## Other Characters
    for i in range(0, len(alignment)):
        if alignment[i] not in informativeSet:
            other = other + 1

    summary = (dashes, questionMarks, other)
    print(summary)
    
    totalUninfo = dashes + questionMarks + other

    return totalUninfo


### Main Function
def alignDiffs():
    print("align Diffs Version 2. This version does not work for all alignments . . . yet.\n")
    print("Let's analyze two species!\n\n")
    print("Try this: /Users/edie/Dropbox/PhyloLab/fishbein.txt \n")
    informativeSet=("A", "T", "C", "G", "a", "t", "c", "g")
    
    ## Choose the alignment
    alignmentPath = input("Please enter the path of your alignment: ")
    alignment = open(alignmentPath, "r")

    ## Specify the first and second species
    print("\nCAUTION: Please enter species names as are spelled and capitalized in your alignment.\n")
    species1 = input("Please input the first species name: ")
    #    species1 = "Lambertia"
    species2 = input("Please input the second species name: ")
    #    species2 = "Dudleya"
    species1Len = len(species1)
    species2Len = len(species2)
    
    # Make program identify the species, then take in their information as strings
    lines = alignment.readlines()

    countLines=0
    
    for line in lines:
        if species1 in line:
            # print(line)
            species1Line=line
        
        if species2 in line:
            # print(line)
            species2Line=line

        # print(countLines)
        countLines = countLines + 1


    # Reformat Strings

    species1info = species1Line[species1Len:]

    species2info = species2Line[species2Len:]
    
    ## Check strings for each index in the alignment
    totalSimilarities = 0
    uninfoRegionLength = 0
    
    # If species1[i]==species2[ii], then record a number of similarities
    for i in range(0,len(species1info)):
        if species1info[i] == species2info[i]:
            # Ignore areas of long uninformative characters
            if species1info[i] not in informativeSet:
                if species2info[i] not in informativeSet:
                    # No change in similarities if no info
                    uninfoRegionLength = uninfoRegionLength + 1
            else:
                totalSimilarities = totalSimilarities + 1
                
    difference = 1 - (totalSimilarities/(len(species1info)-uninfoRegionLength))
    percentDifference = difference*100
    
    # If the species are around 99% similar, then they're probably the same species
    sameSpecies = 0
                      
    if percentDifference <= 2.5:
        sameSpecies = 1
        print("\n"+str(species1)+" and "+str(species2)+" are "+str(percentDifference)+"% different\n")
        print("CONCLUSION: These are the same species")
    else:
        print("\n"+str(species1)+" and "+str(species2)+" are "+str(percentDifference)+"% different\n")
        print("CONCLUSION: May not be same species")

    ## Output which species has more information
    species1infoChar = 0
    species2infoChar = 0
    
    if sameSpecies == 1:
        for i in range(0,len(species1info)):
            if species1info[i] in informativeSet:
                species1infoChar = species1infoChar + 1

        for i in range(0,len(species2info)):
            if species2info[i] in informativeSet:
                species2infoChar = species2infoChar + 2

    if sameSpecies == 1:
        if species1infoChar > species2infoChar:
            print(species1+" has more information")
        else:
            print(species2+" has more information")

    alignment.close()
