import os
from shutil import move
from pathlib import Path

def organize_files_by_type(directory):
    # Ensure the directory exists
    if not os.path.isdir(directory):
        print(f"The directory {directory} does not exist.")
        return

    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        if os.path.isfile(item_path):
            # Extract the file extension and use it as the folder name
            file_type = Path(item).suffix[1:]  # Remove the dot from the extension
            if file_type == "":
                file_type = "Other"  # Handle files without an extension
            folder_path = os.path.join(directory, file_type)

            # Create the folder if it does not exist
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)

            # Move the file into its respective folder
            destination = os.path.join(folder_path, item)
            print(f"Moving {item} to {folder_path}")
            move(item_path, destination)

if __name__ == "__main__":
    target_directory = input("Enter the path to the directory you want to organize: ")
    organize_files_by_type(target_directory)
