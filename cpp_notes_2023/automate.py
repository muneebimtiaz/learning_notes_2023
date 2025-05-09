import os
import re
import shutil


def sort_and_rename_cpp_files(folder_path, output_folder=None):
    try:
        # List all C++ files in the folder
        cpp_files = [f for f in os.listdir(folder_path) if f.endswith('.cpp')]

        # Debug: Print the list of .cpp files
        print("List of .cpp files:")
        for cpp_file in cpp_files:
            print(cpp_file)

        # Extract numbers from file names and sort files
        file_info = []
        for file_name in cpp_files:
            match = re.match(r'(\d+)', file_name)
            if match:
                number = int(match.group(1))
                file_info.append((file_name, number))
        sorted_files = sorted(file_info, key=lambda x: (x[1], x[0]))

        # Determine the output folder
        if output_folder is None:
            output_folder = folder_path

        # Rename and move files to ensure consecutive numbering
        new_number = 1
        for file_name, _ in sorted_files:
            new_name = f"{new_number:02d}_{file_name}"
            old_path = os.path.join(folder_path, file_name)
            new_path = os.path.join(output_folder, new_name)

            # Rename and move the file
            shutil.move(old_path, new_path)

            new_number += 1

        print("Files sorted and renamed successfully.")

    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    folder_path = r"C:\Users\Muneeb\OneDrive\Desktop"
    sort_and_rename_cpp_files(folder_path, output_folder=None)
