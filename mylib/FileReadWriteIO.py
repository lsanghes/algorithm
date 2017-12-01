'''
The modes can be:
'r' when the file will only be read
'w' for only writing /or overwriting
'a' opens the file for appending;
'r+' opens the file for both reading and writing.
'''
file = 'c:\\Temp\\data.txt'
file = r'c:\Temp\data.txt'

# create new file/overwrite existing file
with open(file, 'w') as text_file:
    text_file.write('line1\n')

# append to existing file
with open(file, 'a') as text_file:
    text_file.write('line2\n')

# read file by line
with open(file, 'r') as text_file:
    lines = [line.rstrip('\n') for line in text_file]
    print(lines)
# read file short form
print([line.rstrip('\n') for line in open(file)])
