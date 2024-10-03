import sys
import tabulate
import os
import csv

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")

elif len(sys.argv) < 3:
    sys.exit("Too many command-line arguments")

elif (
    os.path.splitext(sys.argv[1])[1] != ".jpg"
    or os.path.splitext(sys.argv[1])[1] != ".png"
    or os.path.splitext(sys.argv[1])[1] != ".jpeg"
):
    sys.exit("Not a JPG file")

elif os.path.isfile(sys.argv[1]) != True:
    sys.exit("File does not exist")

elif os.path.isfile(sys.argv[1]) == True:
    print("hiii")
else:
    print("wowowo")
