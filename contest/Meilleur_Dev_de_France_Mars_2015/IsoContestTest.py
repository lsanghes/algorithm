import os
def print_test_result(test_data_path, solution):
    print("Test Result")
    print("------------------------------")
    for file_name in [f for f in os.listdir(test_data_path) if f.startswith('input')]:
        file_path_abs = test_data_path + os.sep + file_name
        print('<' + file_name + '>: expected output')
        for line in open(file_path_abs.replace('input', 'output')):
            print(line.rstrip())
        print()
        lines = [line.rstrip('\n') for line in open(file_path_abs)]
        print('<'  + file_name + '>: my output')
        solution(lines)
        print("------------------------------")
