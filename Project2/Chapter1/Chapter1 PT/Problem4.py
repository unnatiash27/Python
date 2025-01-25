import os

# Function to print the contents of a directory
def print_directory_contents(directory_path):
    try:
        # List all files and directories
        contents = os.listdir(directory_path)
        print(f"Contents of '{directory_path}':")
        for item in contents:
            print(item)
    except FileNotFoundError:
        print(f"The directory '{directory_path}' does not exist.")
    except PermissionError:
        print(f"Permission denied to access '{directory_path}'.")

# Specify the directory path
directory_path = input("Enter the directory path: ")

# Call the function
print_directory_contents(directory_path)
