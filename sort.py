import os
import shutil
import logging

def sort_files_by_type(directory):
    # Check if the directory exists
    if not os.path.isdir(directory):
        print(f"The directory {directory} does not exist.")
        return

    # Set up logging
    logging.basicConfig(filename='file_sorter.log', level=logging.INFO, format='%(asctime)s - %(message)s')

    # Iterate over all files in the directory
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        # Skip directories and hidden files
        if os.path.isdir(file_path) or filename.startswith('.'):
            continue

        # Get the file extension
        if '.' in filename:
            file_extension = filename.split('.')[-1]
        else:
            file_extension = 'no_extension'

        # Create a subdirectory for the file type if it doesn't exist
        subdirectory = os.path.join(directory, file_extension)
        if not os.path.exists(subdirectory):
            os.makedirs(subdirectory)

        # Move the file to the subdirectory, handling conflicts
        destination_path = os.path.join(subdirectory, filename)
        if os.path.exists(destination_path):
            base, extension = os.path.splitext(filename)
            counter = 1
            new_filename = f"{base}_{counter}{extension}"
            destination_path = os.path.join(subdirectory, new_filename)
            while os.path.exists(destination_path):
                counter += 1
                new_filename = f"{base}_{counter}{extension}"
                destination_path = os.path.join(subdirectory, new_filename)

        try:
            shutil.move(file_path, destination_path)
            logging.info(f"Moved {file_path} to {destination_path}")
        except Exception as e:
            logging.error(f"Error moving {file_path} to {destination_path}: {e}")

if __name__ == "__main__":
    directory = input("Enter the directory path to sort: ")
    sort_files_by_type(directory)