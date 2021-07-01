import os
import re

path = "C:\\Users\\Pranav Pagote\\Downloads\\unzip_me_for_instructions"

for folder, sub_folders, files in os.walk(path):

    for f in files:
        fil = open(os.path.join(folder, f), "r")
        phonePattern = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
        phone = re.search(phonePattern, fil.read())
        if (phone != None):
            print(phone.group())
