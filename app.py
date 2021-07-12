import os
import shutil

download_dir = r'C:\Users\Ralf\Downloads'
document_dir = r'Documents'
exe_dir = r'exe_file'
zip_dir = r'zip_file'
pic_dir = r'Picture'

#Documents
pdf_dir = os.path.join(document_dir, r'pdf_file')
doc_dir = os.path.join(document_dir, r'docs_file')
pp_dir = os.path.join(document_dir, r'pp_file')

list_dir = os.listdir(download_dir)


if not os.path.isdir(os.path.join(download_dir, document_dir)):
    os.makedirs(os.path.join(download_dir, document_dir))

if not os.path.isdir(os.path.join(download_dir, pdf_dir)):
    os.makedirs(os.path.join(download_dir, pdf_dir))

if not os.path.isdir(os.path.join(download_dir, doc_dir)):
    os.makedirs(os.path.join(download_dir, doc_dir))

if not os.path.isdir(os.path.join(download_dir, pp_dir)):
    os.makedirs(os.path.join(download_dir, pp_dir))

if not os.path.isdir(os.path.join(download_dir, exe_dir)):
    os.makedirs(os.path.join(download_dir, exe_dir))

if not os.path.isdir(os.path.join(download_dir, zip_dir)):
    os.makedirs(os.path.join(download_dir, zip_dir))

if not os.path.isdir(os.path.join(download_dir, pic_dir)):
    os.makedirs(os.path.join(download_dir, pic_dir))


for item in list_dir:   
    if item.endswith(".pptx"):
        shutil.move(download_dir + r'\\' + item, os.path.join(download_dir, pp_dir))
    if item.endswith(".pdf"):
        shutil.move(download_dir + r'\\' + item, os.path.join(download_dir, pdf_dir))
    if item.endswith(".exe"):
        shutil.move(download_dir + r'\\' + item, os.path.join(download_dir, exe_dir))
    if item.endswith(".doc") or item.endswith(".docx"):
        shutil.move(download_dir + r'\\' + item, os.path.join(download_dir, doc_dir))
    if item.endswith((".jpg", "jpeg", "png", "gif")):
        shutil.move(download_dir + r'\\' + item, os.path.join(download_dir, pic_dir))

