import re, os

def fix_hash(s):
    # add a space after #
    ret = re.sub('(#+)([^#\s])', '\g<1> \g<2>', s)
    return ret

def fix_print(s):
    # convert print function into print()
    ret = ''
    if s.endswith('\\n",\n'):
        ret = re.sub(r'("\s*print)\s*(.*)(\\n")', '\g<1>(\g<2>)\g<3>', s)
    else:
        ret = re.sub('(print)\s(.*)"', '\g<1>(\g<2>)"', s)
    return ret

def fix_notebook(file_path):
    print(file_path)
    with open(file_path, "r", encoding='UTF8') as file:
        lines = file.readlines()
    dirpath, filename = os.path.split(file_path)
    new_file_path = os.path.join(dirpath,'_py3.'.join(filename.split('.')))
    print(new_file_path)
    with open(new_file_path, "w", encoding='UTF8') as file:
        for line in lines:
            line = fix_print(line)
            line = fix_hash(line)
            file.write(line)

fix_notebook(r'C:\Users\ssang\Documents\lsang\cs109\hw_backup\hw0\hw0.ipynb')
fix_notebook(r'C:\Users\ssang\Documents\lsang\cs109\hw_backup\hw1\hw1.ipynb')
fix_notebook(r'C:\Users\ssang\Documents\lsang\cs109\hw_backup\hw2\hw2.ipynb')
fix_notebook(r'C:\Users\ssang\Documents\lsang\cs109\hw_backup\hw3\hw3.ipynb')
fix_notebook(r'C:\Users\ssang\Documents\lsang\cs109\hw_backup\hw4\hw4.ipynb')
fix_notebook(r'C:\Users\ssang\Documents\lsang\cs109\hw_backup\hw5\hw5part1.ipynb')
fix_notebook(r'C:\Users\ssang\Documents\lsang\cs109\hw_backup\hw5\hw5part2.ipynb')
