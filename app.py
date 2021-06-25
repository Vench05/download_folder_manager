import os
import shutil

download_dir = r'C:\Users\Ralf\Downloads'
pdf_dir = r'pdf_file'
exe_dir = r'exe_file'

list_dir = os.listdir(download_dir)


if not os.path.isdir(os.path.join(download_dir, pdf_dir)):
    os.makedirs(os.path.join(download_dir, pdf_dir))

if not os.path.isdir(os.path.join(download_dir, exe_dir)):
    os.makedirs(os.path.join(download_dir, exe_dir))


for item in list_dir:   
    if item.endswith(".pdf"):
        shutil.move(download_dir + r'\\' + item, os.path.join(download_dir, pdf_dir))
    if item.endswith(".exe"):
        shutil.move(download_dir + r'\\' + item, os.path.join(download_dir, exe_dir))
