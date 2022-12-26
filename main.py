__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

#1
import os

def clean_cache():
    os.chdir('files')
    if os.path.exists('cache'):
        for files in os.listdir('cache'):
            files_path = os.path.join('cache', files)
            os.remove(files_path)
    else:
        os.mkdir('cache')
(clean_cache())

#2
import os
import shutil
import zipfile

def cache_zip(zip_file_path, cache_dir_path):
    if not os.path.exists(cache_dir_path):
        os.makedirs(cache_dir_path)

    for file in os.listdir(cache_dir_path):
        file_path = os.path.join(cache_dir_path, file)
        if os.path.isfile(file_path):
            os.unlink(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)

    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(cache_dir_path)

#3
import os

def cached_files():
    lists = []
    cache_dir_path = 'C:\\Users\\atill\\Onedrive\\Bureaublad\\important\\back-end developer\\Winc\\files\\cache'
    file_paths = [os.path.join(cache_dir_path, file) for file in os.listdir(cache_dir_path) if os.path.isfile(os.path.join(cache_dir_path, file))]
    lists.append(file_paths)
    return lists


#4
def find_password(files):
    # Iterate over the list of files
    for file in files:
        # Open the file for reading
        with open(file, 'r') as f:
            # Read the contents of the file
            contents = f.read()

            # Search for the password in the contents
            if 'password' in contents:
                # Return the password if found
                return contents.split('password:')[1].strip()

    # Return None if the password is not found in any of the files
    return None