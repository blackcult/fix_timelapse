from ast import arg
import os
import argparse
import datetime
import shutil


parser = argparse.ArgumentParser(description='path')
parser.add_argument("--path", type=str, required=True)
args = parser.parse_args()

files = []
for r, d, f in os.walk(args.path):
    for file in f:
        if '.jpg' in file:
            no_jpg = file.replace(".jpg","")
            timestamp = datetime.datetime.fromtimestamp(int(no_jpg)/1000)
            time = timestamp.strftime("%H%M")
            if '1930' in time:
                original = os.path.join(r, file)
                destination = f'{args.path}/export/{file}'
                shutil.copyfile(original, destination)