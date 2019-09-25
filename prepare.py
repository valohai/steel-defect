import zipfile
import sys
import glob
import os

path_to_zip_file = sys.argv[1]
directory_to_extract_to = sys.argv[2]

print(os.path.join(path_to_zip_file, '*.zip'))
print(glob.glob(os.path.join(path_to_zip_file, '*.zip')))

for zipfile_path in glob.glob(os.path.join(path_to_zip_file, '*.zip')):
    print("Unzipping %s" % (zipfile_path))
    with zipfile.ZipFile(zipfile_path, 'r') as zip_ref:
        zip_ref.extractall(directory_to_extract_to)
