Created to help sort Downloads directory for quicker review / cleanup. Sorts files in a specified directory by their file type into subdirectories named for the file type. For example, `.txt` files will go into a subdirectory named `txt`.

## Features

- Sorts files by their file extension.
- Skips hidden files and directories.
- Moves files without extensions to a `no_extension` subdirectory.
- Handles filename conflicts by appending a counter to the filename.
- Logs all file movements and errors to a log file named `file_sorter.log`.

## Requirements

- Python 3.x

## Usage

1. Clone the repository or download the script.

2. Run the script:

    ```sh
    python sort.py
    ```

3. Enter the directory path you want to sort when prompted.
