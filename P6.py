from zipfile import ZipFile

# Array of names iterated through
names = []
# Array of duplicate names
duplicates = []

# Open namelists.zip without extracting it
with ZipFile('namelists.zip','r') as zip:
    # For each file in the zipped archive
    for file in zip.namelist():
        # Open the text file
        with zip.open(file) as textFile:
            # For each line
            for line in textFile:
                # Isolate the name
                nameOfPerson = line.decode('utf-8').strip()
                # If the name is present in the names array, add the name to the duplicate array
                if nameOfPerson in names:
                    # If the name is already duplicated, don't add it again
                    if nameOfPerson not in duplicates:
                        duplicates.append(nameOfPerson)
                # Otherwise, add the name to the names array
                else:
                    names.append(nameOfPerson)

# Write duplicates to output.txt
with open('output.txt','w') as output:
    for name in duplicates:
        output.write(name + '\n')
            
# Print the duplicate names
print("Duplicates:")
for name in duplicates:
    print(name)