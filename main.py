import os
'''
Python-3.9.1
Requirements in requirements.txt
Required: 
GPL Ghostscript,
Google Tesseract-OCR.
'''

CONVERTED_TAG = '_CONVERTED'  # All converted files will have a _CONVERTED in name.


def main(images_folder):
    if not os.path.isdir(images_folder):
        raise NotADirectoryError(f'{images_folder} não existe.')

    for root, dirs, files in os.walk(images_folder):
        for file in files:
            full_path = os.path.join(root, file)
            if CONVERTED_TAG in full_path:
                continue
            else:
                img_full_path = os.path.join(root, file)
                file_name, extension = os.path.splitext(file)
                new_file = file_name + CONVERTED_TAG + '.pdf'
                new_file_full_path = os.path.join(root, new_file)
                os.system(f'img2pdf {img_full_path} | ocrmypdf - {new_file_full_path}')


if __name__ == '__main__':
    folder = ''  # Put the path of images folder. Be careful, this script access subdirs.
    main(folder)
