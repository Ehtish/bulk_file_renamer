import os 


# Folder containing the files we want to rename
folder = "files_to_rename"


# Get all files from the folder
files = os.listdir(folder)

# Starting number for new file names
counter = 1

# Process each file
for file in files:

    # Get the file extension
    name,extension = os.path.splitext(file)

    # Create the new file name
    new_name = f"image_{counter:03d}{extension}"

    # Create the old file path
    old_path = os.path.join(folder,file)

    # Create the new file path
    new_path = os.path.join(folder,new_name)

    # Rename the file
    os.rename(old_path,new_path)

    # Display the result
    print(file, "→", new_name)

    counter += 1