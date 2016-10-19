# biohazardCleaning
avoid biohazards with well-crafted bioinformatics scripts (in the making) ... available in python and R

# alignmentDiffs.py
> take two alignments as a text file and check if they're "pretty much" the same or not

> script deficiencies: > does not work with all alignments yet
                       > should be able to take in a whole .nex, .fasta, .phy file but may not
                       > needs a more decisive factor on what is "the same"
                       
> brings up question:  > how similar must your genetics be in order to be the "same species"?

# captureRogueFiles.py
> takes files named by patterns and categorizes them into folder

> script usage:        > change the list "criteria" to reflect patterns you want to find
                       > change directories and directory names to reflect your folders
                       > rb_files contains my named files
                       > 

> script deficiencies: > would be better if written as a function
                       > does not work if a file does not exist
