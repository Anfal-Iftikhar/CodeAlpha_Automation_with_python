import os
import shutil

def organize_files(directory):
    # Create the target directory if it doesn't exist
    if not os.path.exists(directory):
        os.makedirs(directory)
        print(f'Created directory: {directory}')
        
    # Change the current working directory to the specified directory
    os.chdir(directory)

    # Loop through all files in the directory
    for filename in os.listdir(directory):
        # Check if it's a file (not a directory)
        if os.path.isfile(filename):
            # Get the file extension
            file_extension = filename.split('.')[-1] if '.' in filename else 'no_extension'
            # Create a new directory for the file extension if it doesn't exist
            if not os.path.exists(file_extension):
                os.makedirs(file_extension)
            # Move the file into the corresponding directory
            shutil.move(filename, os.path.join(file_extension, filename))
            print(f'Moved: {filename} to {file_extension}/')

if __name__ == "__main__":
    # Specify the directory you want to organize
    target_directory = os.path.expanduser('~/Documents/OrganizedFiles')  # This will create a folder in your Documents
    organize_files(target_directory)