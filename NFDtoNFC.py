# Author: EasternPen9uin
# Program to revert the names of files that have separated Jamo characters
# on a Mac to their original form (NFD -> NFC)
# (or vice versa)

import os
from tkinter import filedialog, Tk
import unicodedata

def fileRename(filepath, select):
    filename = filepath.split('/')[-1]
    filenameChanged = unicodedata.normalize(select, filename)
    os.rename(filepath, filepath.replace(filename, filenameChanged))

if __name__ == "__main__":
    while True:
        while True:
            print("1: NFD -> NFC (Combine separated Jamo characters in Korean file names)")
            print("2: NFC -> NFD (Separate all Jamo characters in Korean file names)")
            i = input()
            if i in ('1', '2'):
                break
            else:
                print("Please enter only 1 or 2")

        select = ['NFC', 'NFD'][int(i)-1]
        root = Tk()
        root.withdraw()
        files = filedialog.askopenfilenames()
        for i in range(1, len(files)+1):
            print(f"Processing...[{i}/{len(files)}]")
            filepath = files[i-1]
            fileRename(filepath, select)
