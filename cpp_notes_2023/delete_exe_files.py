import os

def delete_exe_files(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".exe"):
                file_path = os.path.join(root, file)
                os.remove(file_path)
                print(f"Deleted: {file_path}")

if __name__ == "__main__":
    # Specify the directory where you want to search for and delete .exe files.
    desktop_directory = 'C:\\Users\\Muneeb\\OneDrive\\Desktop'

    # Call the function to delete .exe files.
    delete_exe_files(desktop_directory)
