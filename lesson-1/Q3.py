# Write a OS module to read all the file that are present in my device ( internal modules)

import os

directory ="C:\Program Files"
contanes=os.listdir(directory) 
for content in contanes:
    print (content)
