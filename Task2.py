"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
from Task1 import build_numbers_list, extract_unique_numbers
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during
September 2016.".
"""


def unique_numbers(records):
    raw_numbers = build_numbers_list(calls)
    return extract_unique_numbers(raw_numbers)


def build_numbers_dictionary(numbers):
    numbers_dict = {}
    for num in numbers:
        numbers_dict[num] = 0
    return numbers_dict


def calc_call_totals(numbers_dictionary, calls):
    for call in calls:
        for number in numbers_dictionary:
            if number in call:
                numbers_dictionary[number] += int(call[-1])

    return numbers_dictionary


def key_with_max_value(dictionary):
    values = list(dictionary.values())
    keys = list(dictionary.keys())
    return keys[values.index(max(values))]


if __name__ == '__main__':
    unique_numbers_list = unique_numbers(calls)
    uniques_dictionary_init = build_numbers_dictionary(unique_numbers_list)
    uniques_dictionary_updated = calc_call_totals(
        uniques_dictionary_init, calls)
    number_with_longest_call_time = key_with_max_value(
        uniques_dictionary_updated)
    print('{} spent the longest time, {} seconds, on the phone during September 2016.'.format(
        number_with_longest_call_time, uniques_dictionary_updated[number_with_longest_call_time]))


# def task_handler(calls_data):
#     unique_numbers_list = unique_numbers(calls_data)
#     uniques_dictionary_init = build_numbers_dictionary(unique_numbers_list)
#     uniques_dictionary_updated = calc_call_totals(
#         uniques_dictionary_init, calls_data)
#     number_with_longest_call_time = key_with_max_value(
#         uniques_dictionary_updated)
#     return number_with_longest_call_time, uniques_dictionary_updated[number_with_longest_call_time]


# print('{} spent the longest time, {} seconds, on the phone during September 2016.'.format(
#     task_handler(calls)[0], task_handler(calls)[1]))
