# This script defines a function to count the number of items less than 10 in a list of
# numbers.
def count_low(item_list: int):
    count = 0
    for item in item_list:
        while item < 10:
            count += 1
    return count

# Testing
test_list = [1, 3, 5, 12, 15, 8, 2]
number_low = count_low(test_list)
report = "Found " + count_low + " items less than 10."

print(report)