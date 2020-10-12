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
            count = int(current) + count
    return count


# Press the green button in the gutter to run the script.
# print(__name__)

def get_max():
    file_list = []
    result_list = []
    with open("/tcdata/num_list.csv", "r") as f:
        for line in f:
            file_list.append(int(line))
    print(file_list)
    length = 10
    if int(len(file_list)) < 10:
        length = int(len(file_list))

    for i in range(length):
        index = 0
        for i in range(len(file_list)):
            if file_list[i] > file_list[index]:
                index = i
        if file_list[index] == 0:
            break
        else:
            result_list.append(file_list[index])
            file_list[index] = 0
    print(result_list)

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
