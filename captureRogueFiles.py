#########################
## CAPTURE ROGUE FILES ##
## 2016-10-19          ##
#########################

## You would use this script in order to match up "perfectly named" files
## i.e. you have probably generated files computationally with "matchable names"
## and you forgot to put them into respective folders
## This script can fix your problem
## I used this script to match some of my output scripts into folders

## Libraries
import sys, re
from os import listdir
from os import makedirs
from os import rename
from operator import add

## rb_files holds all the files i want to match up to folders
rb_path = "/Users/treehouse5/Desktop/RevBayes/"
all_files = listdir(rb_path)
rb_files = list()

for filename in all_files:
    if ".Rev" in filename:
        rb_files.append(filename)

del all_files

## studies holds the names of the files that i want to create
studies_path = "/Users/treehouse5/Dropbox/effect_of_partitioning/even_newer_temp_directory/data/"
all_files = listdir(studies_path)
studies = list()

for filename in all_files:
    if "." not in filename:
         studies.append(filename)       

del all_files

## look at the files in rb_files
## check against the filenames in studies
## do the files in rb_files have studyname_aic | studyname_bic |studyname_gene | studyname_together 
## | studyname_all_apart | studyname_gene ?

criteria = ["_aic.Rev", "_bic.Rev", "_gene.Rev", "_together.Rev", "_all_apart.Rev"]

for file in rb_files:
    for study in studies:
        possible_files = list()
        
        for criterion in criteria:
            possible_files.append(study+criterion)    
        
        if file in possible_files:
            if not os.path.exists(rb_path+study):
                os.makedirs(rb_path+study)
            os.rename(rb_path+file, rb_path+study+"/"+file)
            print(study+" matches with "+file)
            
## This script does not function if certain files do not exist where they should
## This script needs to be edited to care/not care if these files do/do not exist
