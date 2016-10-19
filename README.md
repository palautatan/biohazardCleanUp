# biohazardCleanUp
avoid biohazards with well-crafted bioinformatics scripts (in the making) ... available in python and R

# Table of Contents
1. alignmentDiffs.py
2. captureRogueFiles.py

# alignmentDiffs.py
take two alignments as a text file and check if they're "pretty much" the same or not

helpful when you are parsing trees for duplicate taxa

script usage:
1. test this out with the alignmentDiffsTesting.txt file /
2. try it with nexus files

script deficiencies:
1. does not work with all alignments yet /
2. should be able to take in a whole .nex, .fasta, .phy file but may not /
3. needs a more decisive factor on what is "the same"
                       
brings up question: how similar must your genetics be in order to be the "same species"?

# captureRogueFiles.py
takes files named by patterns and categorizes them into folder

helpful when you forgot to put your output into folders

sounds like a stupid mistake, but if you don't want to rerun your code, this is your fix

script usage:
1. change the list "criteria" to reflect patterns you want to find /
2. change directories and directory names to reflect your folders /
i.e. rb_files contains my named files, studies contains the folders i want to create

script deficiencies:
1. would be better if written as a function /
2. does not work if a file does not exist
