__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

import os
import shutil
import zipfile
zip_bestand = os.path.join(os.getcwd(), 'files', 'data.zip')
cache_bestand = os.path.join(os.getcwd(), 'files','cache')


#1
def clean_cache():
    os.chdir('files')
    if os.path.exists('cache'):
        for files in os.listdir('cache'):
            files_path = os.path.join('cache', files)
            os.remove(files_path)
    else:
        os.mkdir('cache')

#2
def cache_zip(zip_file_path, cache_dir_path):

    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(cache_dir_path)

#3
def cached_files():
    cache_path = os.path.abspath("./cache")
    if not os.path.exists(cache_path):
        return []
    file_list = os.listdir(cache_path)
    file_list = [os.path.join(cache_path, f) for f in file_list if os.path.isfile(os.path.join(cache_path, f))]
    return file_list

#4
def find_password(file_list):
    password_indicator = "password: "
    for file_path in file_list:
        with open(file_path, "r") as f:
            for line in f:
                if password_indicator in line:
                    return line.split(password_indicator)[-1].strip()
    return None
patat = os.getcwd

if __name__ == "__main__":
    clean_cache()
    cache_zip(zip_bestand, cache_bestand)
    