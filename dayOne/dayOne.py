# list of nums to be filled
main_list = []

# reads in list
with open('dayOneData.txt', 'r') as infile:
    for line in infile:
        line.strip()
        main_list.append(int(line))


# sorts list (insertion sort)
def sort_dat_ish(a_list):
    for index in range(1, len(a_list)):
        val = a_list[index]
        pos = index - 1
        while pos >= 0 and a_list[pos] > val:
            a_list[pos + 1] = a_list[pos]
            pos -= 1
        a_list[pos + 1] = val


# searches list (binary search)
def search_dat_ish(a_list, target):
    start = 0
    end = len(a_list) - 1
    while start <= end:
        middle = (start + end) // 2
        if a_list[middle] == target:
            return True
        if a_list[middle] > target:
            end = middle - 1
        else:
            start = middle + 1
    return False


# finds 2020 with two nums
def find_twenty_twenty_with_two(a_list):
    sort_dat_ish(a_list)
    for num in a_list:
        val = 2020 - num
        if search_dat_ish(a_list, val) is True:
            print(val * num)
            return val * num


# finds two nums less than that equal (2020 - x) (linear search)
def find_with_two(a_list, n):
    n_exclude = 2020 - n
    sort_dat_ish(a_list)
    for num in a_list:
        val = n - num
        if search_dat_ish(a_list, val) is True and val is not n_exclude:
            return val, num


# finds 2020 with three nums
def find_twenty_twenty_with_three(a_list):
    for numOne in a_list:
        for numTwo in a_list:
            for numThree in a_list:
                if numOne + numTwo + numThree == 2020:
                    return numOne * numTwo * numThree
