#!/usr/bin/env python3

# adds blocks to a provided index
# arg 1: the file to add to
# arg 2: the tag to look for
import os
import sys

dir = sys.argv[3]
file = sys.argv[1]
tag = sys.argv[2]

lookFor = f'{tag})' + "\n{: .label" 

# load the original file contents
with open(file, 'r') as fileBuffer:
    fileContents = fileBuffer.read()

# itterate through all blocks but alphabetize
blocks = os.listdir(dir)
blocks.sort()
for block in blocks:
    # Skip .bak files
    if block.find(".bak") == -1:
        address = dir + "/" + block
        name = block.removesuffix(".md")

        with open(address, 'r') as f:
            # Wrap our block with some HTML
            contents = f.read()
        # if the block has the tag add it to the other file
        if (lookFor in contents):
            fileContents += f'![{name}]({dir}/{name})\n'

# Replace the file
with open(file, 'w') as fileBuffer:
    fileBuffer.write(fileContents)