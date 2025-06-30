import shutil
import os

def copy_file_for_names(directory, source_filename, names_list):
    # Resolve the full path to the working directory
    dir_path = os.path.abspath(directory)

    # Construct the full path to the source file
    source_path = os.path.join(dir_path, source_filename)

    if not os.path.isfile(source_path):
        print(f"Source file '{source_filename}' not found in directory: {dir_path}")
        return

    for name in names_list:
        safe_name = name.replace(" ", "_")
        file_ext = os.path.splitext(source_filename)[1]
        new_filename = f"{safe_name}{file_ext}"
        destination_path = os.path.join(dir_path, new_filename)

        shutil.copy(source_path, destination_path)
        print(f"Created: {destination_path}")


relative_dir = "."             # Directory containing the source and where new files will go
source = "Account__c.field-meta.xml"  # source file to use as a template
names = ["firstAmericanFlatRate", "visaPercentFee"]  # Replace with your list of names

copy_file_for_names(relative_dir,source, names)