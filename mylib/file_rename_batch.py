import os
import os.path
file_counts = 0
for dirpath, dirnames, filenames in os.walk("C:\\Users\\ssang\\algorithm"):
    for filename in filenames:
        if filename.startswith('lc'):
            i = filename.find('.')
            old_num = filename[2: i]
            old_file = os.path.join(dirpath, filename)

            new_num = old_num.rjust(3, '0')
            new_name = 'lc' + new_num + filename[i:]
            new_file = os.path.join(dirpath, new_name)

            if len(old_num) < 3:
                print(old_file)
                print(new_file)
                os.rename(old_file, new_file)
                file_counts += 1
print(file_counts)
