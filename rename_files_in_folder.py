# Author - R I
import os

# Ask the user for the desired word to replace 'flickr'
filenameFormat = input("Please enter the file naming format: ")

# Set the directory where your files are located
directory = input("Enter the directory of files: ")

# Initialize a counter
counter = 1

# Iterate through all files in the directory
for filename in os.listdir(directory):
    # Extract the file extension
    _, ext = os.path.splitext(filename)

    # Define the new file name using the user-provided format and the file extension
    new_filename = f"{filenameFormat}-{counter}{ext}"

    # Form the full file paths
    src = os.path.join(directory, filename)  # source file path
    dst = os.path.join(directory, new_filename)  # destination file path

    # Rename the file
    os.rename(src, dst)
    print(f'Renamed {filename} to {new_filename}')

    # Increment the counter
    counter += 1

print('Renaming complete.')
