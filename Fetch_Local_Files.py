import os, glob

os.chdir("E:\Photos")
for file in glob.glob("*.jpg"):
    print(file)