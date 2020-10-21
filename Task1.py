"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""


def build_numbers_list(records):
    """Helper function that builds list of numbers from 
    calls/texts data sets. Indexes 0 and 1 are sender/receiver 
    numbers in each call/text record respectively."""
    numbers = []
    for entry in records:
        numbers.append(entry[0])
        numbers.append(entry[1])
    return numbers


def combine_lists(list_1, list_2):
    return list_1 + list_2


def extract_unique_numbers(numbers):
    return set(numbers)


def count_unique_numbers(data_set_1, data_set_2):
    """Constructs list of numbers from two data sets. 
    Combines and converts them to a set of unique numbers, 
    returning the length of the set."""
    data_set_1_numbers = build_numbers_list(data_set_1)
    data_set_2_numbers = build_numbers_list(data_set_2)

    combined_numbers_list = combine_lists(
        data_set_1_numbers, data_set_2_numbers)

    unique_numbers = extract_unique_numbers(combined_numbers_list)
    return len(unique_numbers)


# print('There are {} different telephone numbers in the records'.format(
#     count_unique_numbers(calls, texts)))
