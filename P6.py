from zipfile import ZipFile
import sys

# Name of zip file passed as a command line argument
zipFileName = sys.argv[1]
# Array of duplicate names
duplicates = []

# Open namelists.zip without extracting it
with ZipFile(zipFileName,'r') as zip:
    # Open the first file in the zipped archive
    with zip.open(zip.namelist()[0]) as firstFile:
        # For each line
        for line in firstFile:
            # Isolate the name
            nameOfPerson = line.decode('utf-8').strip()
            # Not a duplicate by default
            duplicate = False
            # Loop through all names in the rest of the files
            for file in zip.namelist()[1:]:
                # Open the text file
                with zip.open(file) as textFile:
                    # The name is by default not a duplicate
                    duplicate = False
                    # For each line
                    for line in textFile:
                        # Isolate the name
                        nameOfPerson2 = line.decode('utf-8').strip()
                        # If the name is a duplicate, set to true
                        if nameOfPerson2 == nameOfPerson:
                            duplicate = True
                    # If name is not a duplicate, break the loop
                    if duplicate == False:
                        break
            # If duplicate is True, add the name to the duplicates array
            if duplicate == True:
                duplicates.append(nameOfPerson)
            

# Write duplicates to output.txt
with open('output.txt','w') as output:
    for name in duplicates:
        output.write(name + '\n')
            
# Print the duplicate names
print("Duplicates:")
for name in duplicates:
    print(name)