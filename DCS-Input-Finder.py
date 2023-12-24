import os
import shutil
from datetime import datetime

def find_and_copy_files_with_keyword():
    # Ask the user for source folder
    source_folder = input("Enter the full path of the folder that has the Input Settings Ex. \Saved Games\DCS.openbeta\Config\Input: ")

    # Ensure the source folder exists
    if not os.path.exists(source_folder):
        print(f"Source folder '{source_folder}' does not exist.")
        return

    # Ask the user for destination folder
    destination_folder = input("Enter the full path of the destination folder: ")

    # Ensure the destination folder exists, create it if not
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # Ask the user for file extension
    file_extension = input("Enter the file extension Should be (.lua): ")

    # Ask the user for the keyword
    keyword = input("Enter the name of the imput to filter files: ")

    # Iterate through files in the source folder
    for root, dirs, files in os.walk(source_folder):
        for file in files:
            # Check if the file has the specified extension and keyword in its name
            if file.endswith(file_extension) and keyword in file:
                source_path = os.path.join(root, file)

                # Create a folder in the destination directory corresponding to the parent folder of the file's location
                parent_folder = os.path.basename(os.path.dirname(root))
                destination_subfolder = os.path.join(destination_folder, parent_folder)

                # Ensure the destination subfolder exists, create it if not
                if not os.path.exists(destination_subfolder):
                    os.makedirs(destination_subfolder)

                # Create a unique destination filename
                timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
                destination_filename = f"{os.path.splitext(file)[0]}_{timestamp}{os.path.splitext(file)[1]}"
                destination_path = os.path.join(destination_subfolder, destination_filename)

                # Uncomment either shutil.copy or shutil.move based on your requirement
                shutil.copy(source_path, destination_path)  # Uncomment for copying
                # shutil.move(source_path, destination_path)  # Uncomment for moving

                print(f"File '{file}' copied/moved from {source_path} to {destination_path}")

# Call the function
find_and_copy_files_with_keyword()
