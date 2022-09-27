# https://hansonminlearning.tistory.com/42

path_to_zip_file = './appinfo.zip'
directory_to_extract_to = './temp'

import zipfile

with zipfile.ZipFile(path_to_zip_file, 'r') as zip_ref:
    zip_ref.extractall(directory_to_extract_to)
