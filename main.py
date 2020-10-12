# This is a sample Python script.
import json


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def print_hi():
    # Use a breakpoint in the code line below to debug your script.
    # print('Hello world')  # Press Ctrl+F8 to toggle the breakpoint.
    return 'Hello world'


def get_sum():
    count = 0
    with open("/tcdata/num_list.csv", "r") as f:
        for line in f:
            current = line.rstrip()
            # print(current)
            count = int(current) + count
    return count


# Press the green button in the gutter to run the script.
# print(__name__)

def get_max():
    file_list = []
    result_list = []
    min_num = 0
    with open("/tcdata/num_list.csv", "r") as f:
        for line in f:
            if line in file_list:
                continue
            else:
                file_list.append(int(line))

    length = 10
    if int(len(file_list)) < 10:
        length = int(len(file_list))

    for i in range(length):
        current_max = 0
        for current in file_list:
            if current in result_list:
                continue
            if current > current_max:
                current_max = current
        if current_max == 0:
            break
        else:
            result_list.append(current_max)
    return result_list


if __name__ == '__main__':
    result = {
        'Q1': print_hi(),
        'Q2': get_sum(),
        'Q3': get_max()
    }

    # 打开一个文件
    with open("result.json", "w") as f:
        json.dump(result, f)
